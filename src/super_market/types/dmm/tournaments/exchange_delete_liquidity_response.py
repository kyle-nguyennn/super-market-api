# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ExchangeDeleteLiquidityResponse"]


class ExchangeDeleteLiquidityResponse(BaseModel):
    exchange_id: str = FieldInfo(alias="exchangeId")

    swept_orders: int = FieldInfo(alias="sweptOrders")
    """Count of market_maker-owned open orders cancelled."""
