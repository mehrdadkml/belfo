from django.shortcuts import render
from .serializers import CategoryListSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Category




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
