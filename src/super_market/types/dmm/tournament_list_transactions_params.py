# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TournamentListTransactionsParams"]


class TournamentListTransactionsParams(TypedDict, total=False):
    from_: Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]
    """Inclusive lower bound on the row timestamp (ISO-8601 UTC)."""

    to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Inclusive upper bound on the row timestamp (ISO-8601 UTC)."""

    limit: int

    cursor: str
    """Opaque time cursor returned as `nextCursor` by a prior page."""
