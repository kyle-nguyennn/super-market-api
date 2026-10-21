# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .book_version import BookVersion
from .exchange_orderbook_level import ExchangeOrderbookLevel

__all__ = ["ExchangeListOrderbookResponse"]


class ExchangeListOrderbookResponse(BaseModel):
    exchange_id: str = FieldInfo(alias="exchangeId")

    market_id: str = FieldInfo(alias="marketId")

    as_of: Optional[BookVersion] = FieldInfo(alias="asOf", default=None)
    """The engine version an exchange's book was captured at, the same `asOf` the realtime book push carries. Versions compare by `sequence`, then `at`. Null when the book was read from the database, which has no version."""

    depth: int

    bids: List[ExchangeOrderbookLevel]

    asks: List[ExchangeOrderbookLevel]

    best_bid: Optional[float] = FieldInfo(alias="bestBid", default=None)

    best_ask: Optional[float] = FieldInfo(alias="bestAsk", default=None)

    spread: Optional[float] = None
