# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .exchange_pricing_context import ExchangePricingContext

__all__ = ["ExchangeListItem"]


class ExchangeListItem(BaseModel):
    id: str

    market_id: str = FieldInfo(alias="marketId")

    option: Optional[str] = None

    latest_price: Optional[float] = FieldInfo(alias="latestPrice", default=None)
    """Singular public or tournament price. Null for organization-wide rows with multiple accessible contexts; use `contexts` in that case."""

    initial_price: Optional[float] = FieldInfo(alias="initialPrice", default=None)

    contexts: List[ExchangePricingContext]
