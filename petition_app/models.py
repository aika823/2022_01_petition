from django.db import models
from django.db.models.deletion import CASCADE


class Category(models.Model):
    name = models.CharField(max_length=20, db_column="name", null=False)
    
    class Meta:
        db_table = "category"


class User(models.Model):
    email = models.EmailField(max_length=300)
    name = models.CharField(max_length=20, db_column="name", null=False, default="")
    password = models.CharField(max_length=300, default=None, null=True)
    social_login = models.CharField(max_length=32, default='', null=True)
    social_id = models.CharField(max_length=300, default=None, null=True)
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user"


class Petition(models.Model):
    user = models.ForeignKey(to=User, on_delete=CASCADE)
    category = models.ForeignKey(to=Category, on_delete=CASCADE)
    title = models.CharField(max_length=100, db_column="title", null=False, default="")
    content = models.CharField(max_length=500, db_column="content", null=False, default="")
    agreements = models.IntegerField(db_column="agreements", null=False, default=0)
    thumbnail = models.ImageField(upload_to=("media/images"),default='default_image.png')

    class Meta:
        db_table = "petition"


class PetitionImage(models.Model):
    petition = models.ForeignKey(to=Petition, on_delete=CASCADE)
    image = models.ImageField(upload_to=("media/images"))

    class Meta:
        db_table = "petition_image"