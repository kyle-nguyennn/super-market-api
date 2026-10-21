# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BulkExchangePrice"]


class BulkExchangePrice(BaseModel):
    exchange_id: str = FieldInfo(alias="exchangeId")

    market_id: str = FieldInfo(alias="marketId")

    option: Optional[str] = None

    latest_price: Optional[float] = FieldInfo(alias="latestPrice", default=None)

    best_bid: Optional[float] = FieldInfo(alias="bestBid", default=None)

    best_ask: Optional[float] = FieldInfo(alias="bestAsk", default=None)

    spread: Optional[float] = None
