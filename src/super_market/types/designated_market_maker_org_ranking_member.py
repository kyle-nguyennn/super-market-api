# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .designated_market_maker_ranking_member import DesignatedMarketMakerRankingMember

__all__ = ["DesignatedMarketMakerOrgRankingMember"]


class DesignatedMarketMakerOrgRankingMember(DesignatedMarketMakerRankingMember):
    org_role: str = FieldInfo(alias="orgRole")
    """Organization role: `owner`, `admin`, or `member`."""
