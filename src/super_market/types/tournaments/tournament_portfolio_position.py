# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TournamentPortfolioPosition", "Lot"]


class Lot(BaseModel):
    lot_id: str = FieldInfo(alias="lotId")

    side: str

    quantity: float

    entry_price: float = FieldInfo(alias="entryPrice")

    opened_at: str = FieldInfo(alias="openedAt")


class TournamentPortfolioPosition(BaseModel):
    exchange_id: str = FieldInfo(alias="exchangeId")

    market_id: str = FieldInfo(alias="marketId")

    market_title: str = FieldInfo(alias="marketTitle")

    option: Optional[str] = None

    settled: bool

    quantity: float
    """Positive = YES shares, negative = NO shares."""

    avg_cost: float = FieldInfo(alias="avgCost")

    current_price: Optional[float] = FieldInfo(alias="currentPrice", default=None)
    """Tournament valuation price. Null only for zero-quantity rows; nonzero holdings without a valuation return 409."""

    market_value: float = FieldInfo(alias="marketValue")

    cost_basis: float = FieldInfo(alias="costBasis")

    unrealized_pnl: float = FieldInfo(alias="unrealizedPnl")

    unrealized_pnl_pct: float = FieldInfo(alias="unrealizedPnlPct")

    money_earned: float = FieldInfo(alias="moneyEarned")
    """Realized cash from prior closes on this position. Engine-backed positions report 0; legacy positions report the stored realized close proceeds."""

    lots: List[Lot]
