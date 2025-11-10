from django.urls import path
from . import views

app_name = 'stories'

urlpatterns = [
    path('', views.story_list, name='story_list'),
    path('<int:story_id>/', views.story_detail, name='story_detail'),
    path('live-article/', views.live_article_detail, name='live_article_detail'),
     path('debug-api/', views.debug_api, name='debug_api'), 
]