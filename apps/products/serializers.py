from rest_framework import serializers
from .models import Category, Product
from django.contrib.auth.models import User



class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ("modified",)


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        exclude=("modified",)


class ProductSerializer(serializers.ModelSerializer):
    seller = serializers.SlugRelatedField(slug_field="username", queryset=User.objects)
    category = serializers.SerializerMethodField()
