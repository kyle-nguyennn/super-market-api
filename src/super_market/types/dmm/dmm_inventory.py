# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "DmmInventory",
    "Tournament",
    "Market",
    "MarketOutcome",
    "MarketOutcomeInventory",
    "MarketOutcomeMarkToMarket",
    "MarketOutcomeRestingOrders",
    "MarketOutcomeRestingOrdersBids",
    "MarketOutcomeRestingOrdersAsks",
    "MarketOutcomeWorstCase",
    "Summary",
]


class Summary(BaseModel):
    total_net_cash: float = FieldInfo(alias="totalNetCash")
    """Sum of per-outcome netCash across shown outcomes."""

    total_market_value: float = FieldInfo(alias="totalMarketValue")

    total_unrealized_pnl: float = FieldInfo(alias="totalUnrealizedPnl")

    total_resting_bid_notional: float = FieldInfo(alias="totalRestingBidNotional")

    total_resting_ask_notional: float = FieldInfo(alias="totalRestingAskNotional")

    total_worst_case_loss: float = FieldInfo(alias="totalWorstCaseLoss")
    """Sum of each market's true (correlated) worst-case loss. Within a multi-outcome market only one outcome can settle YES, so this nets mutually-exclusive outcomes instead of summing per-outcome losses independently."""


class MarketOutcomeWorstCase(BaseModel):
    pnl_if_yes: float = FieldInfo(alias="pnlIfYes")
    """Settlement P&L if the outcome settles YES (netCash + netShares; a short position is a liability here)."""

    pnl_if_no: float = FieldInfo(alias="pnlIfNo")
    """Settlement P&L if the outcome settles NO (just netCash; YES shares pay nothing and a short owes nothing)."""

    worst_case_loss: float = FieldInfo(alias="worstCaseLoss")
    """Non-negative magnitude of the worse settlement outcome."""


class MarketOutcomeRestingOrdersAsks(BaseModel):
    count: int
    """Number of open maker orders on this side."""

    quantity: int
    """Total resting shares on this side."""

    notional: float
    """Σ price·quantity for resting orders on this side."""


class MarketOutcomeRestingOrdersBids(BaseModel):
    count: int
    """Number of open maker orders on this side."""

    quantity: int
    """Total resting shares on this side."""

    notional: float
    """Σ price·quantity for resting orders on this side."""


class MarketOutcomeRestingOrders(BaseModel):
    bids: MarketOutcomeRestingOrdersBids

    asks: MarketOutcomeRestingOrdersAsks


class MarketOutcomeMarkToMarket(BaseModel):
    valuation_price: Optional[float] = FieldInfo(alias="valuationPrice", default=None)
    """Tournament valuation (YES) price; null when unavailable."""

    market_value: Optional[float] = FieldInfo(alias="marketValue", default=None)
    """Current liquidation value of the net position; null when valuation is missing."""

    unrealized_pnl: Optional[float] = FieldInfo(alias="unrealizedPnl", default=None)
    """Mark-to-market equity: marketValue + netCash. Null when valuation is missing."""

    valuation_missing: bool = FieldInfo(alias="valuationMissing")
    """True when no valuation price was available for the outcome."""


class MarketOutcomeInventory(BaseModel):
    quantity: int
    """Signed net YES inventory reconstructed from the maker's filled trades: positive = net long YES shares, negative = net short YES shares the maker sold."""

    side: Literal["LONG", "SHORT", "FLAT"]

    net_cash: float = FieldInfo(alias="netCash")
    """Net cash from the maker's trades on this outcome: positive = net received, negative = net paid."""


class MarketOutcome(BaseModel):
    exchange_id: str = FieldInfo(alias="exchangeId")

    option: str

    inventory: MarketOutcomeInventory

    mark_to_market: MarketOutcomeMarkToMarket = FieldInfo(alias="markToMarket")

    resting_orders: MarketOutcomeRestingOrders = FieldInfo(alias="restingOrders")

    worst_case: MarketOutcomeWorstCase = FieldInfo(alias="worstCase")


class Market(BaseModel):
    market_id: str = FieldInfo(alias="marketId")

    market_title: str = FieldInfo(alias="marketTitle")

    settled: bool

    mutually_exclusive: bool = FieldInfo(alias="mutuallyExclusive")
    """True when exactly one outcome of this market settles YES (native/binary markets). False for independent (imported range) markets where each outcome resolves YES/NO on its own. Determines how worstCaseLoss is computed."""

    worst_case_loss: float = FieldInfo(alias="worstCaseLoss")
    """True worst-case settlement loss for this market. For mutually-exclusive markets it accounts for the fact that exactly one outcome settles YES (so held outcomes can't all lose at once). For independent (range) markets it is the sum of every outcome taking its own worse side, since they can all settle NO together."""

    outcomes: List[MarketOutcome]


class Tournament(BaseModel):
    slug: str

    id: str

    name: str


class DmmInventory(BaseModel):
    tournament: Tournament

    as_of: str = FieldInfo(alias="asOf")

    markets: List[Market]

    summary: Summary
