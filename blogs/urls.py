from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='blogs'),
    path('<int:pk>/', views.detail, name='detail'),
]
