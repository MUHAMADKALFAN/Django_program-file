from django.urls import path
from myapp import views
urlpatterns = [

    path('',views.home,name='home'),
    path('sigup1/',views.signup1,name='sigup1'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),


]
