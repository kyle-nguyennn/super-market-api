# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from .dmm_trader_analytics_top_performer import DmmTraderAnalyticsTopPerformer

__all__ = ["DmmTraderAnalyticsEliteSummary", "Scope", "Thresholds", "ThresholdsComponentWeights", "Cohort"]


class Cohort(BaseModel):
    size: int

    mean_smart_score_decayed: Optional[float] = FieldInfo(alias="meanSmartScoreDecayed", default=None)

    min_smart_score_decayed: Optional[float] = FieldInfo(alias="minSmartScoreDecayed", default=None)

    max_smart_score_decayed: Optional[float] = FieldInfo(alias="maxSmartScoreDecayed", default=None)


class ThresholdsComponentWeights(BaseModel):
    pnl: float

    win_rate: float = FieldInfo(alias="winRate")

    roi: float

    sharpe: float


class Thresholds(BaseModel):
    minimum_elite_score: float = FieldInfo(alias="minimumEliteScore")

    elite_percentage: float = FieldInfo(alias="elitePercentage")

    minimum_trade_count: float = FieldInfo(alias="minimumTradeCount")

    minimum_stake: float = FieldInfo(alias="minimumStake")

    component_weights: ThresholdsComponentWeights = FieldInfo(alias="componentWeights")

    time_decay_factor: float = FieldInfo(alias="timeDecayFactor")


class Scope(BaseModel):
    market_type: str = FieldInfo(alias="marketType")

    organization_id: str = FieldInfo(alias="organizationId")

    organization_slug: Optional[str] = FieldInfo(alias="organizationSlug", default=None)

    tournament_id: Optional[str] = FieldInfo(alias="tournamentId", default=None)

    tournament_slug: Optional[str] = FieldInfo(alias="tournamentSlug", default=None)


class DmmTraderAnalyticsEliteSummary(BaseModel):
    scope: Scope

    latest_elite_cut_as_of: Optional[str] = FieldInfo(alias="latestEliteCutAsOf", default=None)

    thresholds: Thresholds

    cohort: Cohort

    top_performers: List[DmmTraderAnalyticsTopPerformer] = FieldInfo(alias="topPerformers")
