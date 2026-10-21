# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, Required, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SettlementOverrideCreatePreviewParams", "Override"]


class SettlementOverrideCreatePreviewParams(TypedDict, total=False):
    reason: Required[str]
    """Operator-visible audit reason stored on every correction transaction."""

    overrides: Required[Iterable[Override]]
    """Batch of exchange corrections within this one tournament. Duplicate exchange IDs are rejected."""


class Override(TypedDict, total=False):
    exchange_id: Required[Annotated[str, PropertyInfo(alias="exchangeId")]]
    """Exchange ID as a positive integer string."""

    price: Required[float]
    """Corrected final settlement valuation. `0` and `1` are allowed for complete no/yes outcomes."""
