# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SettlementEntry"]


class SettlementEntry(BaseModel):
    id: str
    """Legacy entries use a UUID; engine-recorded entries use `engine-<sequence>`."""

    type: Optional[Literal["win", "loss", "refund", "correction"]] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    market_id: Optional[str] = FieldInfo(alias="marketId", default=None)

    market_title: Optional[str] = FieldInfo(alias="marketTitle", default=None)

    exchange_id: Optional[str] = FieldInfo(alias="exchangeId", default=None)

    settlement_option: Optional[str] = FieldInfo(alias="settlementOption", default=None)
    """The exchange's outcome label (e.g. "YES", "NO", "Trump")."""

    settlement_outcome: Optional[str] = FieldInfo(alias="settlementOutcome", default=None)
    """The outcome the market resolved to (from settlement metadata). Null for engine-recorded entries."""

    shares: Optional[float] = None
    """Share quantity reported by this settlement entry; null when unavailable. Do not infer YES/NO direction from its sign."""

    avg_entry_price: Optional[float] = FieldInfo(alias="avgEntryPrice", default=None)
    """Null for engine-recorded entries."""

    cost_basis: Optional[float] = FieldInfo(alias="costBasis", default=None)
    """Null for engine-recorded entries."""

    payout: float
    """Cash credited (or 0 for losses) by this settlement entry."""

    realized_pnl: Optional[float] = FieldInfo(alias="realizedPnl", default=None)
    """Null for engine-recorded entries."""
