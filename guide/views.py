from django.shortcuts import render
from guide.models import Gallery

# Create your views here.

def guide(request):

    """A view to return guides page"""
    gallery = Gallery.objects.all()

    context = {
        'gallery': gallery,
    }
    
    return render(request, 'guide.html', context)