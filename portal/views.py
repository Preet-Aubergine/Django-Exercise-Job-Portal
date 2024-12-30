from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from companies.models import CompanyDetail
from django.contrib.auth.models import User,auth

def index(request):
    # Check if the user has entered company details
    has_company_details = False
    if request.user.is_authenticated:
        has_company_details = CompanyDetail.objects.filter(user=request.user).exists()

    return render(request, 'index.html', {'has_company_details': has_company_details})