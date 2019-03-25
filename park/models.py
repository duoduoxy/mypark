from django.db import models

class Admin(models.Model):
    adminID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class User(models.Model):
    userID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    isOwner = models.CharField(max_length=1, default=0)
    payMonth = models.IntegerField(default=-1)
    payState = models.IntegerField(default=0)
    oncePark = models.IntegerField(default=0)

class Comment(models.Model):
    commentID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User, to_field='userID', on_delete=models.CASCADE)
    time = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    hygiene = models.IntegerField(default=0)
    service = models.IntegerField(default=0)
    platform = models.IntegerField(default=0)

class Notification(models.Model):
    notiID = models.AutoField(primary_key=True)
    notiTime = models.CharField(max_length=50)
    adminID = models.ForeignKey(Admin, to_field='adminID', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=200)


class Park(models.Model):
    parkID = models.CharField(primary_key=True, max_length=1)

class Position(models.Model):
    positionID = models.CharField(primary_key=True, max_length=2)

class ParkInfo(models.Model):
    infoID = models.AutoField(primary_key=True)
    parkID = models.ForeignKey(Park, to_field='parkID', on_delete=models.CASCADE)
    positionID = models.ForeignKey(Position, to_field='positionID', on_delete=models.CASCADE)
    userID = models.IntegerField(default=-1)
    isBusy = models.CharField(max_length=3, default="no")
    carID = models.CharField(max_length=20, default="")
    isBind = models.CharField(max_length=3, default="no")
    minute = models.IntegerField(default=0)

class Answer(models.Model):
    answerID = models.AutoField(primary_key=True)
    commentID = models.ForeignKey(Comment, to_field="commentID" , on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

class Balance(models.Model):
    userID = models.ForeignKey(User, to_field="userID", on_delete=models.CASCADE)
    balance = models.CharField(max_length=10)

class PositionBind(models.Model):
    userID = models.ForeignKey(User, to_field="userID", on_delete=models.CASCADE)
    infoID = models.ForeignKey(ParkInfo, to_field="infoID", on_delete=models.CASCADE)

