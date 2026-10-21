# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .all_execution_economics import AllExecutionEconomics

__all__ = ["OrderCreateResponse"]


class OrderCreateResponse(BaseModel):
    order_id: Optional[int] = FieldInfo(alias="orderId", default=None)

    exchange_id: str = FieldInfo(alias="exchangeId")

    open: bool
    """True if the order is resting on the book; false if fully filled."""

    remaining_quantity: Optional[float] = FieldInfo(alias="remainingQuantity", default=None)
    """Engine-authoritative unfilled quantity after admission resizing. Present for engine-routed orders."""

    action: Optional[Literal["buy", "sell"]] = None
    """Canonical engine action. Present for engine-routed orders; may differ from the requested action when a sell is converted to its complement buy."""

    side: Optional[Literal["yes", "no"]] = None
    """Canonical engine outcome side. Present for engine-routed orders."""

    price: Optional[float] = None
    """Canonical engine limit price in side-relative terms. Present for engine-routed orders."""

    quantity: Optional[int] = None
    """Canonical engine quantity as a positive integer. Present for engine-routed orders."""

    terminal_reason_code: Optional[str] = FieldInfo(alias="terminalReasonCode", default=None)
    """Canonical terminal reason, including SelfTradePrevented, or null when the placed order has no terminal reason. Present for engine-routed orders."""

    quantity_traded: float = FieldInfo(alias="quantityTraded")

    total_cost: float = FieldInfo(alias="totalCost")

    fill_price: Optional[float] = FieldInfo(alias="fillPrice", default=None)
    """Price of the order's last fill, or null when nothing filled (`quantityTraded` is 0)."""

    all: Optional[AllExecutionEconomics] = None
    """Authoritative ALL execution economics, or null when no engine relationship quote was produced."""
