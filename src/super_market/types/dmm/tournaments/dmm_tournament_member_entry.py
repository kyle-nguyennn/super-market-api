# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DmmTournamentMemberEntry"]


class DmmTournamentMemberEntry(BaseModel):
    profile_id: str = FieldInfo(alias="profileId")

    username: Optional[str] = None

    email: Optional[str] = None

    avatar_url: Optional[str] = FieldInfo(alias="avatarUrl", default=None)

    joined_at: str = FieldInfo(alias="joinedAt")

    balance: float

    added_directly: bool = FieldInfo(alias="addedDirectly")
