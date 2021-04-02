from django.shortcuts import render
from guide.models import Gallery
from guide.models import nutitionGuides
# Create your views here.

def guide(request):

    """A view to return guides page"""
    gallery = Gallery.objects.all()
    guides = nutitionGuides.objects.all()

    context = {
        'gallery': gallery,
        'guides': guides,
    }
    
    return render(request, 'guide.html', context)