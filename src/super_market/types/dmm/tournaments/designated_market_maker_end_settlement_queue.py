# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

from .designated_market_maker_end_settlement_lifecycle_summary import DesignatedMarketMakerEndSettlementLifecycleSummary
from .designated_market_maker_end_settlement_attempt_summary import DesignatedMarketMakerEndSettlementAttemptSummary

__all__ = ["DesignatedMarketMakerEndSettlementQueue", "Links"]


class Links(BaseModel):
    status: str

    preview: str


class DesignatedMarketMakerEndSettlementQueue(BaseModel):
    status: Literal["accepted", "already_active"]

    queued: bool

    reason: Optional[Literal["already_queued", "already_running", "already_active"]] = None

    tournament_id: str = FieldInfo(alias="tournamentId")

    slug: str

    settlement: DesignatedMarketMakerEndSettlementLifecycleSummary

    attempt: DesignatedMarketMakerEndSettlementAttemptSummary

    event_ids: Optional[List[str]] = FieldInfo(alias="eventIds", default=None)

    links: Links
