from django.db import models
from django.db.models.deletion import CASCADE


class User(models.Model):
    email = models.EmailField(max_length=300, db_column="email")
    name = models.CharField(max_length=20, db_column="name", null=False, default="")
    password = models.CharField(max_length=300, db_column="password",default=None, null=True)
    social_login = models.CharField(max_length=32, db_column="social_login",default='', null=True)
    social_id = models.CharField(max_length=300, db_column="social_id",default=None, null=True)
    registered_at = models.DateTimeField(db_column="registered_at",auto_now_add=True)

    class Meta:
        db_table = "user"


class Category(models.Model):
    name = models.CharField(max_length=30, db_column="name", null=False)
    content = models.CharField(max_length=100, db_column="content", null=False)

    class Meta:
        db_table = "category"


class Department(models.Model):
    name = models.CharField(max_length=10, db_column="name", null=False)
    content = models.CharField(max_length=100, db_column="content", null=False)

    class Meta:
        db_table = "department"


class Petition(models.Model):
    user = models.ForeignKey(to=User, db_column="user", on_delete=CASCADE, default=None)
    title = models.CharField(max_length=100, db_column="title", null=False, default="")
    department = models.ForeignKey(to=Department, db_column="department", on_delete=CASCADE, default=None)
    
    # 자가응답형 템플릿
    content = models.CharField(max_length=500, db_column="content", null=True, default=None)
    
    # 청원을 작성한 배경
    content_1 = models.CharField(max_length=500, db_column="content_1", null=True, default=None)
    # 제안하는 정책의 효과
    content_2 = models.CharField(max_length=500, db_column="content_2", null=True, default=None)
    # 경험했던 사례 및 근거
    content_3 = models.CharField(max_length=500, db_column="content_3", null=True, default=None)
    # 신빙성 있는 객관적 근거
    content_4 = models.CharField(max_length=500, db_column="content_4", null=True, default=None)
    # 이해를 돕는 자료
    content_5 = models.CharField(max_length=500, db_column="content_5", null=True, default=None)
    # 제안하는 정책/해결안
    content_6 = models.CharField(max_length=500, db_column="content_6", null=True, default=None)
    # 청원이 이루어지면 어떤 효과가 있을까요?
    content_7 = models.CharField(max_length=500, db_column="content_7", null=True, default=None)

    keyword_1 = models.CharField(max_length=10, db_column="keyword_1", null=True, default=None)
    keyword_2 = models.CharField(max_length=10, db_column="keyword_2", null=True, default=None)
    keyword_3 = models.CharField(max_length=10, db_column="keyword_3", null=True, default=None)

    agreements = models.IntegerField(db_column="agreements", null=False, default=0)
    thumbnail = models.ImageField(upload_to=("images/"),default='default_image.png')

    class Meta:
        db_table = "petition"


class PetitionCategory(models.Model):
    petition = models.ForeignKey(to=Petition, db_column="petition", on_delete=CASCADE)
    category = models.ForeignKey(to=Category, db_column="category", on_delete=CASCADE)

    class Meta:
        db_table = "petition_category"


class PetitionImage(models.Model):
    petition = models.ForeignKey(to=Petition, on_delete=CASCADE)
    image = models.ImageField(upload_to=("images/"))

    class Meta:
        db_table = "petition_image"


class PetitionPrediction(models.Model):
    petition = models.ForeignKey(to=Petition, db_column="petition", on_delete=CASCADE)
    ai = models.BooleanField(db_column="ai", null=False)
    user = models.ForeignKey(to=User, db_column="user", on_delete=CASCADE)
    prediction = models.BooleanField(db_column='prediction', null=False)
    
    class Meta:
        db_table = "petition_prediction"
