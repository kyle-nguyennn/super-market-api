# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MarketCreate"]


class MarketCreate(BaseModel):
    message: str

    market_id: float = FieldInfo(alias="marketId")
