from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView

from . import views

app_name = "petition_app"

urlpatterns = [
    
    path('user/login/<str:type>', views.login),
    path('user/callback/<str:type>', views.callback),

    path('', views.index),
    path('main', views.main),
    
    path('check', views.check),
    path('check_highlight', views.check_highlight),
    path('check_keyboard', views.check_keyboard),
    path('good', views.good),
    
    path('list', views.list),
    
    path('title_finish', views.title_finish),
    path('choose_category', views.choose_category),
    path('choose_receiver', views.choose_receiver),
    path('write', views.write),
    path('write_template', views.write_template),
    path('write_template_click', views.write_template_click),
    path('inspection', views.inspection),
    
    path('detail/<int:id>', views.detail),
]