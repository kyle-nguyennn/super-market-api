# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DesignatedMarketMakerLiquidityLevelParam"]


class DesignatedMarketMakerLiquidityLevelParam(TypedDict, total=False):
    price: Required[float]
    """Outcome-perspective price on a 0.005 tick."""

    quantity: Required[int]
