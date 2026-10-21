# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DesignatedMarketMakerSettlementOverrideMemberPreview"]


class DesignatedMarketMakerSettlementOverrideMemberPreview(BaseModel):
    profile_id: str = FieldInfo(alias="profileId")

    username: Optional[str] = None

    settled_quantity: float = FieldInfo(alias="settledQuantity")

    previous_payout: float = FieldInfo(alias="previousPayout")

    corrected_payout: float = FieldInfo(alias="correctedPayout")

    delta: float
    """Signed balance adjustment that execute will apply for this member."""
