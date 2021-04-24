from django.shortcuts import render
# Create your views here.

def bag(request):

    """A view to return bag page"""

    return render(request, 'bag.html')