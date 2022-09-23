from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='homepage'),
    path('signup/', views.signup , name='signup'),
    path('login/', views.loginview , name='login'),
    path('send_friend_request/<int:userID>/', 
            views.send_friend_request , name='send_friend_request'),
    path('accept_friend_request/<int:requestID>/', 
            views.accept_friend_request, name='accept_friend_request'),

]