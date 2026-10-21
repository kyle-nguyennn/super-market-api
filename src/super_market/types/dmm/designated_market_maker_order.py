# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DesignatedMarketMakerOrder"]


class DesignatedMarketMakerOrder(BaseModel):
    id: int

    created_at: str = FieldInfo(alias="createdAt")

    profile_id: Optional[str] = FieldInfo(alias="profileId", default=None)

    username: Optional[str] = None

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    email: Optional[str] = None

    market_id: str = FieldInfo(alias="marketId")

    market_title: str = FieldInfo(alias="marketTitle")

    settlement_option: str = FieldInfo(alias="settlementOption")

    order_type: Optional[str] = FieldInfo(alias="orderType", default=None)

    price_limit: float = FieldInfo(alias="priceLimit")

    quantity: int

    open: bool

    expiration_date: Optional[str] = FieldInfo(alias="expirationDate", default=None)
