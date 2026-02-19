import os
from typing import Optional
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

SUPABASE_URL: str = os.environ.get('SUPABASE_URL', '')
SUPABASE_KEY: str = os.environ.get('SUPABASE_KEY', '')

_client: Optional[Client] = None


def get_supabase() -> Client:
    """Return a singleton Supabase client."""
    global _client
    if _client is None:
        if not SUPABASE_URL or not SUPABASE_KEY:
            raise RuntimeError(
                'SUPABASE_URL and SUPABASE_KEY must be set in backend/.env'
            )
        _client = create_client(SUPABASE_URL, SUPABASE_KEY)
    return _client
