# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DesignatedMarketMakerSettlementOverrideSummary"]


class DesignatedMarketMakerSettlementOverrideSummary(BaseModel):
    exchanges: int

    members_affected: int = FieldInfo(alias="membersAffected")

    total_credited: float = FieldInfo(alias="totalCredited")

    total_debited: float = FieldInfo(alias="totalDebited")

    net_delta: float = FieldInfo(alias="netDelta")
