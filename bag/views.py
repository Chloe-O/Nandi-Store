from django.shortcuts import render

# Renders shopping bag #


def view_bag(request):
    return render(request, 'bag/bag.html')
