from django.urls import path

from . import views

app_name = 'intra_event'

urlpatterns = [
    path('', views.index, name='intra_events'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create_intra_event/', views.createIntra_event, name='create_event'),
    path('edit_intra_event/<int:pk>', views.editIntra_event.as_view(), name='edit_event'),
    path('update_intra_event/<int:pk>', views.updateIntra_event, name='update_event'),
    path('google_form_intra_event/<int:pk>', views.google_formIntra_event, name='google_form'),
    path('delete_intra_event/<int:pk>', views.deleteIntra_event, name='delete_event'),
]

'''

'''
