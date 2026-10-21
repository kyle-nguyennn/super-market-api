# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DesignatedMarketMakerFailedSettlementRow"]


class DesignatedMarketMakerFailedSettlementRow(BaseModel):
    contract_id: str = FieldInfo(alias="contractId")

    market_id: str = FieldInfo(alias="marketId")

    market_title: str = FieldInfo(alias="marketTitle")

    contract_title: Optional[str] = FieldInfo(alias="contractTitle", default=None)
    """Title of the failed contract/node inside the market tree. Useful for composite or multi-leg markets."""

    contract_type: str = FieldInfo(alias="contractType")
    """Autosettleable contract type that produced the failure."""

    contract_details: Optional[Dict[str, object]] = FieldInfo(alias="contractDetails", default=None)
    """Raw contract details for the failed node, included so operators can identify the exact external event or metric before manually resolving."""

    is_range_settlement: bool = FieldInfo(alias="isRangeSettlement")
    """True for Kalshi range imports, where each settlement option must be manually resolved as YES or NO instead of choosing a single winning option."""

    settlement_options: List[str] = FieldInfo(alias="settlementOptions")
    """Valid outcomes for this contract — supply one of these when calling the settle-node endpoint to manually resolve."""

    settlement_error: Optional[str] = FieldInfo(alias="settlementError", default=None)

    settlement_retry_count: int = FieldInfo(alias="settlementRetryCount")

    last_check_attempt: Optional[str] = FieldInfo(alias="lastCheckAttempt", default=None)

    settlement_date: Optional[str] = FieldInfo(alias="settlementDate", default=None)

    is_abandoned: bool = FieldInfo(alias="isAbandoned")
    """True once retry count reaches the autosettler cap (12). The contract will no longer be picked up by cron — only manual resolution will clear it."""
