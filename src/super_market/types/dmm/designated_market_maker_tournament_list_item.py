# File generated from our OpenAPI spec by Scalar. See README.md for details.
# pyright: reportIncompatibleVariableOverride=false

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .designated_market_maker_tournament import DesignatedMarketMakerTournament

__all__ = ["DesignatedMarketMakerTournamentListItem"]


class DesignatedMarketMakerTournamentListItem(DesignatedMarketMakerTournament):
    updated_at: str = FieldInfo(alias="updatedAt")

    status: Literal["draft", "active", "ended"]

    member_count: int = FieldInfo(alias="memberCount")

    market_count: int = FieldInfo(alias="marketCount")
