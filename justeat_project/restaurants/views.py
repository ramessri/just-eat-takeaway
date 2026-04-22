from django.http import JsonResponse
from .services import get_restaurants

def restaurant_list(request):
    restaurants = get_restaurants('SW1A1AA')
    return JsonResponse(restaurants, safe=False)