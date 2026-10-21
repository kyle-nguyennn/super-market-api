# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PortfolioCollateral"]


class PortfolioCollateral(BaseModel):
    profile_id: str = FieldInfo(alias="profileId")

    tournament_id: Optional[str] = FieldInfo(alias="tournamentId", default=None)
    """Null for the global trading scope."""

    outstanding_advance: float = FieldInfo(alias="outstandingAdvance")

    component_id: str = FieldInfo(alias="componentId")

    covered_exchange_ids: List[int] = FieldInfo(alias="coveredExchangeIds")

    relationship_ids: List[str] = FieldInfo(alias="relationshipIds")

    guaranteed_payout_floor: Optional[float] = FieldInfo(alias="guaranteedPayoutFloor", default=None)
    """Minimum component payout when the engine can evaluate every allowed joint outcome; null when unavailable."""

    diagnostic: Optional[str] = None
