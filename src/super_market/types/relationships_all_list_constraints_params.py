# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["RelationshipsAllListConstraintsParams"]


class RelationshipsAllListConstraintsParams(TypedDict, total=False):
    market_id: Annotated[str, PropertyInfo(alias="marketId")]
    """Optionally restrict evaluations to relationships touching this accessible market."""

    relationship_id: Annotated[str, PropertyInfo(alias="relationshipId")]
    """Return the engine evaluation for one accessible canonical relationship."""

    violations_only: Annotated[Literal["true", "false"], PropertyInfo(alias="violationsOnly")]

    min_violation: Annotated[Optional[float], PropertyInfo(alias="minViolation")]

    tournament_id: Annotated[str, PropertyInfo(alias="tournamentId")]
    """Evaluate or read relationships in one accessible tournament context. Omit for the API key's default context: the public context for an unbound key, or the organization's default tournament for an organization-bound key."""
