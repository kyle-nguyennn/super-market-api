# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from .._models import BaseModel

from .market import Market
from .pagination import Pagination

__all__ = ["MarketListResponse"]


class MarketListResponse(BaseModel):
    data: List[Market]

    pagination: Pagination
