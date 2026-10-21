# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrderListParams"]


class OrderListParams(TypedDict, total=False):
    status: Literal["open", "closed", "expired", "all"]
    """Filter by order status. `open` — resting orders that have not expired. `closed` — filled, cancelled, or expired orders. `expired` — legacy orders still stored as open but past their `expirationDate`, plus engine orders cancelled with reason `Expired` (reporting terminal reason code `Expired`). `all` — no filter."""

    exchange_id: Annotated[str, PropertyInfo(alias="exchangeId")]
    """Filter to a specific exchange."""

    market_id: Annotated[str, PropertyInfo(alias="marketId")]
    """Filter to all exchanges in a market."""

    limit: int
    """Results per page (max 200)."""

    cursor: str
    """Pagination cursor from a previous response."""

    tournament_id: Annotated[str, PropertyInfo(alias="tournamentId")]
    """Filter to orders placed in a specific accessible tournament. Omit to use the organization's default tournament for an organization-bound key or public global orders for an unbound key."""
