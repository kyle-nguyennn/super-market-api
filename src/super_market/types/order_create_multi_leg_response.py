# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List

from .._models import BaseModel

from .multi_leg_order_data import MultiLegOrderData

__all__ = ["OrderCreateMultiLegResponse", "Result"]


class Result(BaseModel):
    index: int

    data: MultiLegOrderData


class OrderCreateMultiLegResponse(BaseModel):
    results: List[Result]
