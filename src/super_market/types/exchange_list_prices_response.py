# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .bulk_exchange_price import BulkExchangePrice

__all__ = ["ExchangeListPricesResponse"]


class ExchangeListPricesResponse(BaseModel):
    data: List[BulkExchangePrice]

    missing_ids: List[str] = FieldInfo(alias="missingIds")
    """Requested exchange IDs that were not found or not in scope."""
