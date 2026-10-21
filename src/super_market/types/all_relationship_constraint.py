# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .dmm.all_relationship_type import AllRelationshipType
from .all_relationship_corrective_trade import AllRelationshipCorrectiveTrade
from .all_relationship_observed_price import AllRelationshipObservedPrice
from .dmm.all_relationship_direction import AllRelationshipDirection
from .dmm.all_relationship_constraint_semantics import AllRelationshipConstraintSemantics

__all__ = ["AllRelationshipConstraint"]


class AllRelationshipConstraint(BaseModel):
    relationship_id: str = FieldInfo(alias="relationshipId")

    type: AllRelationshipType

    violation_amount: float = FieldInfo(alias="violationAmount")
    """Distance from the valid price bound. Zero for satisfied or unevaluable relationships."""

    reason: str

    suggested_corrective_trades: List[AllRelationshipCorrectiveTrade] = FieldInfo(alias="suggestedCorrectiveTrades")

    observed_prices: Optional[List[AllRelationshipObservedPrice]] = FieldInfo(alias="observedPrices", default=None)

    bound: Optional[float] = None

    lower_bound: Optional[float] = FieldInfo(alias="lowerBound", default=None)

    upper_bound: Optional[float] = FieldInfo(alias="upperBound", default=None)

    current_value: Optional[float] = FieldInfo(alias="currentValue", default=None)

    evaluation_status: Literal["satisfied", "violated", "unevaluable"] = FieldInfo(alias="evaluationStatus")

    diagnostic: Optional[str] = None

    tournament_id: Optional[str] = FieldInfo(alias="tournamentId", default=None)

    direction: AllRelationshipDirection

    constraint: AllRelationshipConstraintSemantics
