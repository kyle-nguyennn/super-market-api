# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Exchange"]


class Exchange(BaseModel):
    id: str

    option: Optional[str] = None

    latest_price: Optional[float] = FieldInfo(alias="latestPrice", default=None)
    """Latest YES trade price in the resolved context. In tournament context, null means no tournament trade has established a price; the orderbook may still contain bids and asks, and the value never falls back to the global price. In an organization-wide view of a market with more than one tournament context, this is null — read each context's price from `contexts[]`."""

    initial_price: Optional[float] = FieldInfo(alias="initialPrice", default=None)
