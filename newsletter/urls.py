# newsletter/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('manual/', views.signup_manual, name='signup_manual'),
    path('modelform/', views.signup_modelform, name='signup_modelform'),
]
