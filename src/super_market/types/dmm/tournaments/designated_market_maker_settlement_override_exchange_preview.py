# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

from .designated_market_maker_settlement_override_member_preview import (
    DesignatedMarketMakerSettlementOverrideMemberPreview,
)

__all__ = ["DesignatedMarketMakerSettlementOverrideExchangePreview"]


class DesignatedMarketMakerSettlementOverrideExchangePreview(BaseModel):
    exchange_id: str = FieldInfo(alias="exchangeId")

    market_id: str = FieldInfo(alias="marketId")

    market_title: str = FieldInfo(alias="marketTitle")

    settlement_option: str = FieldInfo(alias="settlementOption")

    previous_price: float = FieldInfo(alias="previousPrice")

    corrected_price: float = FieldInfo(alias="correctedPrice")

    members_affected: int = FieldInfo(alias="membersAffected")

    total_credited: float = FieldInfo(alias="totalCredited")

    total_debited: float = FieldInfo(alias="totalDebited")

    net_delta: float = FieldInfo(alias="netDelta")

    members: List[DesignatedMarketMakerSettlementOverrideMemberPreview]
