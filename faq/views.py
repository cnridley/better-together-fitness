from django.shortcuts import render
from faq.models import questions
# Create your views here.

def faq(request):

    """A view to return faq page"""
    Qu = questions.objects.all()

    context = {
        'Qu': Qu,
    }

    return render(request, 'faq.html', context)
