from pyexpat import model
from rest_framework import serializers
from .models import Category, Product,ProductViews
from django.contrib.auth.models import User
import serpy
from drf_haystack.serializers import HaystackSerializer
from .search_indexes import ProductIndex


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ("modified",)


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        exclude=("modified",)


class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        exclude=("modified","parent",)




class ProductSerializer(serializers.ModelSerializer):
    seller = serializers.SlugRelatedField(slug_field="username", queryset=User.objects)
    category = serializers.SerializerMethodField()

    def get_category(self, obj):
        return obj.category.name

    class Meta:
        model = Product
        exclude = ("modified",)




class SerpyProductSerializer(serpy.Serializer):
    seller = serpy.StrField()
    category = serpy.StrField()
    title = serpy.StrField()
    price = serpy.FloatField()
    image = serpy.StrField()
    description = serpy.StrField()
    quantity = serpy.IntField()
    views = serpy.IntField()



class ProductViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductViews
        exclude = "modified"

class ProductIndexSerializer(HaystackSerializer):
    class Meta:
        
        index_classes = [ProductIndex]
        fields = ("text", "title", "category",)
