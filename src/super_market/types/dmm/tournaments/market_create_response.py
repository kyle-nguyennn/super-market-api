# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["MarketCreateResponse"]


class MarketCreateResponse(BaseModel):
    market_id: str = FieldInfo(alias="marketId")

    title: str
