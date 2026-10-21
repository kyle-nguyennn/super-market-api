# File generated from our OpenAPI spec by Scalar. See README.md for details.

from ...._models import BaseModel

__all__ = ["DesignatedMarketMakerLiquidityLevel"]


class DesignatedMarketMakerLiquidityLevel(BaseModel):
    price: float
    """Outcome-perspective price on a 0.005 tick."""

    quantity: int
