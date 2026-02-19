from rest_framework.decorators import api_view
from rest_framework.response import Response
from hvacapi.supabase_client import get_supabase


@api_view(['GET'])
def category_list(request):
    """List all HVAC categories with guide count."""
    sb = get_supabase()
    result = sb.table('categories').select('*').order('name').execute()
    categories = result.data

    # Attach guide_count to each category
    for cat in categories:
        count_result = (
            sb.table('guides')
            .select('id', count='exact')
            .eq('category_id', cat['id'])
            .execute()
        )
        cat['guide_count'] = count_result.count or 0

    return Response(categories)


@api_view(['GET'])
def category_detail(request, pk):
    """Retrieve a single category."""
    sb = get_supabase()
    result = sb.table('categories').select('*').eq('id', pk).single().execute()
    category = result.data

    count_result = (
        sb.table('guides')
        .select('id', count='exact')
        .eq('category_id', pk)
        .execute()
    )
    category['guide_count'] = count_result.count or 0

    return Response(category)
