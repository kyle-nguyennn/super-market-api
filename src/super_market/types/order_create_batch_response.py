# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, List

from .._models import BaseModel

__all__ = ["OrderCreateBatchResponse", "Result"]


class Result(BaseModel):
    index: int

    ok: bool

    status: int

    data: Dict[str, object]


class OrderCreateBatchResponse(BaseModel):
    results: List[Result]
