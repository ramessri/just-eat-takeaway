from django.shortcuts import render
from .forms import PostcodeForm
from .services import get_restaurants

QUICK_POSTCODES = [
    {'code': 'EC4M7RF', 'label': 'EC4M 7RF · City'},
    {'code': 'W1D3QU',  'label': 'W1D 3QU · Soho'},
    {'code': 'E16RF',   'label': 'E1 6RF · Whitechapel'},
    {'code': 'N19BE',   'label': 'N1 9BE · Islington'},
    {'code': 'SW1A1AA', 'label': 'SW1A 1AA · Westminster'},
    {'code': 'SE17PB',  'label': 'SE1 7PB · Southwark'},
    {'code': 'WC2N5DU', 'label': 'WC2N 5DU · Covent Gdn'},
    {'code': 'E145AB',  'label': 'E14 5AB · Canary Wharf'},
    {'code': 'NW16XE',  'label': 'NW1 6XE · Camden'},
    {'code': 'SW72AS',  'label': 'SW7 2AS · South Ken'},
]

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
        'quick_postcodes': QUICK_POSTCODES,
    })