from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from .models import Guide
from .serializers import GuideListSerializer, GuideDetailSerializer


@api_view(['GET'])
def guide_list(request):
    """List/search/filter guides."""
    guides = Guide.objects.select_related('category').all()

    # Filters
    category = request.query_params.get('category')
    difficulty = request.query_params.get('difficulty')
    search = request.query_params.get('search')

    if category:
        guides = guides.filter(category_id=category)
    if difficulty:
        guides = guides.filter(difficulty=difficulty)
    if search:
        guides = guides.filter(
            Q(title__icontains=search) | Q(summary__icontains=search)
        )

    guides = guides.order_by('-created_at')
    
    serializer = GuideListSerializer(guides, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def guide_detail(request, pk):
    """Retrieve a guide with its steps and category."""
    try:
        guide = Guide.objects.select_related('category').prefetch_related('steps').get(pk=pk)
    except Guide.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)
        
    serializer = GuideDetailSerializer(guide)
    return Response(serializer.data)


@api_view(['GET'])
def guide_featured(request):
    """Return featured guides."""
    guides = Guide.objects.select_related('category').filter(is_featured=True).order_by('-created_at')[:6]
    serializer = GuideListSerializer(guides, many=True)
    return Response(serializer.data)
