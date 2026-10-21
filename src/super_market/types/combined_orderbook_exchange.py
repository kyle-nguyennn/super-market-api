# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .orderbook_level import OrderbookLevel
from .book_version import BookVersion

__all__ = ["CombinedOrderbookExchange"]


class CombinedOrderbookExchange(BaseModel):
    exchange_id: str = FieldInfo(alias="exchangeId")

    option: Optional[str] = None

    as_of: Optional[BookVersion] = FieldInfo(alias="asOf", default=None)
    """The engine version an exchange's book was captured at, the same `asOf` the realtime book push carries. Versions compare by `sequence`, then `at`. Null when the book was read from the database, which has no version."""

    implied_probability: Optional[float] = FieldInfo(alias="impliedProbability", default=None)
    """Best ask price, or latestPrice if no asks exist. Null when no tournament price or ask exists."""

    bids: List[OrderbookLevel]

    asks: List[OrderbookLevel]
