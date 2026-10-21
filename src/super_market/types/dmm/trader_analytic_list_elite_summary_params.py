# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TraderAnalyticListEliteSummaryParams"]


class TraderAnalyticListEliteSummaryParams(TypedDict, total=False):
    tournament_id: Annotated[str, PropertyInfo(alias="tournamentId")]

    market_type: Annotated[str, PropertyInfo(alias="marketType")]

    organization_slug: Annotated[str, PropertyInfo(alias="organizationSlug")]
