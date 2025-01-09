"""
This module defines the views for the 'portal' application.

Functions:
    index(request): Displays the index page of the portal.

Dependencies:
    django.shortcuts.render: Renders a template.
    django.shortcuts.redirect: Redirects to a different URL.
    django.contrib.auth.decorators.login_required: Ensures the user is logged in to access the view.
    companies.models.CompanyDetail: The model representing company details.
    django.contrib.auth.models.User: Represents a user in the authentication system.
    django.contrib.auth.models.auth: Provides authentication-related functions.
"""
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from companies.models import CompanyDetail
from django.contrib.auth.models import User,auth

def index(request):
    """
    Displays the index page of the portal.

    Checks if the authenticated user has entered company details and passes this information to the template.

    Args:
        request (HttpRequest): The request object used to generate this response.

    Returns:
        HttpResponse: The response object containing the rendered index page.
    """
    has_company_details = False
    if request.user.is_authenticated:
        has_company_details = CompanyDetail.objects.filter(user=request.user).exists()

    return render(request, 'index.html', {'has_company_details': has_company_details})