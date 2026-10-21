# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from ..book_version import BookVersion

__all__ = ["TournamentExchangeWithOrderbook", "Bid", "Ask"]


class Ask(BaseModel):
    price: float

    quantity: float


class Bid(BaseModel):
    price: float

    quantity: float


class TournamentExchangeWithOrderbook(BaseModel):
    id: str

    option: Optional[str] = None

    latest_price: Optional[float] = FieldInfo(alias="latestPrice", default=None)
    """Tournament-specific latest traded price. Null when no tournament trade has established a price; the tournament orderbook may still contain bids and asks. It never falls back to the global price."""

    initial_price: Optional[float] = FieldInfo(alias="initialPrice", default=None)

    as_of: Optional[BookVersion] = FieldInfo(alias="asOf", default=None)
    """The engine version an exchange's book was captured at, the same `asOf` the realtime book push carries. Versions compare by `sequence`, then `at`. Null when the book was read from the database, which has no version."""

    bids: List[Bid]

    asks: List[Ask]

    best_bid: Optional[float] = FieldInfo(alias="bestBid", default=None)

    best_ask: Optional[float] = FieldInfo(alias="bestAsk", default=None)
