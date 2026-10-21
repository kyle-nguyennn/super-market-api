# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

from .designated_market_maker_settlement_override_exchange_preview import (
    DesignatedMarketMakerSettlementOverrideExchangePreview,
)
from .designated_market_maker_settlement_override_summary import DesignatedMarketMakerSettlementOverrideSummary

__all__ = ["DesignatedMarketMakerSettlementOverridePreview"]


class DesignatedMarketMakerSettlementOverridePreview(BaseModel):
    tournament_id: str = FieldInfo(alias="tournamentId")

    slug: str

    snapshot_date: str = FieldInfo(alias="snapshotDate")
    """Tournament end date used when refreshing downstream tournament portfolio snapshots."""

    reason: str

    exchanges: List[DesignatedMarketMakerSettlementOverrideExchangePreview]

    summary: DesignatedMarketMakerSettlementOverrideSummary
