# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TournamentTransaction"]


class TournamentTransaction(BaseModel):
    event_id: str

    event_type: Literal["trade", "settlement", "deposit", "fee", "market_creation"]

    created_at: str = FieldInfo(alias="createdAt")

    price: Optional[float] = None
    """Trades: execution price per share. Settlement events: legacy entries report the average entry price; engine-recorded entries report the payout per share (null when nothing was paid). Null for other events."""

    quantity: float

    exchange_id: Optional[str] = FieldInfo(alias="exchangeId", default=None)

    market_id: Optional[str] = FieldInfo(alias="marketId", default=None)

    settlement_option: Optional[str] = FieldInfo(alias="settlementOption", default=None)

    current_price: Optional[float] = FieldInfo(alias="currentPrice", default=None)

    market_title: str = FieldInfo(alias="marketTitle")
    """Market title, or a placeholder when the event has no market: `Account Activity` for engine-recorded events (trades included); legacy rows use `Unknown Market` for trades and `Account Activity` otherwise."""

    market_image: Optional[str] = FieldInfo(alias="marketImage", default=None)
    """Market header image URL, or null."""

    order_type: Optional[str] = FieldInfo(alias="orderType", default=None)

    contract_type: Optional[str] = FieldInfo(alias="contractType", default=None)

    description: Optional[str] = None

    amount: Optional[float] = None
    """Balance change for non-trade events; ALL collateral events report the collateral change (`collateralDelta`). Null for trades."""

    cost_basis: Optional[float] = FieldInfo(alias="costBasis", default=None)
    """Legacy settlement events only: the position's cost basis from settlement metadata. Absent on engine-recorded events."""

    settlement_type: Optional[str] = FieldInfo(alias="settlementType", default=None)
    """Legacy non-trade events only: the settlement type from transaction metadata, when recorded. Absent on engine-recorded events."""

    transaction_type: Optional[str] = FieldInfo(alias="transactionType", default=None)
    """Authoritative transaction name, including ALL_COLLATERAL_ADVANCE, ALL_COLLATERAL_REPAYMENT, and ALL_COLLATERAL_RELEASE."""

    outstanding_advance_after: Optional[float] = FieldInfo(alias="outstandingAdvanceAfter", default=None)
    """Outstanding component advance after an ALL collateral event; null for other events."""

    component_id: Optional[str] = FieldInfo(alias="componentId", default=None)
    """ALL relationship component identifier for collateral events."""

    reason: Optional[str] = None
    """Engine reason for a collateral event."""

    tournament_id: Optional[str] = FieldInfo(alias="tournamentId", default=None)
    """The tournament this event belongs to."""
