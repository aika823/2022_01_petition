from petition_app.models import Category, Department, Petition, PetitionCategory, PetitionImage, User


def create_petition(request):
    
    user = User.objects.get(id=request.session.get('user'))
    petition = Petition()

    petition.user = user

    petition.title = request.POST.get('title')
    department = Department.objects.get(id=request.POST.get('department'))
    petition.department = department
    petition.thumbnail = request.FILES.get('thumbnail')

    petition.content = request.POST.get('content')
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
        petition_image = PetitionImage()
        petition_image.petition = petition
        petition_image.image = image
        petition_image.save()

    categories = request.POST.getlist('category[]')
    for category in categories:
        petition_category = PetitionCategory()
        category =  Category.objects.get(id=category)
        petition_category.petition = petition
        petition_category.category = category
        petition_category.save()

    return petition