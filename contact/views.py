from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact(request):
    if request.method == 'POST':
        # Capture the form data
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number', '')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to the database
        Contact.objects.create(
            full_name=full_name,
            email=email,
            mobile_number=mobile_number,
            subject=subject,
            message=message,
        )
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('home')     

    return render(request, 'home.html')
