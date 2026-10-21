# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["RelationshipsAllListGraphParams"]


class RelationshipsAllListGraphParams(TypedDict, total=False):
    market_id: Required[Annotated[str, PropertyInfo(alias="marketId")]]
    """Accessible market whose exchanges seed the graph traversal."""

    depth: int

    tournament_id: Annotated[str, PropertyInfo(alias="tournamentId")]
    """Evaluate or read relationships in one accessible tournament context. Omit for the API key's default context: the public context for an unbound key, or the organization's default tournament for an organization-bound key."""
