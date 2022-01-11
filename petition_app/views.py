from django.shortcuts import render
import requests
import json


def test(request):
    data = json.dumps({"text":"동해물과 백두산이 마르고 닳도록"})
    result = json.loads(requests.post("http://143.248.41.54:8000/predict", data=data).text)


def index(request):
    context={
        'body_class':'splash',
        'bottom_nav':True
    }
    return render(request, "index.html", context=context)


def main(request):
    context={
        'body_class':'background_white',
        'active':{'main':"active"},
        'bottom_nav':True
    }
    return render(request, "main.html", context=context)


def check(request):
    context={
        'body_class':'background_white2',
        'bottom_nav':False
    }
    return render(request, "check.html", context=context)


def check_highlight(request):
    context={
        'body_class':'background-white2 check-page',
        'bottom_nav':False
    }
    return render(request, "check_highlight.html", context=context)


def check_keyboard(request):
    context={
        'body_class':'background-white2 check-page',
        'bottom_nav':False
    }
    return render(request, "check_keyboard.html", context=context)
    

def good(request):
    context={
        'body_class':'check-page',
        'bottom_nav':False
    }
    return render(request, "good.html", context=context)


def list(request):
    context={
        'body_class':'background-white2',
        'active':{'list':"active"},
        'bottom_nav':True
    }
    return render(request, "list.html", context=context)


def title_finish(request):
    context={
        'body_class':'background-white2',
        'active':{'list':"active"},
        'bottom_nav':True
    }
    return render(request, "title_finish.html", context=context)