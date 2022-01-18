from django.shortcuts import render
import requests
import json
from django.shortcuts import redirect, render
from api.check_appropriate import check_appropriate
from api.social import login_social, callback_social
from .models import Petition, User


def test(request):
    text = "동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세"
    # result = check_appropriate(text)

    social = "kakao"
    return redirect(login_social(social))

    # return render(request, "test.html", {'result':social})


def callback(request, type):
    code = request.GET.get('code')

    user_info = callback_social(request, type)
    
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
    petition_list = Petition.objects.all()
    for petition in petition_list:
        petition.percentage = (petition.agreements/200000) * 100
    context={
        'body_class':'background-white2',
        'active':{'list':"active"},
        'bottom_nav':True,
        'petition_list':petition_list
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
    if request.method=="POST":
        title = request.POST.get('title')
        category = request.POST.get('category')
        department = request.POST.get('department')
        return redirect('/write_template?title={}&category={}&department={}'.format(title, category, department))
    else:
        return render(request, "write.html", context=context)

    
    
    
def write_template(request):
    title = request.GET.get('title')
    category = request.GET.get('category')
    department = request.GET.get('department')
    context={
        'body_class':'height-auto',
        'active':{'list':"active"},
        'bottom_nav':False,
        'title': title,
        'category': category,
        'department':department
    }
    
    if request.method == "POST":
        user_id = 1
        user = User.objects.get(id=user_id)

        petition = Petition()

        petition.user = user

        petition.title = request.POST.get('title')
        petition.category = request.POST.get('category')
        petition.department = request.POST.get('department')
        petition.thumbnail = request.FILES.get('thumbnail')

        petition.content_1 = request.POST.get('content_1')
        petition.content_2 = request.POST.get('content_2')
        petition.content_3 = request.POST.get('content_3')
        petition.content_4 = request.POST.get('content_4')
        petition.content_5 = request.POST.get('content_5')
        petition.content_6 = request.POST.get('content_6')
        petition.content_7 = request.POST.get('content_7')

        petition.keyword_1 = request.POST.get('keyword_1')
        petition.keyword_2 = request.POST.get('keyword_2')
        petition.keyword_3 = request.POST.get('keyword_3')

        petition.save()


    return render(request, "write_template.html", context=context)


def success(request):
    if request.method == "POST":
        user_id = 1
        user = User.objects.get(id=user_id)

        petition = Petition()

        petition.user = user

        petition.title = request.POST.get('title')
        petition.category = request.POST.get('category')
        petition.department = request.POST.get('department')
        petition.thumbnail = request.FILES.get('thumbnail')

        petition.content_1 = request.POST.get('content_1')
        petition.content_2 = request.POST.get('content_2')
        petition.content_3 = request.POST.get('content_3')
        petition.content_4 = request.POST.get('content_4')
        petition.content_5 = request.POST.get('content_5')
        petition.content_6 = request.POST.get('content_6')
        petition.content_7 = request.POST.get('content_7')

        petition.keyword_1 = request.POST.get('keyword_1')
        petition.keyword_2 = request.POST.get('keyword_2')
        petition.keyword_3 = request.POST.get('keyword_3')

        petition.save()
        
        
        context = {
            'petition': petition
        }
        
        return render(request, "success.html", context=context)



    


def write_template_click(request):
    context={
        'body_class':'height-auto',
        'active':{'list':"active"},
        'bottom_nav':False
    }
    return render(request, "write_template_click.html", context=context)


def inspection(request):
    context={
        'body_class':'height-auto',
        'active':{'list':"active"},
        'bottom_nav':False
    }
    return render(request, "inspection.html", context=context)


def detail(request):
    context={
        'body_class':'height-auto',
        'active':{'list':"active"},
        'bottom_nav':False
    }
    return render(request, "detail.html", context=context)
