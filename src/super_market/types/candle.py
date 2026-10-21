# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Candle"]


class Candle(BaseModel):
    time: str
    """ISO-8601 bucket start time."""

    open: Optional[float] = None

    high: Optional[float] = None

    low: Optional[float] = None

    close: Optional[float] = None

    vwap: Optional[float] = None
    """Volume-weighted average YES price."""

    volume: float

    trade_count: int = FieldInfo(alias="tradeCount")
