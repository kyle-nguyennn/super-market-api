# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .order_pagination import OrderPagination

__all__ = ["OrderListFillsResponse", "Data", "Coverage"]


class Coverage(BaseModel):
    complete: Literal[True]
    """Always true because cursor pagination exposes the complete order fill history."""

    projected_through_sequence: Optional[int] = FieldInfo(alias="projectedThroughSequence", default=None)
    """Latest trading-engine sequence reflected by the reporting projection, or null when no checkpoint exists."""


class Data(BaseModel):
    id: int
    """Trade identifier, shared by both counterparties' fills of the same trade. Engine-recorded fills use the trading-engine trade sequence; pre-cutover fills use the legacy trade ID — the two are separate ID spaces. Not an order ID — use orderId to look up the associated order."""

    price: Optional[float] = None

    quantity: float
    """Outcome-signed fill quantity; negative values indicate the NO side."""

    side: Literal["yes", "no"]

    filled_at: str = FieldInfo(alias="filledAt")


class OrderListFillsResponse(BaseModel):
    order_id: int = FieldInfo(alias="orderId")

    exchange_id: str = FieldInfo(alias="exchangeId")

    tournament_id: Optional[str] = FieldInfo(alias="tournamentId", default=None)
    """Tournament this order belongs to, or null for global orders."""

    data: List[Data]

    pagination: OrderPagination

    coverage: Coverage

    total_quantity_filled: float = FieldInfo(alias="totalQuantityFilled")
    """Exact outcome-signed filled quantity for the whole order, not only this page; negative values indicate the NO side."""

    avg_fill_price: Optional[float] = FieldInfo(alias="avgFillPrice", default=None)
    """Exact average fill price for the whole order, or null before the first fill."""
