from django.urls import path

from . import views

app_name = 'inter_event'

urlpatterns = [
    path('', views.index, name='inter_events'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create_inter_event/', views.createInter_event, name='create_event'),
    path('edit_inter_event/<int:pk>', views.editInter_event.as_view(), name='edit_event'),
    path('update_inter_event/<int:pk>', views.updateInter_event, name='update_event'),
    path('delete_inter_event/<int:pk>', views.deleteInter_event, name='delete_event'),
    path('team_registration/<int:pk>', views.team_registration, name='team_registration'),
    
]

'''

'''
