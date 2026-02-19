from rest_framework.decorators import api_view
from rest_framework.response import Response
from hvacapi.supabase_client import get_supabase


@api_view(['GET'])
def tip_list(request):
    """List tips with optional type/category filtering."""
    sb = get_supabase()
    query = sb.table('tips').select('*')

    tip_type = request.query_params.get('type')
    category = request.query_params.get('category')

    if tip_type:
        query = query.eq('tip_type', tip_type)
    if category:
        query = query.eq('category_id', category)

    result = query.order('created_at', desc=True).execute()
    tips = result.data

    # Enrich with category_name
    _enrich_tips(sb, tips)

    return Response(tips)


@api_view(['GET'])
def tip_detail(request, pk):
    """Retrieve a single tip."""
    sb = get_supabase()
    tip = sb.table('tips').select('*').eq('id', pk).single().execute().data

    if tip.get('category_id'):
        cat = (
            sb.table('categories')
            .select('name')
            .eq('id', tip['category_id'])
            .single()
            .execute()
        ).data
        tip['category_name'] = cat['name']

    return Response(tip)


@api_view(['GET'])
def tip_featured(request):
    """Return featured tips."""
    sb = get_supabase()
    result = (
        sb.table('tips')
        .select('*')
        .eq('is_featured', True)
        .order('created_at', desc=True)
        .limit(6)
        .execute()
    )
    tips = result.data
    _enrich_tips(sb, tips)
    return Response(tips)


def _enrich_tips(sb, tips):
    """Add category_name to tip dicts."""
    cat_ids = {t['category_id'] for t in tips if t.get('category_id')}
    cat_map = {}
    if cat_ids:
        cats = (
            sb.table('categories')
            .select('id, name')
            .in_('id', list(cat_ids))
            .execute()
        ).data
        cat_map = {c['id']: c['name'] for c in cats}

    for t in tips:
        t['category_name'] = cat_map.get(t.get('category_id'))
