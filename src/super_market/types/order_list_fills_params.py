# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["OrderListFillsParams"]


class OrderListFillsParams(TypedDict, total=False):
    limit: int
    """Fills per page (max 200)."""

    cursor: str
    """Opaque pagination cursor from a previous response."""
