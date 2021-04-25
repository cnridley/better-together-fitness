from django.shortcuts import render, redirect
# Create your views here.

def bag(request):

    """A view to return bag page"""

    return render(request, 'bag.html')


def add_guides_to_bag(request, item_id):
    """Add a guide to the shopping bag"""
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url) 