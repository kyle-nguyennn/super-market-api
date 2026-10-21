# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DmmTournamentMarketEntry", "Group"]


class Group(BaseModel):
    id: str

    name: str

    slug: str


class DmmTournamentMarketEntry(BaseModel):
    market_id: str = FieldInfo(alias="marketId")

    title: str

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    status: Literal["open", "closed", "settled"]

    added_directly: bool = FieldInfo(alias="addedDirectly")
    """Whether this market was added by an admin (vs. supplied by a bound group)."""

    groups: List[Group]
