# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DesignatedMarketMakerTransaction"]


class DesignatedMarketMakerTransaction(BaseModel):
    id: str

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    profile_id: str = FieldInfo(alias="profileId")

    username: Optional[str] = None

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    email: Optional[str] = None

    transaction_type: str = FieldInfo(alias="transactionType")
    """Economic entry type, including nominal trades and ALL_COLLATERAL_ADVANCE, ALL_COLLATERAL_REPAYMENT, or ALL_COLLATERAL_RELEASE adjustments."""

    amount: float

    balance_after: Optional[float] = FieldInfo(alias="balanceAfter", default=None)
    """Cash balance after a MONEY entry, or outstanding advance after a COLLATERAL entry."""

    asset_type: str = FieldInfo(alias="assetType")
    """MONEY, HOLDINGS, or COLLATERAL."""

    market_id: Optional[str] = FieldInfo(alias="marketId", default=None)

    settlement_option: Optional[str] = FieldInfo(alias="settlementOption", default=None)
