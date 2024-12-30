from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CompanyDetail

@login_required
def details(request):
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