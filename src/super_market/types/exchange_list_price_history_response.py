# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .candle import Candle

__all__ = ["ExchangeListPriceHistoryResponse", "Coverage"]


class Coverage(BaseModel):
    complete: bool
    """False only when an explicit `from` window was truncated by the candle limit."""

    projected_through_sequence: Optional[int] = FieldInfo(alias="projectedThroughSequence", default=None)
    """Latest trading-engine sequence these candles are complete through — the lower of the reporting projection's position and the event-ingest position, since both write this store. Null when either has no checkpoint, including on a deployment the engine has never touched."""


class ExchangeListPriceHistoryResponse(BaseModel):
    exchange_id: str = FieldInfo(alias="exchangeId")

    market_id: str = FieldInfo(alias="marketId")

    resolution: Literal["1m", "5m", "1h", "1d", "1w"]

    from_: str = FieldInfo(alias="from")

    to: str

    candles: List[Candle]

    coverage: Coverage
