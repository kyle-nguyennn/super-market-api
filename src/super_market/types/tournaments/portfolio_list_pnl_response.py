# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PortfolioListPnlResponse"]


class PortfolioListPnlResponse(BaseModel):
    period: Literal["day", "week", "month", "quarter", "year", "all"]

    period_start: Optional[str] = FieldInfo(alias="periodStart", default=None)

    period_end: str = FieldInfo(alias="periodEnd")

    period_pnl: Optional[float] = FieldInfo(alias="periodPnl", default=None)
    """P&L since the period-start baseline. Null for `all` and when no baseline exists."""

    unrealized_pnl: float = FieldInfo(alias="unrealizedPnl")

    total_account_value: float = FieldInfo(alias="totalAccountValue")

    total_holdings_value: float = FieldInfo(alias="totalHoldingsValue")

    total_cost_basis: float = FieldInfo(alias="totalCostBasis")

    roi: Optional[float] = None
    """Percentage return vs the initial virtual balance (`all`) or vs the period-start baseline (other periods)."""

    sharpe: Optional[float] = None
    """Annualized by √252 from daily returns; null without usable variance."""
