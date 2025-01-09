"""
This module defines the views for the 'companies' application.

Functions:
    details(request): Handles the display and submission of company details.

Dependencies:
    django.shortcuts.render: Renders a template.
    django.shortcuts.redirect: Redirects to a different URL.
    django.contrib.auth.decorators.login_required: Ensures the user is logged in to access the view.
    django.contrib.messages: Provides a way to store messages in one request and retrieve them in a subsequent request.
    .models.CompanyDetail: The model representing company details.
"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CompanyDetail

@login_required
def details(request):
    """
    Handles the display and submission of company details.

    If the user has already entered company details, displays an error message and redirects to the home page.
    If the request method is POST, validates the form data and saves the company details.
    If the form data is invalid, displays an error message and renders the details page again.
    If the request method is not POST, renders the details page.

    Args:
        request (HttpRequest): The request object used to generate this response.

    Returns:
        HttpResponse: The response object containing the rendered details page or a redirect.
    """
    user_company = CompanyDetail.objects.filter(user=request.user).first()
    
    if user_company:
        messages.error(request, "You have already entered company details. You cannot add another company.")
        return redirect('/')

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact = request.POST.get('contact')

        if not name or not address or not contact:
            messages.error(request, "All fields are required.")
            return render(request, 'details.html')
        
        try:
            CompanyDetail.objects.create(
                user=request.user,
                name=name,
                address=address,
                contact=contact,
            )
            messages.success(request, "Company details saved successfully!")
            return redirect('/')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'details.html')

    return render(request, 'details.html')