from django.urls import path

from . import views

app_name = 'achievements'

urlpatterns = [
    path('', views.index, name='achievements'),
    path('create_achievement/', views.createAchievement, name='create_achievement'),
    path('edit_achievement/<int:pk>', views.editAchievement.as_view(), name='edit_Achievement'),
    path('update_achievement/<int:pk>', views.updateAchievement, name='update_Achievement'),
    path('delete_achievement/<int:pk>', views.deleteAchievement, name='delete_Achievement'),
]
