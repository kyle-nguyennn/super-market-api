# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PortfolioListCollateralParams"]


class PortfolioListCollateralParams(TypedDict, total=False):
    tournament_id: Annotated[str, PropertyInfo(alias="tournamentId")]
    """Return collateral from one accessible tournament. Omit to use the organization's default tournament for an organization-bound key or the public global context for an unbound key."""
