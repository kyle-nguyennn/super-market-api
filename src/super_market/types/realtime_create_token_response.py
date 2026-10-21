# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RealtimeCreateTokenResponse", "Channels"]


class Channels(BaseModel):
    user: str


class RealtimeCreateTokenResponse(BaseModel):
    token: str

    expires_at: str = FieldInfo(alias="expiresAt")

    supabase_url: str = FieldInfo(alias="supabaseUrl")
    """Base project URL — createClient(supabaseUrl, anonKey)."""

    anon_key: str = FieldInfo(alias="anonKey")
    """Publishable/anon key — pass as the connection apikey (createClient second arg)."""

    channels: Channels
