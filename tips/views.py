from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tip
from .serializers import TipSerializer


@api_view(['GET'])
def tip_list(request):
    """List tips with optional type/category filtering."""
    tips = Tip.objects.select_related('category').all()

    tip_type = request.query_params.get('type')
    category = request.query_params.get('category')

    if tip_type:
        tips = tips.filter(tip_type=tip_type)
    if category:
        tips = tips.filter(category_id=category)

    tips = tips.order_by('-created_at')
    
    serializer = TipSerializer(tips, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def tip_detail(request, pk):
    """Retrieve a single tip."""
    try:
        tip = Tip.objects.select_related('category').get(pk=pk)
    except Tip.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)
        
    serializer = TipSerializer(tip)
    return Response(serializer.data)


@api_view(['GET'])
def tip_featured(request):
    """Return featured tips."""
    tips = Tip.objects.select_related('category').filter(is_featured=True).order_by('-created_at')[:6]
    serializer = TipSerializer(tips, many=True)
    return Response(serializer.data)
