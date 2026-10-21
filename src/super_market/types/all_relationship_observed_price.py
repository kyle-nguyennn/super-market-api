# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AllRelationshipObservedPrice"]


class AllRelationshipObservedPrice(BaseModel):
    exchange_id: str = FieldInfo(alias="exchangeId")
    """Positive numeric ID encoded as a string."""

    price: float

    market_id: Optional[str] = FieldInfo(alias="marketId", default=None)
    """Positive numeric ID encoded as a string."""

    market_title: Optional[str] = FieldInfo(alias="marketTitle", default=None)

    outcome: Optional[str] = None

    current_price: Optional[float] = FieldInfo(alias="currentPrice", default=None)
