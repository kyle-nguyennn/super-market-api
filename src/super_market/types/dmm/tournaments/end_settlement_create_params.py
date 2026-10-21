# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, Required, TypedDict

from ...._utils import PropertyInfo

__all__ = ["EndSettlementCreateParams", "SubmittedPrice"]


class EndSettlementCreateParams(TypedDict, total=False):
    submitted_prices: Annotated[Iterable[SubmittedPrice], PropertyInfo(alias="submittedPrices")]
    """Submitted prices for exchanges flagged with `needsSubmittedPrice` in the GET preview. Accepted only when the tournament scope has engine trading activity or nonzero app holdings and no final valuation price."""


class SubmittedPrice(TypedDict, total=False):
    exchange_id: Required[Annotated[str, PropertyInfo(alias="exchangeId")]]
    """Exchange ID as an integer string."""

    price: Required[float]
    """Submitted final settlement price for an exchange that needs a price. Boundary values 0 and 1 are accepted."""
