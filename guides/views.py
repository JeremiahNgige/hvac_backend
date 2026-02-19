from rest_framework.decorators import api_view
from rest_framework.response import Response
from hvacapi.supabase_client import get_supabase


@api_view(['GET'])
def guide_list(request):
    """List/search/filter guides."""
    sb = get_supabase()
    query = sb.table('guides').select('*')

    # Filters
    category = request.query_params.get('category')
    difficulty = request.query_params.get('difficulty')
    search = request.query_params.get('search')

    if category:
        query = query.eq('category_id', category)
    if difficulty:
        query = query.eq('difficulty', difficulty)
    if search:
        query = query.or_(
            f'title.ilike.%{search}%,summary.ilike.%{search}%'
        )

    result = query.order('created_at', desc=True).execute()
    guides = result.data

    # Enrich with category_name and step_count
    _enrich_guides(sb, guides)

    return Response(guides)


@api_view(['GET'])
def guide_detail(request, pk):
    """Retrieve a guide with its steps and category."""
    sb = get_supabase()

    guide = (
        sb.table('guides').select('*').eq('id', pk).single().execute()
    ).data

    # Get category
    if guide.get('category_id'):
        cat = (
            sb.table('categories')
            .select('*')
            .eq('id', guide['category_id'])
            .single()
            .execute()
        ).data
        guide['category'] = cat

    # Get steps
    steps = (
        sb.table('guide_steps')
        .select('*')
        .eq('guide_id', pk)
        .order('step_number')
        .execute()
    ).data
    guide['steps'] = steps

    return Response(guide)


@api_view(['GET'])
def guide_featured(request):
    """Return featured guides."""
    sb = get_supabase()
    result = (
        sb.table('guides')
        .select('*')
        .eq('is_featured', True)
        .order('created_at', desc=True)
        .limit(6)
        .execute()
    )
    guides = result.data
    _enrich_guides(sb, guides)
    return Response(guides)


def _enrich_guides(sb, guides):
    """Add category_name and step_count to a list of guide dicts."""
    # Cache categories
    cat_ids = {g['category_id'] for g in guides if g.get('category_id')}
    cat_map = {}
    if cat_ids:
        cats = (
            sb.table('categories')
            .select('id, name')
            .in_('id', list(cat_ids))
            .execute()
        ).data
        cat_map = {c['id']: c['name'] for c in cats}

    for g in guides:
        g['category_name'] = cat_map.get(g.get('category_id'))
        # Step count
        count = (
            sb.table('guide_steps')
            .select('id', count='exact')
            .eq('guide_id', g['id'])
            .execute()
        )
        g['step_count'] = count.count or 0
