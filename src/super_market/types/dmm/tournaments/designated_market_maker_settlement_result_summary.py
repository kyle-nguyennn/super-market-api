# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DesignatedMarketMakerSettlementResultSummary"]


class DesignatedMarketMakerSettlementResultSummary(BaseModel):
    settled_at: Optional[str] = FieldInfo(alias="settledAt", default=None)

    trigger: Optional[Literal["automation", "platform_admin", "dmm_operator"]] = None

    triggered_by: Optional[str] = FieldInfo(alias="triggeredBy", default=None)
    """DMM responses redact API-key identifiers and platform-admin profile identifiers."""

    positions_settled: int = FieldInfo(alias="positionsSettled")

    members_affected: int = FieldInfo(alias="membersAffected")

    open_orders_cancelled: int = FieldInfo(alias="openOrdersCancelled")

    final_snapshot_status: Literal["refreshed", "failed", "skipped"] = FieldInfo(alias="finalSnapshotStatus")
