from django.shortcuts import render

# Create your views here.

def sam(request):

    """A view to return sams page"""
    return render(request, 'sam.html')
