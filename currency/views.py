from django.shortcuts import render
from django.http import JsonResponse
from .scrape import exchange_rate
# Create your views here.


def rate_exchange(request):
    if request.method == 'POST':
        return JsonResponse(exchange_rate('03-04-2021', 'EU'), status=200)
    return JsonResponse({'error': '404'}, status=404)