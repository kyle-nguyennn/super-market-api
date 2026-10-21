# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PositionLot"]


class PositionLot(BaseModel):
    lot_id: str = FieldInfo(alias="lotId")

    side: str

    quantity: float

    entry_price: float = FieldInfo(alias="entryPrice")

    opened_at: str = FieldInfo(alias="openedAt")
