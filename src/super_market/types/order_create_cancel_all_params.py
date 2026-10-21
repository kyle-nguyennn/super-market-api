# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrderCreateCancelAllParams"]


class OrderCreateCancelAllParams(TypedDict, total=False):
    exchange_id: Annotated[str, PropertyInfo(alias="exchangeId")]
    """Scope cancellation to a specific exchange. Numeric string. Mutually exclusive with marketId."""

    market_id: Annotated[str, PropertyInfo(alias="marketId")]
    """Scope cancellation to all exchanges in a market. Numeric string. Mutually exclusive with exchangeId."""

    tournament_id: Annotated[str, PropertyInfo(alias="tournamentId")]
    """Scope cancellation to a specific accessible tournament. Omit for the organization's default tournament with an organization-bound key or public global orders with an unbound key."""
