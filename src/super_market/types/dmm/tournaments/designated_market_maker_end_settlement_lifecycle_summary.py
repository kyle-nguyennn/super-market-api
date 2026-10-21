# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

from .designated_market_maker_settlement_actor import DesignatedMarketMakerSettlementActor
from .designated_market_maker_settlement_result_summary import DesignatedMarketMakerSettlementResultSummary

__all__ = ["DesignatedMarketMakerEndSettlementLifecycleSummary"]


class DesignatedMarketMakerEndSettlementLifecycleSummary(BaseModel):
    status: Literal[
        "pending", "settling", "blocked_missing_valuation", "settled", "failed", "awaiting_market_resolution"
    ]

    derived: bool

    active_attempt_id: Optional[str] = FieldInfo(alias="activeAttemptId", default=None)

    trigger: Optional[Literal["automation", "platform_admin", "dmm_operator"]] = None

    actor: Optional[DesignatedMarketMakerSettlementActor] = None

    locked_until: Optional[str] = FieldInfo(alias="lockedUntil", default=None)

    settled_at: Optional[str] = FieldInfo(alias="settledAt", default=None)

    result: Optional[DesignatedMarketMakerSettlementResultSummary] = None
