# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

from .designated_market_maker_settlement_status_attempt import DesignatedMarketMakerSettlementStatusAttempt
from .designated_market_maker_settlement_actor import DesignatedMarketMakerSettlementActor
from .designated_market_maker_missing_settlement_valuation import DesignatedMarketMakerMissingSettlementValuation
from .designated_market_maker_settlement_result_summary import DesignatedMarketMakerSettlementResultSummary
from .designated_market_maker_settlement_error_summary import DesignatedMarketMakerSettlementErrorSummary

__all__ = [
    "DesignatedMarketMakerSettlementStatus",
    "ActiveAttempt",
    "Retry",
    "Blocked",
    "Awaiting",
    "AwaitingUnresolvedMarket",
    "Actions",
]


class Actions(BaseModel):
    can_queue: bool = FieldInfo(alias="canQueue")

    can_submit_prices: bool = FieldInfo(alias="canSubmitPrices")

    can_retry: bool = FieldInfo(alias="canRetry")

    can_override_settlement: bool = FieldInfo(alias="canOverrideSettlement")


class AwaitingUnresolvedMarket(BaseModel):
    market_id: str = FieldInfo(alias="marketId")

    market_title: str = FieldInfo(alias="marketTitle")


class Awaiting(BaseModel):
    unresolved_markets: List[AwaitingUnresolvedMarket] = FieldInfo(alias="unresolvedMarkets")


class Blocked(BaseModel):
    missing_valuations: List[DesignatedMarketMakerMissingSettlementValuation] = FieldInfo(alias="missingValuations")


class Retry(BaseModel):
    automated_attempt_count: int = FieldInfo(alias="automatedAttemptCount")

    max_automated_attempts: int = FieldInfo(alias="maxAutomatedAttempts")

    next_retry_at: Optional[str] = FieldInfo(alias="nextRetryAt", default=None)


class ActiveAttempt(BaseModel):
    id: str

    locked_until: Optional[str] = FieldInfo(alias="lockedUntil", default=None)


class DesignatedMarketMakerSettlementStatus(BaseModel):
    tournament_id: str = FieldInfo(alias="tournamentId")

    slug: str

    status: Literal[
        "pending", "settling", "blocked_missing_valuation", "settled", "failed", "awaiting_market_resolution"
    ]

    derived: bool

    active_attempt: Optional[ActiveAttempt] = FieldInfo(alias="activeAttempt", default=None)

    trigger: Optional[Literal["automation", "platform_admin", "dmm_operator"]] = None

    actor: Optional[DesignatedMarketMakerSettlementActor] = None

    retry: Retry

    blocked: Optional[Blocked] = None

    awaiting: Optional[Awaiting] = None
    """Present while a `resolved_outcomes` tournament waits for every attached market to settle; empty once the closeout is queued."""

    result: Optional[DesignatedMarketMakerSettlementResultSummary] = None

    last_error: Optional[DesignatedMarketMakerSettlementErrorSummary] = FieldInfo(alias="lastError", default=None)

    attempts: List[DesignatedMarketMakerSettlementStatusAttempt]

    actions: Actions
