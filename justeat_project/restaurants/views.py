from django.shortcuts import render
from .forms import PostcodeForm
from .services import get_restaurants

def restaurant_list(request):
    restaurants = None

    if request.method == 'POST':
        form = PostcodeForm(request.POST)
        if form.is_valid():
            postcode = form.cleaned_data['postcode']
            restaurants = get_restaurants(postcode)
    else:
        form = PostcodeForm()

    return render(request, 'restaurants/restaurant_list.html', {
        'form': form,
        'restaurants': restaurants,
    })