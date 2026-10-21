# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExchangeListPricesParams"]


class ExchangeListPricesParams(TypedDict, total=False):
    ids: Required[str]
    """Required. Comma-separated list of exchange IDs (max 100)."""

    tournament_id: Annotated[str, PropertyInfo(alias="tournamentId")]
    """When provided, returns quotes from that accessible tournament. Omit for the organization's default tournament with an organization-bound key or public-global quotes with an unbound key. Exchanges outside the resolved context are reported in `missingIds`."""
