from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test, name='test'),
    # path('<str:room>/', views.room, name='room'),
    # path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/', views.getMessages, name='getMessages'),
    path('login/',views.loginPage,name='login'),
]