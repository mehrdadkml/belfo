from rest_framework import serializers
from .models import Category, Product



class CategoryListSerializer(serializers.ModelSerializer):
    # lft = serializers.SlugRelatedField(slug_field='lft', read_only=True)
    class Meta:
        model = Category
        # queryset = Category.objects.all()
        
        exclude = "modified"
