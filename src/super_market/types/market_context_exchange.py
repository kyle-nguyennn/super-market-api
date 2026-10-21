# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MarketContextExchange"]


class MarketContextExchange(BaseModel):
    id: str

    latest_price: Optional[float] = FieldInfo(alias="latestPrice", default=None)
    """Latest YES trade price in this exact public or tournament context. Null means no trade has established a tournament price."""
