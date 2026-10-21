# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Order"]


class Order(BaseModel):
    id: int

    exchange_id: str = FieldInfo(alias="exchangeId")

    side: Literal["yes", "no"]

    action: Literal["buy", "sell"]

    quantity: float
    """Always positive. Use `side` to determine YES/NO direction. While `open` is true this is the executable remainder; a closed order reports its unfilled remainder plus everything it filled. Orders whose remainder was discarded before they closed — legacy market orders, which never rest, and orders shrunk to fit a decreased balance — therefore report the reduced size rather than the quantity originally submitted."""

    price_limit: Optional[float] = FieldInfo(alias="priceLimit", default=None)

    open: bool
    """True if the order is still resting on the book and not expired. An order can have `open: true` yet be past its `expirationDate` — use `status=expired` to query that state."""

    created_at: str = FieldInfo(alias="createdAt")

    expiration_date: Optional[str] = FieldInfo(alias="expirationDate", default=None)
    """ISO-8601 order expiration timestamp, or null when no expiration was set. Reporting-backed orders preserve the engine order's expiration timestamp."""

    tournament_id: Optional[str] = FieldInfo(alias="tournamentId", default=None)
    """Tournament whose orderbook and balance the order belongs to, or null for a public-global order."""

    terminal_reason_code: Optional[str] = FieldInfo(alias="terminalReasonCode", default=None)
    """The trading engine's reason code for a closed order, such as `Expired` or `SelfTradePrevented`. Null while `open` is true and when no reason was recorded, which includes every order placed before the trading engine."""

    quantity_filled: Optional[float] = FieldInfo(alias="quantityFilled", default=None)
    """Always positive. Total quantity a closed order filled; `quantity` minus this is what closed unfilled. Null while `open` is true — read the order's fills for a resting order's progress."""
