# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Fill"]


class Fill(BaseModel):
    id: int
    """Trade identifier, shared by both counterparties' fills of the same trade. Engine-recorded fills use the trading-engine trade sequence; pre-cutover fills use the legacy trade ID — the two are separate ID spaces. Not an order ID — use orderId to look up the associated order."""

    order_id: Optional[int] = FieldInfo(alias="orderId", default=None)
    """The order that was filled. Use this ID with GET /orders/{id}."""

    exchange_id: str = FieldInfo(alias="exchangeId")

    market_id: str = FieldInfo(alias="marketId")

    price: Optional[float] = None

    quantity: float
    """Outcome-signed fill quantity; negative values indicate the NO side."""

    side: Literal["yes", "no"]

    filled_at: str = FieldInfo(alias="filledAt")
