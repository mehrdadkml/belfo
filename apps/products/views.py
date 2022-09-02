from django.shortcuts import render
from .serializers import CategoryListSerializer,CreateProductSerializer,ProductSerializer,CreateCategorySerializer,ProductViewsSerializer

from rest_framework.generics import ListAPIView,CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters,permissions,status
from ..core.decorators import time_calculator
from .models import Category,Product,User,ProductViews
from django.core.cache import cache
from rest_framework.response import Response
import logging
from django.http import JsonResponse

logger = logging.getLogger(__name__)



class CategoryListAPIView(ListAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = ("name",)
    ordering_fields = ("created",)
    filter_fields = ("created",)
    queryset = Category.objects.all()

    @time_calculator
    def time(self):
        return 0

    def get_queryset(self):
        queryset = Category.objects.all()
        self.time()
        return queryset

class CreateProductAPIView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CreateProductSerializer
    def create(self,request,*args,**kwargs):

        user=request.user
        serializer=self.get_serializer(data=request.data)
        logger.info(
            "محصول ( "
            + str(serializer.data.get("title"))
            + " ) فروشنده"
            + " در ( "
            + str(user.username)
            + " )"
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CreateCategoryAPIView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class =CreateCategorySerializer

    def create(self,request,*args,**kwargs):
        user=request.user
        serializer=self.get_serializer(data=request.data)
        logger.info(
            "محصول ( "
            + str(serializer.data.get("name"))
            + " ) فروشنده"
         
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.data, status=status.HTTP_201_CREATED)


  



class ListUserProductAPIView(ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = (
        "title",
        "user__username",
    )
    ordering_fields = ("created",)
    filter_fields = ("views",)

    def get_queryset(self):
        user = self.request.user
        queryset = Product.objects.filter(seller=user)
        # queryset = Product.objects.filter(user=User).values()
        
        # return JsonResponse({"user_product": list(queryset)})
        return queryset


class ProductViewsAPIView(ListAPIView):
    
    serializer_class = ProductViewsSerializer
    queryset = ProductViews.objects.all()



