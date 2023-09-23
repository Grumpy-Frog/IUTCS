from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [

]

'''
path('', views.index, name='events'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create_event/', views.createEvent, name='create_event'),
    path('edit_event/<int:pk>', views.editEvent.as_view(), name='edit_event'),
    path('update_event/<int:pk>', views.updateEvent, name='update_event'),
    path('delete_event/<int:pk>', views.deleteEvent, name='delete_event'),
'''