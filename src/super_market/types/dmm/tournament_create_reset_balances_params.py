# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TournamentCreateResetBalancesParams"]


class TournamentCreateResetBalancesParams(TypedDict, total=False):
    confirm: Required[str]
    """Must match the path `slug` exactly. Guards against accidental destructive calls."""

    reset_key: Required[Annotated[str, PropertyInfo(alias="resetKey")]]
    """Required stable client retry key. Reuse the same value after a timeout or `503 TX_CONFLICT`; a committed reset is replayed and an interrupted reset is resumed."""
