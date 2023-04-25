from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_donor/', views.add_donor, name='add_donor'),
    path('add_blood_bag/', views.add_blood_bag, name='add_blood_bag'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('register/', views.register, name='register'),
    path('dashboard', views.admin_dashboard_view,name='dashboard'),
]
