from django.shortcuts import render, redirect, reverse
from products.models import Product
from django.contrib import messages


# Renders shopping bag #


def view_bag(request):
    return render(request, 'bag/bag.html')


# Add specified quantity of product to bag #


def add_to_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, "Successfully added to your bag")

    request.session['bag'] = bag
    return redirect(redirect_url)


# Add or remove specified quantity of product to bag #


def adjust_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity in range(0, 10):
        bag[item_id] = quantity
        messages.success(request, "Successfully added to your bag")
    else:
        bag.pop(item_id)
        messages.success(request, "Successfully removed from you bag")

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
