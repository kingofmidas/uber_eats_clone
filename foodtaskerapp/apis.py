from django.http import JsonResponse
from .models import Restaurant
from .serializers import RestaurantSerializer


def customer_get_restaurants(request):
    restaurants = RestaurantSerializer(
        Restaurant.objects.all().order_by('-id'),
        many = True,
        context = {'request': request}
    ).data

    return JsonResponse({'restaurants': restaurants})