from django.shortcuts import render

# Create your views here.
def whelcome(request):
    return render(request, 'welcome/welcome.html', {})