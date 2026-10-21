# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .order import Order
from .order_pagination import OrderPagination

__all__ = ["OrderListResponse", "Coverage"]


class Coverage(BaseModel):
    complete: Literal[True]
    """Always true because cursor pagination exposes the complete order history without window truncation."""

    projected_through_sequence: Optional[int] = FieldInfo(alias="projectedThroughSequence", default=None)
    """Latest trading-engine sequence reflected by the reporting projection, or null when no checkpoint exists."""


class OrderListResponse(BaseModel):
    data: List[Order]

    pagination: OrderPagination

    coverage: Optional[Coverage] = None
    """Reporting projection coverage metadata for engine-backed history."""
