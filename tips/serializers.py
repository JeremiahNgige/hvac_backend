from rest_framework import serializers
from .models import Tip


class TipSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source='category.name', read_only=True, default=None
    )

    class Meta:
        model = Tip
        fields = [
            'id', 'title', 'content', 'tip_type', 'is_featured',
            'category', 'category_name', 'created_at',
        ]
