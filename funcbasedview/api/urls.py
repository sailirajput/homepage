# this is our url file
# i want to pull
from django.urls import path
from .import views

urlpatterns = [
    path('studentapi/',views.student_api),
    path('studentapi/<int:pk>/',views.student_api),
    
]
