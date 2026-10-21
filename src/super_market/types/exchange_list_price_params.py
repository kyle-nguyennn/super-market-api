# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExchangeListPriceParams"]


class ExchangeListPriceParams(TypedDict, total=False):
    tournament_id: Annotated[str, PropertyInfo(alias="tournamentId")]
    """Tournament UUID returned as `id` by `GET /tournaments/{slug}`. When provided, returns the tournament-specific latest price and computes best bid/ask from that tournament's isolated orderbook."""
