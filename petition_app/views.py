from unicodedata import category
from django.shortcuts import render
import requests
import json
from django.shortcuts import redirect, render
from api.check_appropriate import check_appropriate
from api.social import login_social, callback_social
from api.petition import create_petition
from .models import Category, Department, Petition, PetitionCategory, PetitionPrediction, User, PetitionImage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
            'bottom_nav':False
        }
        return render(request, "index.html", context=context)


def main(request):
    user = User.objects.get(id=request.session.get('user'))
    petition_list = Petition.objects.all().order_by('-agreements')[:5]
    for petition in petition_list:
        petition.category_list = Category.objects.filter(petitioncategory__petition=petition)
        petition.percentage = min(100,round(100*(petition.agreements/200000), 2))
    
    context={
        'body_class':'background_white',
        'active':{'main':"active"},
        'bottom_nav':True,
        'user':user,
        'petition_list':petition_list
    }
    return render(request, "main.html", context=context)


def check(request):
    context={
        'body_class':'background-white2 choose-page',
        'bottom_nav':False
    }
    return render(request, "check.html", context=context)


def check_highlight(request):
    context={
        'body_class':'background-white2 check-page height-100',
        'bottom_nav':False
    }
    return render(request, "check_highlight.html", context=context)


def check_keyboard(request):
    context={
        'body_class':'background-white2 check-page height-100',
        'bottom_nav':False
    }
    return render(request, "check_keyboard.html", context=context)
    

def good(request):
    context={
        'body_class':'check-page good-page',
        'bottom_nav':False
    }
    return render(request, "good.html", context=context)


def list(request):
    active_category = request.GET.get('category')
    category_list = Category.objects.all()
    active_all = "active"
    for category in category_list:
        if active_category and (category.id == int(active_category)):
            category.active = "active"
            active_all = None
    if active_category:
        petition_list = Petition.objects.filter(petitioncategory__category = active_category).order_by('-agreements')
    else:
        petition_list = Petition.objects.all().order_by('-agreements')
    
    print(petition_list)
        
    for petition in petition_list:
        petition.percentage = min(100,round(100*(petition.agreements/200000), 2))

    # infinite scroll
    max = petition_list.count()
    numbers_list = range(0, max)
    page = request.GET.get("page", 1)
    paginator = Paginator(numbers_list, 10)

    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    
    print(numbers)

    context={
        'body_class':'background-white2 listpage',
        'bottom_nav':True,
        'category_list':category_list,
        'petition_list':petition_list,
        'active_all':active_all,
        'numbers':numbers
    }
    return render(request, "list.html", context=context)


def write_title(request):
    context={
        'body_class':'background-white2 check-page titlepage',
        'active':{'list':"active"},
        'bottom_nav':False
    }
    return render(request, "write_title.html", context=context)


def write_category(request):
    category_list = Category.objects.all()
    context={
        'body_class':'background-white2 check-page category height-100',
        'active':{'list':"active"},
        'bottom_nav':False,
        'title':request.GET.get('title'),
        'category_list':category_list,
    }
    return render(request, "write_category.html", context=context)


def write_receiver(request):
    department_list = Department.objects.all()
    context={
        'body_class':'background-white2 check-page height-100',
        'active':{'list':"active"},
        'bottom_nav':False,
        'title':request.GET.get('title'),
        'category_list':request.GET.getlist('category[]'),
        'department_list':department_list,
    }
    return render(request, "write_receiver.html", context=context)


def write(request):
    context={
        'body_class':'check-page write',
        'active':{'list':"active"},
        'bottom_nav':False,
        'title':request.GET.get('title'),
        'category_list':request.GET.getlist('category[]'),
        'department':request.GET.get('department')
    }
    return render(request, "write.html", context=context)


def write_template_qna(request):
    category_list = [Category.objects.get(id=id) for id in request.GET.getlist('category[]')]
    department = Department.objects.get(id=request.GET.get('department'))
    
    context={
        'body_class':'height-auto',
        'active':{'list':"active"},
        'bottom_nav':False,
        'title':request.GET.get('title'),
        'category_list':category_list,
        'department':department
    }
    return render(request, "write_template_qna.html", context=context)


def write_template_click(request):
    category_list = [Category.objects.get(id=id) for id in request.GET.getlist('category[]')]
    department = Department.objects.get(id=request.GET.get('department'))

    context={
        'body_class':'height-auto',
        'active':{'list':"active"},
        'bottom_nav':False,
        'title':request.GET.get('title'),
        'category_list':category_list,
        'department':department
    }
    return render(request, "write_template_click.html", context=context)


def inspection(request):
    if request.method == "POST":
        petition = create_petition(request)
        # category_list = PetitionCategory.objects.filter(petition=petition)
        category_list = Category.objects.filter(petitioncategory__petition = petition)
        image_list = PetitionImage.objects.filter(petition=petition)

        if request.POST.get('content'):
            status = {
                'content': check_appropriate(petition.content)['prediction']
            }
        else:
            status = {
                'content_1': check_appropriate(petition.content_1)['prediction'],
                'content_2': check_appropriate(petition.content_2)['prediction'],
                # 'content_3': check_appropriate(petition.content_3)['prediction'],
                # 'content_4': check_appropriate(petition.content_4)['prediction'],
                # 'content_5': check_appropriate(petition.content_5)['prediction'],
                # 'content_6': check_appropriate(petition.content_6)['prediction'],
                'content_7': check_appropriate(petition.content_7)['prediction'],
            }

        # 적절성 여부 데이터 입력
        prediction = False
        for key in status:
            if status[key] == "부적절":
                prediction = True
                break

        petition_prediction = PetitionPrediction()
        petition_prediction.ai = True
        petition_prediction.petition = petition
        petition_prediction.prediction = prediction
        petition_prediction.save()

        
        has_keyword = True if petition.keyword_1 or petition.keyword_2 or petition.keyword_3 else False
        print(image_list.count())
        

        context={
            'petition':petition,
            'category_list':category_list,
            'image_list':image_list,
            'status':status,
            'body_class':'height-auto',
            'active':{'list':"active"},
            'bottom_nav':False,
            'has_keyword':has_keyword
        }
        return render(request, "inspection.html", context=context)


def detail(request, id):
    try:
        user= User.objects.get(id=request.session.get('user'))
        petition = Petition.objects.get(id=id)
        petition.percentage = min(100,round(100*(petition.agreements/200000), 2))
    except:
        user = None
        petition = None
    category_list = PetitionCategory.objects.filter(petition=petition)
    image_list = PetitionImage.objects.filter(petition=petition)
    context={
        'user':user,
        'petition':petition,
        'body_class':'height-auto',
        'active':{'list':"active"},
        'bottom_nav':False,
        'category_list':category_list,
        'image_list':image_list,
    }
    return render(request, "detail.html", context=context)