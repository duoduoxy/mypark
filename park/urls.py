from django.urls import path
from . import views
from .admin.admin_page import AdminPage
from .user.user_page import UserPage
urlpatterns =[

    path('admin_login', views.admin_login),
    path('adminLogin', AdminPage().to_manage),
    path('exit_system', AdminPage().exit_system),
    path('publish_notification', AdminPage().publish_notification),
    path('get_comment', AdminPage().get_comment),
    path('comment_detail', AdminPage().comment_detail),
    path('get_comment_detail', AdminPage().get_comment_detail),
    path('ans_comment', AdminPage().ans_comment),
    path('get_parkinfo', AdminPage().get_parkinfo),
    path('add_position', AdminPage().add_position),
    path('del_position', AdminPage().del_position),

    path('user_login', views.user_login),
    path('userLogin', UserPage().to_index),
    path('user_register', UserPage().go_register),
    path('register', UserPage().register),
    path('get_notification', UserPage().get_notification),
    path('to_info', UserPage().to_info),
    path('to_park', UserPage().to_park),
    path('to_charge', UserPage().to_charge),
    path('to_comment', UserPage().to_comment),
    path('get_balance', UserPage().get_balance),
    path('get_position', UserPage().get_position),
    path('submit_comment', UserPage().submit_comment),
    path('pic_upload', UserPage().pic_upload),
    path('confirm_park', UserPage().confirm_park),
    path('finish', UserPage().finish),
    path('once_park', UserPage().once_park),
    path('get_user_parkinfo', UserPage().get_user_parkinfo),
]

