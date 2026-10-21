# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OrderDeleteResponse"]


class OrderDeleteResponse(BaseModel):
    order_id: int = FieldInfo(alias="orderId")

    tournament_id: Optional[str] = FieldInfo(alias="tournamentId", default=None)
    """Tournament the order belonged to, or null for global orders."""

    message: str
