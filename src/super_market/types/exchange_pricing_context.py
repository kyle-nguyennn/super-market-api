# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ExchangePricingContext", "Tournament"]


class Tournament(BaseModel):
    id: str

    slug: str

    name: str

    currency_name: str = FieldInfo(alias="currencyName")

    is_ongoing_play: bool = FieldInfo(alias="isOngoingPlay")


class ExchangePricingContext(BaseModel):
    type: Literal["public", "tournament"]

    tournament: Optional[Tournament] = None

    latest_price: Optional[float] = FieldInfo(alias="latestPrice", default=None)
    """Latest YES trade price in this exact public or tournament context."""
