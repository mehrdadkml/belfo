from django.shortcuts import render
from .serializers import CategoryListSerializer,CreateProductSerializer
from rest_framework.generics import ListAPIView,CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters,permissions,status
from ..core.decorators import time_calculator
from .models import Category
from django.core.cache import cache
from rest_framework.response import Response
import logging

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






