from django.http import JsonResponse
from .scrape import *
import json


def rate_exchange(request):
    print(request.body)
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        return JsonResponse(
            exchange_rate(
                data.get('date'),
                data.get('currency')
            ),
            status=200
        )
    return JsonResponse({'error': '404'}, status=404)


def rate_exchange_comparison(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        return JsonResponse(
            exchange_rate_comparison(
                data.get('date1'),
                data.get('date2'),
                data.get('currency')
            ),
            status=200
        )
    return JsonResponse({'error': '404'}, status=404)
