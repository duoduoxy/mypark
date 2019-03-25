from django.shortcuts import render
from django.http import HttpResponse
from park.models import *
from django.views.decorators.csrf import csrf_exempt
from park.utils.get_time import get_normal_time, get_current_month, get_timestamp
from park.image_recognition.predict import CardPredictor

import math

class UserPage:

    MONTH_FEE = 10.00
    MINUTE_FEE = 1.00

    def to_index(self, request):
        user_name = request.POST['name']
        user_pass = request.POST['password']
        user = User.objects.filter(name=user_name, password=user_pass).first()
        if user is None:
            return HttpResponse(render(request, 'user_login.html'))
        request.session["user_id"] = user.userID
        request.session["user_name"] = user.name
        request.session['is_owner'] = user.isOwner
        current_month = get_current_month()
        if user.isOwner == "1":
            if int(user.payMonth == current_month) and user.payState == 1:
                request.session['pay_state'] = "已包月"
            elif int(user.payMonth < current_month):
                state = self.charge_for_park(user.userID, current_month)
                if state:
                    request.session['pay_state'] = '已包月'
                else:
                    request.session['pay_state'] = '余额不足'
        else:
            request.session["pay_state"] = "无包月服务"
        return HttpResponse(render(request, 'user_main_page.html'))

    def charge_for_park(self, id, current_month):
        balance = float(Balance.objects.filter(userID_id=id).first().balance)
        if balance >= self.MONTH_FEE:
            balance = balance -self.MONTH_FEE
            Balance.objects.filter(userID_id=id).update(balance=balance)
            User.objects.filter(userID=id).update(payMonth=current_month, payState=1)
            return True
        else:
            return False

    def go_register(self, request):
        return HttpResponse(render(request, "user_register_page.html"))

    def register(self, request):
        user = {
            "name": request.POST["name"],
            "password": request.POST["password"]
        }
        User.objects.create(**user)
        return HttpResponse(render(request, "user_login.html"))

    @csrf_exempt
    def get_notification(self, request):
        notification = Notification.objects.all().last()
        return HttpResponse(notification.title + ":" +  notification.content)

    def to_info(self, request):
        return HttpResponse(render(request, "info.html"))

    def to_park(self, request):
        return HttpResponse(render(request, "park.html"))

    def to_charge(self, request):
        return HttpResponse(render(request, "charge.html"))

    def to_comment(self, request):
        return HttpResponse(render(request, "comment.html"))

    @csrf_exempt
    def get_balance(self, request):
        return HttpResponse(Balance.objects.filter(userID=request.POST["id"]).first().balance)

    @csrf_exempt
    def get_position(self, request):
        infoID = PositionBind.objects.filter(userID=request.POST["id"]).first().infoID_id
        print(infoID)
        parkinfo = ParkInfo.objects.filter(infoID=infoID).first()
        return HttpResponse(str(parkinfo.parkID_id + parkinfo.positionID_id))

    @csrf_exempt
    def submit_comment(self, request):
        print(request.POST["hygiene"])
        comment = {
            "time": get_normal_time(),
            "comment": request.POST["comment_content"],
            "userID_id": request.POST["user_id"],
            "hygiene": request.POST["hygiene"],
            "platform": request.POST["platform"],
            "service": request.POST["service"],
        }
        Comment.objects.create(**comment)
        return HttpResponse("success");

    @csrf_exempt
    def pic_upload(self, request):
       file_obj = request.FILES.get("file")
       f = open('test.jpg', 'wb')
       for chunk in file_obj.chunks():
           f.write(chunk)
       f.close()
       card_predictor = CardPredictor()
       card_predictor.train_svm()
       card, roi, color = card_predictor.predict("test.jpg")
       result = ''
       for each in card:
           result += each
       return HttpResponse(result)

    @csrf_exempt
    def confirm_park(self, request):
        position = request.POST["position"]
        if request.POST["is_owner"] =="1":
            ParkInfo.objects.filter(parkID_id=position[0], positionID_id=position[1]+position[2]).update(isBusy="yes", userID=request.POST["user_id"],carID=request.POST["car_id"])
        else:
            ParkInfo.objects.filter(parkID_id=position[0], positionID_id=position[1]+position[2]).update(isBusy="yes", userID=request.POST["user_id"],carID=request.POST["car_id"], minute=get_timestamp())
        User.objects.filter(userID=request.POST["user_id"]).update(oncePark="1")
        return HttpResponse("success")



    @csrf_exempt
    def finish(self, request):
        position = request.POST["position"]
        parkinfo = ParkInfo.objects.filter(parkID_id=position[0], positionID_id=position[1]+position[2])
        if request.POST["is_owner"] == "1":
            parkinfo.update(isBusy="no", userID="-1", carID="")
            User.objects.filter(userID=request.POST["user_id"]).update(oncePark="0")
            return HttpResponse("success")
        else:
            start_time = parkinfo.first().minute
            end_time = get_timestamp()
            count_minute = math.ceil((end_time-start_time)/60)
            balance = float(Balance.objects.filter(userID_id=request.POST["user_id"]).first().balance)
            if count_minute*self.MINUTE_FEE <= balance:
                parkinfo.update(isBusy="no", userID="-1", carID="", minute=0)
                User.objects.filter(userID=request.POST["user_id"]).update(oncePark="0")
                balance = balance-count_minute*self.MINUTE_FEE
                Balance.objects.filter(userID_id=request.POST["user_id"]).update(balance=str(balance))
                return HttpResponse("您总共消费了" + str(count_minute*self.MINUTE_FEE) + "元")
            else:
                return HttpResponse("您的余额不足,请先充值")

    @csrf_exempt
    def once_park(self, request):
        once_park = User.objects.filter(userID=request.POST["user_id"]).first().oncePark
        if int(once_park) == 0:
            return HttpResponse("success")
        else:
            return HttpResponse("fail")

    @csrf_exempt
    def get_user_parkinfo(self, request):
        parkinfo = ParkInfo.objects.filter(userID=request.POST["user_id"])
        if parkinfo.first() is not None:
            return HttpResponse(parkinfo.first().parkID_id + parkinfo.first().positionID_id)
        else:
            return HttpResponse("")
