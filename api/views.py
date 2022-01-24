from django.shortcuts import render
import requests
import json
from django.shortcuts import redirect, render
from api.check_appropriate import check_appropriate
from api.social import login_social, callback_social
from django.http import HttpResponse, JsonResponse
from .check_appropriate import check_appropriate


def check_validation(request):
    content_1 = request.POST.get('content_1')
    content_2 = request.POST.get('content_2')
    # content_2 = request.POST.get('content_3')
    # content_2 = request.POST.get('content_4')
    # content_2 = request.POST.get('content_5')
    # content_2 = request.POST.get('content_6')
    content_7 = request.POST.get('content_7')

    data = {
        'content_1' : check_appropriate(content_1),
        'content_2' : check_appropriate(content_2),
        # 'content_3' : check_appropriate(content_3),
        # 'content_4' : check_appropriate(content_4),
        # 'content_5' : check_appropriate(content_5),
        # 'content_6' : check_appropriate(content_6),
        'content_7' : check_appropriate(content_7),
    }

    return JsonResponse(data, json_dumps_params = {'ensure_ascii': True})