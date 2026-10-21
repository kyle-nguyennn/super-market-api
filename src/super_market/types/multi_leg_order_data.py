# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .all_execution_economics import AllExecutionEconomics

__all__ = ["MultiLegOrderData", "All"]


class All(BaseModel):
    full_notional_cost: float = FieldInfo(alias="fullNotionalCost")
    """Nominal cost of the filled shares before relationship-backed collateral savings."""

    effective_entry_cost: float = FieldInfo(alias="effectiveEntryCost")
    """Cash actually debited for the new fill after applying an eligible ALL collateral advance."""

    collateral_savings: float = FieldInfo(alias="collateralSavings")
    """Part of the nominal fill cost backed by the portfolio's guaranteed payout floor instead of cash."""

    relationship_ids: List[str] = FieldInfo(alias="relationshipIds")

    component_id: Optional[str] = FieldInfo(alias="componentId", default=None)
    """Opaque identifier for the connected relationship component used by the collateral calculation."""

    guaranteed_payout_floor_after: float = FieldInfo(alias="guaranteedPayoutFloorAfter")
    """Minimum payout guaranteed by the linked portfolio after this execution."""

    outstanding_advance_after: float = FieldInfo(alias="outstandingAdvanceAfter")
    """Relationship-backed collateral advance still encumbering this component after execution."""

    collateral_repayment: float = FieldInfo(alias="collateralRepayment")
    """Advance repaid by this execution because it reduced the component's guaranteed backing."""

    net_buying_power_impact: float = FieldInfo(alias="netBuyingPowerImpact")
    """Positive consumes buying power, negative releases buying power, and zero is neutral."""


class MultiLegOrderData(BaseModel):
    order_id: Optional[int] = FieldInfo(alias="orderId", default=None)

    exchange_id: str = FieldInfo(alias="exchangeId")

    open: bool
    """True if the leg is resting on the book; false if fully filled."""

    remaining_quantity: Optional[float] = FieldInfo(alias="remainingQuantity", default=None)
    """Engine-authoritative unfilled quantity after admission resizing. Present for engine-routed orders."""

    action: Optional[Literal["buy", "sell"]] = None
    """Canonical engine action. Present for engine-routed legs; may differ from the requested action when a sell is converted to its complement buy."""

    side: Optional[Literal["yes", "no"]] = None
    """Canonical engine outcome side. Present for engine-routed legs."""

    price: Optional[float] = None
    """Canonical engine limit price in side-relative terms. Present for engine-routed legs."""

    quantity: Optional[int] = None
    """Canonical engine quantity as a positive integer. Present for engine-routed legs."""

    terminal_reason_code: Optional[str] = FieldInfo(alias="terminalReasonCode", default=None)
    """Canonical terminal reason, including SelfTradePrevented, or null when the leg has no terminal reason. Present for engine-routed legs."""

    quantity_traded: float = FieldInfo(alias="quantityTraded")

    total_cost: float = FieldInfo(alias="totalCost")

    fill_price: Optional[float] = FieldInfo(alias="fillPrice", default=None)
    """Price of the leg's last fill, or null when nothing filled (`quantityTraded` is 0)."""

    all: All
