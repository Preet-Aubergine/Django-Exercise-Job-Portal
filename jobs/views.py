"""
This module defines the views for the 'jobs' application.

Functions:
    post(request): Handles job posting.
    job_list(request): Displays a list of jobs.
    edit_job(request, job_id): Handles editing a job.
    delete_job(request, job_id): Handles deleting a job.

Dependencies:
    django.shortcuts.render: Renders a template.
    django.shortcuts.get_object_or_404: Retrieves an object or raises a 404 error if not found.
    django.shortcuts.redirect: Redirects to a different URL.
    django.contrib.messages: Provides a way to store messages in one request and retrieve them in a subsequent request.
    .models.JobPost: The model representing job postings.
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import JobPost

def post(request):
    """
    Handles job posting.

    If the request method is POST, validates the form data and saves the job posting.
    If the form data is invalid, displays an error message and redirects to the job posting page.
    If the request method is not POST, renders the job posting page.

    Args:
        request (HttpRequest): The request object used to generate this response.

    Returns:
        HttpResponse: The response object containing the rendered job posting page or a redirect.
    """
    if request.method == 'POST':

        name = request.POST.get('name')
        desc = request.POST.get('desc')
        location = request.POST.get('location')
        salary_from = request.POST.get('salaryfrom')
        salary_to = request.POST.get('salaryto')
        tags = request.POST.get('tags')
        #TODO: Add validation for salary_from and salary_to
        if not name or not desc or not location or not salary_from or not salary_to or not tags:
            messages.error(request, "All fields are required.")
            return redirect('jobs:post')

        try:
            job_post = JobPost(
                user=request.user,
                name=name,
                desc=desc,
                location=location,
                salary_from=salary_from,
                salary_to=salary_to,
                tags=tags
            )
            job_post.save()
            messages.success(request, "Job posted successfully!")
            return redirect('/')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('jobs:post')

    else:
        return render(request, 'post.html')
    
def job_list(request):

    jobs = JobPost.objects.all()

    if jobs.exists():
        return render(request, 'job_list.html', {'jobs': jobs})
    else:
        return render(request, 'job_list.html', {'message': 'No jobs available'})
    
def edit_job(request, job_id):

    job = get_object_or_404(JobPost, id=job_id)

    if job.user != request.user:
        messages.error(request, "You are not authorized to edit this job post.")
        return redirect('job_list')

    if request.method == 'POST':
        job.name = request.POST['name']
        job.desc = request.POST['desc']
        job.location = request.POST['location']
        job.salary_from = request.POST['salaryfrom']
        job.salary_to = request.POST['salaryto']
        job.tags = request.POST['tags']
        job.save()

        messages.success(request, "Job post updated successfully!")
        return redirect('job_list')

    return render(request, 'edit_job.html', {'job': job})

def delete_job(request, job_id):
    job = get_object_or_404(JobPost, id=job_id)

    if job.user != request.user:
        messages.error(request, "You are not authorized to delete this job post.")
        return redirect('job_list')

    job.delete()

    messages.success(request, "Job post deleted successfully!")
    return redirect('job_list')

