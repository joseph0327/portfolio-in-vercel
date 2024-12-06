from django.shortcuts import render

# Create your views here.
def adminlogin(request):
    
    
    context = {
    }
    return render(request, 'admincenter/adminlogin.html',context)