"""RailwayDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from railway import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',nav,name="nav"),
    path('about/',views.About,name="about"),
    path('login/',views.Login_customer,name="login_customer"),
    path('register_customer/',views.Register_customer,name="register_customer"),
    path('contact/',views.contact,name="contact"),
    path('search_train/',views.Search_Train,name="search_train"),
    path('book_detail/(?P<coun>[0-9]+)/(?P<pid>[0-9]+)/(<str:route1>)',views.Book_detail,name="book_detail"),
    path('delete_passenger/(?P<pid>[0-9]+)/(?P<bid>[0-9]+)/(<str:route1>)',views.Delete_passenger,name="delete_passenger"),
    path('dashboard/',views.Dashboard,name="dashboard"),
    path('card_detail/(?P<total>[0-9]+)/(?P<coun>[0-9]+)/(<str:route1>)/(?P<pid>[0-9]+)',views.Card_Detail,name="card_detail"),
    path('log_out/',views.Logout,name="log_out"),
    path('my_booking/',views.my_booking,name="my_booking"),
    path('delte_my_booking/(?P<pid>[0-9]+)',views.delte_my_booking,name="delte_my_booking"),
    path('dashboard2/', views.admindashboard, name="admindashboard"),
    path('addtrain/', views.Add_train, name="add_train"),
    path('addroute/', views.add_route, name="add_route"),
    path('edittrain/?P<pid>[0-9]+)', views.edit, name="edittrain"),
    path('editroute/?P<pid>[0-9]+)', views.Edit_route, name="editroute"),
    path('delete/?P<pid>[0-9]+)', views.delete, name="delete"),
    path('delete_route/?P<pid>[0-9]+)', views.delete_route, name="delete_route"),
    path('viewtrain/', views.view_train, name="view_train"),
    path('availableroute/', views.displayroute, name="availableroute"),
    path('viewbookings/', views.viewbookings, name="viewbookings"),
    path('deletebooking/(?P<pid>[0-9]+)',views.deletebooking,name="deletebooking"),
    path('view_ticket/(?P<pid>[0-9]+)',views.view_ticket, name="view_ticket"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
