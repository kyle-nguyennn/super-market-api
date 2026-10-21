# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .exchange import Exchange
from .market_pricing_context import MarketPricingContext

__all__ = ["Market", "Creator"]


class Creator(BaseModel):
    id: str

    username: Optional[str] = None


class Market(BaseModel):
    id: str

    title: str

    thumbnail_url: Optional[str] = FieldInfo(alias="thumbnailUrl", default=None)
    """Current market thumbnail URL, or null when the market has no thumbnail."""

    status: Literal["open", "closed", "settled"]
    """Lifecycle status in the request's scope. Organization and tournament reads reflect that scope's settlement; see `contexts` for each context."""

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    settlement_date: Optional[str] = FieldInfo(alias="settlementDate", default=None)

    settled_with: Optional[str] = FieldInfo(alias="settledWith", default=None)
    """Effective settlement in the request's scope: an organization or tournament ruling when one exists, otherwise the global one."""

    settled_on: Optional[str] = FieldInfo(alias="settledOn", default=None)

    categories: List[str]

    is_composite: bool = FieldInfo(alias="isComposite")

    is_multi_outcome: bool = FieldInfo(alias="isMultiOutcome")

    exchanges: List[Exchange]

    contexts: List[MarketPricingContext]
    """The accessible pricing contexts for this canonical market row. Organization-wide discovery may return multiple tournament contexts for one market."""

    creator: Optional[Creator] = None
