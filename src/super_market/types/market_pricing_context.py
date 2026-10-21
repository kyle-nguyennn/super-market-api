# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .market_read_context_descriptor import MarketReadContextDescriptor
from .market_context_exchange import MarketContextExchange

__all__ = ["MarketPricingContext"]


class MarketPricingContext(MarketReadContextDescriptor):
    status: Literal["open", "closed", "settled"]
    """Lifecycle status in this context. An organization or tournament settlement settles the market here even while it stays open globally."""

    settled_with: Optional[str] = FieldInfo(alias="settledWith", default=None)
    """Effective settlement in this context: the organization/tournament ruling when one exists, otherwise the global one."""

    settled_on: Optional[str] = FieldInfo(alias="settledOn", default=None)

    exchanges: List[MarketContextExchange]
