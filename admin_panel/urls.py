from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

#app_name = 'admin_panel'

urlpatterns = [
    # Login and Logout
    path('', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='admin_panel/login.html'), name='login'),
    path('all/',views.AdminPanel,name='admin_panel'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

]
