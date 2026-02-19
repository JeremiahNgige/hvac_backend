from rest_framework import serializers
from .models import Guide, GuideStep
from categories.serializers import CategorySerializer


class GuideStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuideStep
        fields = ['id', 'step_number', 'title', 'description', 'pro_tip']


class GuideListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for list views."""
    category_name = serializers.CharField(source='category.name', read_only=True)
    step_count = serializers.SerializerMethodField()

    class Meta:
        model = Guide
        fields = [
            'id', 'title', 'summary', 'difficulty', 'estimated_time',
            'image_url', 'is_featured', 'category', 'category_name',
            'step_count', 'created_at',
        ]

    def get_step_count(self, obj):
        return obj.steps.count()


class GuideDetailSerializer(serializers.ModelSerializer):
    """Full serializer with nested steps."""
    category = CategorySerializer(read_only=True)
    steps = GuideStepSerializer(many=True, read_only=True)

    class Meta:
        model = Guide
        fields = [
            'id', 'title', 'summary', 'difficulty', 'estimated_time',
            'image_url', 'is_featured', 'category', 'steps', 'created_at',
        ]
