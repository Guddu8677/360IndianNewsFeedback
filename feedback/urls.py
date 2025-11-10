# from django.urls import path
# from . import views

# app_name = 'feedback'

# urlpatterns = [
#     path('form/<int:story_id>/', views.feedback_form, name='feedback_form'),
#     path('submit/<int:story_id>/', views.submit_feedback, name='submit_feedback'),
# ]






from django.urls import path
from . import views

app_name = 'feedback'

urlpatterns = [
    path('submit/<int:story_id>/', views.feedback_form, name='feedback_form'),
    path('form/<int:story_id>/', views.feedback_form, name='submit_feedback'),
]