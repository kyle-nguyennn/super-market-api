# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TournamentListInventoryParams"]


class TournamentListInventoryParams(TypedDict, total=False):
    market: str
    """Optional market id. When provided, the snapshot is scoped to that single market instead of every market the maker has exposure on, and the `summary` totals reflect only that market. The market must belong to the tournament (otherwise 404). Omit to list all markets."""
