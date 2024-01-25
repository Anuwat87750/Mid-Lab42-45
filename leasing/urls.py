from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('login',views.custom_login),#เรียกใช้ def ชื่อ custom_login
    path('add_drug',views.add_drug),
    path('add_type',views.add_type),
    path('manage_drug',views.manage_drug),
    path('manage_type',views.manage_type),
    path('delete/<int:pk>',views.delete_drug),
    path('delete_type/<int:pk>/', views.delete_type, name='delete_type'),
    path('edit/<int:pk>',views.edit_drug),#หน้าแก้ไขข้อมูลยา
    path('editt/<int:pk>',views.edit_type),#หน้าแก้ไขข้อมูลประเภทยา
    path('increase_qty/<int:pk>',views.increase_drug),#หน้าเพิ่มจำนวนยา
    path('decrease_qty/<int:pk>',views.decrease_drug),#หน้าลดจำนวนยา
    path('logout/',views.logout_view),
    path('buy_drug/', views.buy_drug_view, name='buy_drug'),
    path('buy_drugu/', views.buy_drug,),
    path('register/', views.register_view, name='register'),
    path('report', views.report_a,),
    
]