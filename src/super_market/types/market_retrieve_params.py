# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MarketRetrieveParams"]


class MarketRetrieveParams(TypedDict, total=False):
    tournament_id: Annotated[str, PropertyInfo(alias="tournamentId")]
    """Optional explicit tournament UUID. Omit for the API key's public or organization-wide default scope."""
