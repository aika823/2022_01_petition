from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf.urls.static import static
from api import views as api_views


urlpatterns = [
    path("api/check_validation", api_views.check_validation),
    path("api/predict_petition", api_views.predict_petition),
    path("api/agree_petition", api_views.agree_petition),
    path("", include("petition_app.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)