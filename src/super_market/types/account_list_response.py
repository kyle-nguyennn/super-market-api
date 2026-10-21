# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AccountListResponse"]


class AccountListResponse(BaseModel):
    id: str

    username: Optional[str] = None

    email: Optional[str] = None

    created_at: str = FieldInfo(alias="createdAt")

    avatar_url: Optional[str] = FieldInfo(alias="avatarUrl", default=None)

    bio: Optional[str] = None

    balance: Optional[float] = None
    """Default-tournament balance for an organization-bound key; public-global cash balance for an unbound key."""
