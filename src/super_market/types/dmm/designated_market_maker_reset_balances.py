# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DesignatedMarketMakerResetBalances"]


class DesignatedMarketMakerResetBalances(BaseModel):
    success: bool

    tournament_id: str = FieldInfo(alias="tournamentId")

    slug: str

    cancelled_user_orders: int = FieldInfo(alias="cancelledUserOrders")

    closed_maker_orders: int = FieldInfo(alias="closedMakerOrders")

    deleted_holdings: int = FieldInfo(alias="deletedHoldings")

    deleted_position_lots: int = FieldInfo(alias="deletedPositionLots")

    reset_members: int = FieldInfo(alias="resetMembers")

    deleted_portfolio_snapshots: int = FieldInfo(alias="deletedPortfolioSnapshots")

    replayed: Optional[bool] = None
    """True when the stored response from a completed reset is replayed."""
