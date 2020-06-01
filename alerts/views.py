from django.shortcuts import render

# Create your views here.
def email_alert(request):
    return render(request, 'alerts/email_alert.html')
