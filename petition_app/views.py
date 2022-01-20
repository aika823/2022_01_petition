from django.shortcuts import render
import requests
import json
from django.shortcuts import redirect, render
from api.check_appropriate import check_appropriate
from api.social import login_social, callback_social
from .models import Petition, User, PetitionImage


def login(request, type):
    return redirect(login_social(type))


def callback(request, type):
    user_info = callback_social(request, type)

    if user_info:
        try:
            user = User.objects.get(social_id = user_info['social_id'])
            request.session['user'] = user.id
            return redirect('/main')
        except:
            user = User()
            user.social_login = type
            user.name = user_info['username']
            user.email = user_info['email']
            user.social_id = user_info['social_id']
            user.save()
            request.session['user'] = user.id
            return redirect('/main')


def index(request):
    try:
        user = User.objects.get(id=request.session.get('user'))
        if user:
            return redirect('/main')
    except:
        context={
            'body_class':'splash',
            'bottom_nav':True
        }
        return render(request, "index.html", context=context)


def main(request):
    user = User.objects.get(id=request.session.get('user'))
    context={
        'body_class':'background_white',
        'active':{'main':"active"},
        'bottom_nav':True,
        'user':user
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


def choose_category(request):
    context={
        'body_class':'background-white2 check-page category',
        'active':{'list':"active"},
        'bottom_nav':False
    }
    return render(request, "choose_category.html", context=context)


def choose_receiver(request):
    context={
        'body_class':'background-white2 check-page',
        'active':{'list':"active"},
        'bottom_nav':False
    }
    return render(request, "choose_receiver.html", context=context)


def write(request):
    context={
        'body_class':'background-white2 check-page write',
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
        
        user = User.objects.get(id=request.session.get('user'))

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

        images = request.FILES.getlist('images')
        for image in images:
            print(image)
            petition_image = PetitionImage()
            petition_image.petition = petition
            petition_image.image = image

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


def detail(request, id):
    try:
        petition = Petition.objects.get(id=id)
    except:
        petition = None
        
    context={
        'petition':petition,
        'body_class':'height-auto',
        'active':{'list':"active"},
        'bottom_nav':False
    }
    return render(request, "detail.html", context=context)