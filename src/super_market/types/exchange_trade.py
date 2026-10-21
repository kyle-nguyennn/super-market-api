# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ExchangeTrade"]


class ExchangeTrade(BaseModel):
    id: str
    """Trade identifier: the trading-engine trade sequence for engine-recorded trades, or the legacy trade ID for pre-cutover trades. The two are separate ID spaces."""

    created_at: str = FieldInfo(alias="createdAt")

    price: Optional[float] = None
    """YES-normalized fill price."""

    size: int
    """Shares traded (absolute value of the underlying signed quantity)."""

    side: Literal["YES", "NO"]
    """Whether the fill happened in YES or NO space."""

    volume: float
    """Notional volume. Engine-recorded trades report `size` × the executed side's price, unrounded; pre-cutover trades report the stored trade volume."""
