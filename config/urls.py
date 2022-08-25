
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from django.conf.urls import url

router = DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("api-auth/",include('rest_framework.urls')),
    path("api/rest-auth/",include('rest_auth.urls')),
    path("", include("apps.products.urls")),

]


