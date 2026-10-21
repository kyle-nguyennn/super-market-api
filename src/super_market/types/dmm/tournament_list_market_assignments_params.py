# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TournamentListMarketAssignmentsParams"]


class TournamentListMarketAssignmentsParams(TypedDict, total=False):
    limit: int
    """Page size (default 50, max 200)."""

    cursor: str
    """Opaque pagination cursor from a prior response. It marks the last row served rather than a row offset, so rows added or removed between pages neither repeat a row nor hide an unseen one."""
