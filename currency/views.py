from django.shortcuts import render
from django.http import JsonResponse
from .scrape import *
# Create your views here.


def rate_exchange(request):
    if request.method == 'POST':
        return JsonResponse(
            exchange_rate(
                request.POST.get('date'),
                request.POST.get('currency')
            ),
            status=200
        )
    return JsonResponse({'error': '404'}, status=404)


def rate_exchange_comparison(request):
    if request.method == 'POST':
        return JsonResponse(
            exchange_rate_comparison(
                request.POST.get('date1'),
                request.POST.get('date2'),
                request.POST.get('currency')
            ),
            status=200
        )
    return JsonResponse({'error': '404'}, status=404)
