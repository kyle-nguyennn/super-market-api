# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DesignatedMarketMakerRelationshipOperationStatus", "Data"]


class Data(BaseModel):
    operation_id: str = FieldInfo(alias="operationId")

    kind: Literal["create", "disable"]

    status: Literal["pending", "succeeded", "failed"]

    relationship_id: Optional[str] = FieldInfo(alias="relationshipId", default=None)
    """Canonical relationship UUID when one is available."""

    engine_status: Optional[int] = FieldInfo(alias="engineStatus", default=None)
    """Trading-engine HTTP status after a terminal attempt."""

    error: Optional[str] = None
    """Most recent failure detail when available."""

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")


class DesignatedMarketMakerRelationshipOperationStatus(BaseModel):
    data: Data
