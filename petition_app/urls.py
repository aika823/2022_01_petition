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
    path('check/highlight', views.check_highlight),
    path('check/keyboard', views.check_keyboard),
    path('good', views.good),
    
    path('write', views.write),
    path('write/title', views.write_title),
    path('write/category', views.write_category),
    path('write/receiver', views.write_receiver),
    path('write/template/qna', views.write_template_qna),
    path('write/template/click', views.write_template_click),
    
    path('inspection', views.inspection),
    
    path('list', views.list),
    path('detail/<int:id>', views.detail),
]