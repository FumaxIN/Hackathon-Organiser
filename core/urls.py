from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

urlpatterns = [
    path('hackathons/', views.HackathonList.as_view(), name='feed'),
    path('hackathons/<int:hackathonID>/enrol/', views.Details_Enrol.as_view(), name='enrollments'),
    path('enrollments/', views.my_enrollments, name='my-enrollments'),
    path('hackathons/<int:hackathonID>/submission/', views.UserSubmission.as_view(), name='submit'),
    path('submissions/', views.my_submissions, name='submissions'),
]