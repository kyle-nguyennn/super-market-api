# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TournamentListParams"]


class TournamentListParams(TypedDict, total=False):
    organization_slug: Annotated[str, PropertyInfo(alias="organizationSlug")]
    """Filter to a single organization's tournaments."""

    archived: Literal["active", "archived", "all"]
    """Select active tournaments (default), archived tournaments, or all tournaments."""

    limit: int

    cursor: str
    """Opaque pagination cursor from a prior response."""
