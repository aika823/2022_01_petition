from django.shortcuts import render
import requests
import json
from django.shortcuts import redirect, render
from api.check_appropriate import check_appropriate
from api.social import login_social, callback_social


def test(request):
    text = "동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세"
    # result = check_appropriate(text)

    social = "kakao"
    return redirect(login_social(social))
    # print(social_login_result)

    # return render(request, "test.html", {'result':social})


def callback(request, type):
    print(request.GET)
    code = request.GET.get('code')

    user_info = callback_social(request, type)
    print(user_info)
    
    return render(request, "test.html", {'result':user_info})

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
        'body_class':'background-white2 check-page',
        'active':{'list':"active"},
        'bottom_nav':False
    }
    return render(request, "title_finish.html", context=context)


def write(request):
    context={
        'body_class':'background-white2 check-page',
        'active':{'list':"active"},
        'bottom_nav':False
    }
    return render(request, "write.html", context=context)
    
def write_template(request):
    context={
        'body_class':'height-auto',
        'active':{'list':"active"},
        'bottom_nav':False
    }
    return render(request, "write_template.html", context=context)

def write_template_click(request):
    context={
        'body_class':'height-auto',
        'active':{'list':"active"},
        'bottom_nav':False
    }
    return render(request, "write_template_click.html", context=context)