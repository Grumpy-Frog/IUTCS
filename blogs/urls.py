from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='blogs'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create_blog/', views.createBlog, name='create_blog'),
    path('edit_blog/<int:pk>', views.editBlog.as_view(), name='edit_blog'),
    path('update_blog/<int:pk>', views.updateBlog, name='update_blog'),
    path('delete_blog/<int:pk>', views.deleteBlog, name='delete_blog'),
]
