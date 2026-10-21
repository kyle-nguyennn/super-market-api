# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DesignatedMarketMakerRelationshipPendingOperation", "Data"]


class Data(BaseModel):
    operation_id: str = FieldInfo(alias="operationId")
    """Durable operation UUID to poll with GET /dmm/relationships/operations/{operationId}."""

    status: Literal["pending"]


class DesignatedMarketMakerRelationshipPendingOperation(BaseModel):
    data: Data
