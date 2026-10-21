# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExchangeListOrderbookParams"]


class ExchangeListOrderbookParams(TypedDict, total=False):
    depth: int
    """Maximum number of price levels per side (max 200)."""

    tournament_id: Annotated[str, PropertyInfo(alias="tournamentId")]
    """Tournament UUID returned as `id` by `GET /tournaments/{slug}`. When provided, returns only orders belonging to that tournament's isolated orderbook."""
