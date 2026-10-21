# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DmmTournamentBoundGroup"]


class DmmTournamentBoundGroup(BaseModel):
    id: str

    name: str

    slug: str

    description: Optional[str] = None

    member_count: int = FieldInfo(alias="memberCount")

    bound: bool

    bound_at: Optional[str] = FieldInfo(alias="boundAt", default=None)
