"""Flat_Rent_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Flatapp.views import *

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name="index"),
    path('contact/',contact, name="contact"),
    path('about/',about, name="about"),
    path('user_login/', user_login, name="user_login"),
    path('admin_login/', admin_login, name="admin_login"),
    path('user_register/', user_register, name="user_register"),
    path('owner_register/', owner_register, name="owner_register"),
    path('logout_user/', logout_user, name="logout_user"),
    path('user_table/', user_table, name="user_table"),
    path('owner_table/', owner_table, name="owner_table"),
    path('add_Apartment/', add_Apartment, name="add_Apartment"),
    path('apartment_table/', apartment_table, name="apartment_table"),
    path('user_profile/', user_profile, name="user_profile"),
    path('owner_profile/', owner_profile, name="owner_profile"),
    path('user-change/', user_change, name="user_change"),
    path('admin_change_password/', admin_change_password, name="admin_change_password"),
    path('send-feedback/', send_feedback, name="send_feedback"),
    path('owner_apartment_detail/<int:aid>/', owner_apartment_detail, name="owner_apartment_detail"),
    path('user_apartment_detail/<int:aid>/', user_apartment_detail, name="user_apartment_detail"),
    path('change_apartment_status/<int:pid>/', change_apartment_status, name="change_apartment_status"),
    path('change_payment_status/<int:pid>/', change_payment_status, name="change_payment_status"),
    path('user_booking_apartment/', user_booking_apartment, name="user_booking_apartment"),
    path('user_booking_list/', user_booking_list, name="user_booking_list"),
    path('user_payment/', user_payment, name="user_payment"),
    path('owner_detail/<int:pid>/', owner_detail, name="owner_detail"),
    path('user_detail/<int:pid>/', user_detail, name="user_detail"),
    path('change_owner_status/<int:pid>/', change_owner_status, name="change_owner_status"),
    path('change_user_status/<int:pid>/', change_user_status, name="change_user_status"),
    path('apartment_delete/<int:pid>/', apartment_delete, name="apartment_delete"),
    path('delete_feed/<int:pid>/', delete_feed, name="delete_feed"),
    path('feedback/', feedback, name="feedback"),
    path('apartment_search/', apartment_search, name="apartment_search"),
    path('forgot_password/', forgot_password, name="forgot_password"),
path('apartment_admtable/', apartment_admtable, name="apartment_admtable"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
