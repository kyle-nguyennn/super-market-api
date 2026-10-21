# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from .tournament_portfolio_position import TournamentPortfolioPosition

__all__ = ["PortfolioListPositionsResponse", "Summary"]


class Summary(BaseModel):
    total_market_value: float = FieldInfo(alias="totalMarketValue")

    total_cost_basis: float = FieldInfo(alias="totalCostBasis")

    total_unrealized_pnl: float = FieldInfo(alias="totalUnrealizedPnl")


class PortfolioListPositionsResponse(BaseModel):
    positions: List[TournamentPortfolioPosition]

    summary: Summary
