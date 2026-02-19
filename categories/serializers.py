from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    guide_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'icon_name', 'color_hex', 'guide_count']

    def get_guide_count(self, obj):
        return obj.guides.count()
