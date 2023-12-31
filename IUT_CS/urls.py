"""
URL configuration for IUTCS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path("admin/", admin.site.urls),
                  path('home/', views.home.as_view(), name='home_'),
                  path('mdeditor/', include('mdeditor.urls')),
                  path('blogs/', include('blogs.urls')),
                  path('achievements/', include('achievements.urls')),
                  path('activity/', include('activity.urls')),
                  path('executive_committee/', views.ExecutiveCommittee.as_view(), name='executive_committee'),
                  path('about/', views.about.as_view(), name='about'),
                  path('admin_panel/', include('admin_panel.urls')),
                  path('intra_events/', include('intra_university_event.urls')),
                  path('inter_events/', include('inter_university_event.urls')),
                  path('events/', views.events.as_view(), name='events'),
                  path('', views.home.as_view(), name='home'),
                  path('inter_events_and_participants/', views.inter_event_participants.as_view(), name='inter_events_and_participants'),
                  path('intra_events_and_participants/', views.intra_event_participants.as_view(), name='intra_events_and_participants'),
                  path('leaderboard/', views.leaderboard.as_view(), name='leaderboard'),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
