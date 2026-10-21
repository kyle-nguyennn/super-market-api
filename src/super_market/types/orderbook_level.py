# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["OrderbookLevel"]


class OrderbookLevel(BaseModel):
    price: float

    quantity: float
