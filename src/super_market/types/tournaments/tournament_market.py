# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TournamentMarket", "Exchange", "Creator"]


class Creator(BaseModel):
    id: str

    username: Optional[str] = None


class Exchange(BaseModel):
    id: str

    option: Optional[str] = None

    latest_price: Optional[float] = FieldInfo(alias="latestPrice", default=None)
    """Tournament-specific latest traded price. Null when no tournament trade has established a price; the tournament orderbook may still contain bids and asks. It never falls back to the global price."""

    initial_price: Optional[float] = FieldInfo(alias="initialPrice", default=None)


class TournamentMarket(BaseModel):
    id: str

    title: str

    status: Literal["open", "closed", "settled"]

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    settlement_date: Optional[str] = FieldInfo(alias="settlementDate", default=None)

    settled_with: Optional[str] = FieldInfo(alias="settledWith", default=None)

    settled_on: Optional[str] = FieldInfo(alias="settledOn", default=None)
    """Effective settlement timestamp in this tournament context. When the tournament has its own ruling, this is the tournament-scoped settlement timestamp."""

    categories: List[str]

    is_composite: bool = FieldInfo(alias="isComposite")

    is_multi_outcome: bool = FieldInfo(alias="isMultiOutcome")

    exchanges: List[Exchange]

    creator: Optional[Creator] = None

    thumbnail_url: Optional[str] = FieldInfo(alias="thumbnailUrl", default=None)
    """Market header image URL, or null."""
