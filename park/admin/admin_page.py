from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from park.models import *
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from park.utils import get_time

import json

class AdminPage:

    admin = None

    def to_manage(self, request):
        admin_name = request.POST['name']
        admin_pass = request.POST['password']
        self.admin = Admin.objects.filter(name=admin_name, password=admin_pass).first()
        if self.admin is None:
            return HttpResponse(render(request, 'admin_login.html'))
        request.session["admin_id"] = self.admin.adminID;
        request.session["admin_name"] = self.admin.name;
        return HttpResponse(render(request, 'manage.html'))

    @csrf_exempt
    def exit_system(self, request):
        del request.session["admin_name"]
        return HttpResponse("admin_login")

    @csrf_exempt
    def publish_notification(self, request):
        title = request.POST["title"]
        content = request.POST["content"]
        adminID = request.session["admin_id"]
        current_time = get_time.get_normal_time()
        notification = {
            'notiTime': current_time,
            'adminID_id': adminID,
            'title': title,
            'content': content
        }
        Notification.objects.create(**notification)
        return HttpResponse("success")

    @csrf_exempt
    def get_comment(self, request):
        all_comments = Comment.objects.all()
        data = []
        for comment in all_comments:
            answer = Answer.objects.filter(commentID=comment.commentID).first()
            username = User.objects.filter(userID=comment.userID_id).first().name
            temp_dict = {
                'id': comment.commentID,
                'username': username,
                'time': comment.time,
            }
            if answer is  None:
                temp_dict['state'] = "未处理"
            else:
                temp_dict['state'] = "已回复"
            data.append(temp_dict)
        result = json.dumps(data, ensure_ascii=False)
        return HttpResponse(result)

    def comment_detail(self, request):
        id = request.GET["id"]
        request.session['comment_id'] = id
        return HttpResponse(render(request, "comment_detail.html"))

    @csrf_exempt
    def get_comment_detail(self, request):
        comment = Comment.objects.filter(commentID=request.POST['id']).first().comment
        return HttpResponse(comment)

    @csrf_exempt
    def ans_comment(self, request):
        content = request.POST["content"]
        commentID = request.POST["id"]
        answer = {
            "text": content,
            "commentID_id": commentID
        }
        Answer.objects.create(**answer)
        return HttpResponse("回复成功")

    @csrf_exempt
    def get_parkinfo(self, request):
        all_parkinfo = ParkInfo.objects.all()
        data = []
        for parkinfo in all_parkinfo:
            data.append({"parkID":parkinfo.parkID_id,
                        "positionID": parkinfo.positionID_id,
                         "isBusy": parkinfo.isBusy,
                         "isBind": parkinfo.isBind,
                         })
        result = json.dumps(data, ensure_ascii=False)
        return HttpResponse(result)

    @csrf_exempt
    def add_position(self, request):
        number = None
        all_position = Position.objects.all().last()
        current_max_position = all_position.positionID
        if current_max_position.startswith('0'):
            temp = int(current_max_position[1])+1
            if temp != 10:
                number = '0'+ str(temp)
            else:
                number = ''+ str(temp)
        else:
            temp = int(current_max_position)+1
            number = '' + str(temp)
        Position.objects.create(positionID=number)
        parkinfo = {
            "positionID_id": number,
            "parkID_id": request.POST["group"]
        }
        ParkInfo.objects.create(**parkinfo)
        return HttpResponse("success")

    @csrf_exempt
    def del_position(self, request):
        ParkInfo.objects.filter(parkID_id=request.POST["parkID"], positionID_id=request.POST["positionID"]).delete()
        Position.objects.filter(positionID=request.POST["positionID"]).delete()
        return HttpResponse("车位删除成功")
