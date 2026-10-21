# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

from .dmm.all_relationship_type import AllRelationshipType

__all__ = ["RelationshipsAllListRelationshipsParams"]


class RelationshipsAllListRelationshipsParams(TypedDict, total=False):
    market_id: Annotated[str, PropertyInfo(alias="marketId")]
    """Return relationships touching any exchange in this accessible market."""

    exchange_id: Annotated[str, PropertyInfo(alias="exchangeId")]
    """Return relationships touching this accessible exchange."""

    type: AllRelationshipType

    depth: int

    limit: int

    cursor: str

    tournament_id: Annotated[str, PropertyInfo(alias="tournamentId")]
    """Evaluate or read relationships in one accessible tournament context. Omit for the API key's default context: the public context for an unbound key, or the organization's default tournament for an organization-bound key."""
