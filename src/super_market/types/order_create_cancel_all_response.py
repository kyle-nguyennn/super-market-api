# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["OrderCreateCancelAllResponse"]


class OrderCreateCancelAllResponse(BaseModel):
    cancelled: int
    """Orders this request cancelled."""
