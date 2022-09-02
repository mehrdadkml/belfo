from django.urls import path, include
from . import views,viewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"product-search", viewsets.ProductSearchView)
app_name = "products"

urlpatterns = [
    path('', include(router.urls)),
    path("category/", views.CategoryListAPIView.as_view()),
    path("create/product/", views.CreateProductAPIView.as_view()),
    path("create/category/", views.CreateCategoryAPIView.as_view()),
    path("list-product/user/", views.ListUserProductAPIView.as_view()),
    path("product/views/", views.ProductViewsAPIView.as_view()),
    
]
