from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('feedback/', views.feedback_form, name='feedback_form'),
    path('confirmation/', views.feedback_confirmation, name='feedback_confirmation'),
] 