# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrderCreateMultiLegParams", "Leg"]


class OrderCreateMultiLegParams(TypedDict, total=False):
    legs: Required[Iterable[Leg]]

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="idempotencyKey")]]
    """Required client-supplied idempotency key. Reuse this key only when retrying the same logical request. An identical resolved payload replays the exact stored response; reuse with a different resolved payload returns 409."""

    relationship_constraint: Annotated[str, PropertyInfo(alias="relationshipConstraint")]
    """Optional active ALL relationship UUID. Every leg exchange must belong to it, and an exchange may appear only once per tournament scope. Validation evaluates prices in YES terms: YES leg limit prices are unchanged, NO leg limit prices use their YES-complement price, and uncovered nodes or market orders use current engine prices. Exhaustive mutually exclusive relationships require sum(P) = 1; non-exhaustive mutually exclusive relationships require sum(P) ≤ 1."""


class Leg(TypedDict, total=False):
    exchange_id: Required[Annotated[str, PropertyInfo(alias="exchangeId")]]
    """Exchange ID as a numeric string."""

    side: Required[Literal["yes", "no"]]

    action: Required[Literal["buy", "sell"]]

    quantity: Required[int]
    """Number of shares, at most 2147483647 (the trading engine holds quantities as a signed 32-bit integer). Larger values are rejected with `VALIDATION_ERROR`."""

    price: float
    """Limit price in [0, 1]. Limit prices must be on the 0.005 tick between 0.005 and 0.995. `1` with `action: "buy"` and `0` with `action: "sell"` mean a market order; omit `price` for a market order. Off-tick values are rejected with `VALIDATION_ERROR`."""

    expiration_date: Annotated[Union[str, datetime], PropertyInfo(alias="expirationDate", format="iso8601")]
    """Optional future ISO 8601 datetime after which the limit order expires. Not supported for market orders."""

    tournament_id: Annotated[str, PropertyInfo(alias="tournamentId")]
    """When provided, routes the order through that accessible tournament's isolated orderbook and balance. A first order in an open tournament, or by an owner or admin in any tournament of their organization, enrols the caller. When omitted, an organization-bound key uses its organization's default tournament; an unbound key uses the public global context."""
