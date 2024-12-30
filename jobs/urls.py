from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post, name='post'),
    path('list/', views.job_list, name='job_list'),
    path('edit/<int:job_id>/', views.edit_job, name='edit_job'),
    path('delete/<int:job_id>/', views.delete_job, name='delete_job'),
]