# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AllExecutionEconomics"]


class AllExecutionEconomics(BaseModel):
    """Authoritative ALL execution economics, or null when no engine relationship quote was produced."""

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
