"""
This module defines the URL patterns for the 'jobs' application.

Functions:
    urlpatterns: A list of URL patterns to route URLs to the appropriate views.

Routes:
    post/ -> views.post: Handles job posting.
    list/ -> views.job_list: Displays a list of jobs.
    edit/<int:job_id>/ -> views.edit_job: Handles editing a job.
    delete/<int:job_id>/ -> views.delete_job: Handles deleting a job.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post, name='post'),
    path('list/', views.job_list, name='job_list'),
    path('edit/<int:job_id>/', views.edit_job, name='edit_job'),
    path('delete/<int:job_id>/', views.delete_job, name='delete_job'),
]