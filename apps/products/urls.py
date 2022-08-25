from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

app_name = "products"

urlpatterns = [
    path('', include(router.urls)),
    path("category/", views.CategoryListAPIView.as_view()),

    
    

]
