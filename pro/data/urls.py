from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('register',views.registerpage, name='register'),
    path('loginpage',views.loginpage, name='loginpage'),
    path('logout',views.logoutpage, name='logout'),
    path('',views.base,name='base'),
     path('details',views.viewpage,name='details'),
     path('bio_data', views.bio_data, name='bio_data'),
    path('edit_bio_data', views.edit_bio_data, name='edit_bio_data'),
    path('userdetails',views.userdetails,name='userdetails'),
    path('showuser',views.showuser,name="showuser"),
    path('delete/<int:id>',views.delete_user,name="delete"),
     path('edit/<int:id>',views.update_user,name="edit"),

]
