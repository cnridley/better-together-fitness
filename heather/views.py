from django.shortcuts import render

# Create your views here.

def heather(request):

    """A view to return sams page"""
    return render(request, 'heather.html')