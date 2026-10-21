# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PortfolioListPnlResponse"]


class PortfolioListPnlResponse(BaseModel):
    period: Literal["day", "week", "month", "quarter", "year", "all"]

    period_start: Optional[str] = FieldInfo(alias="periodStart", default=None)

    period_end: str = FieldInfo(alias="periodEnd")

    period_pnl: Optional[float] = FieldInfo(alias="periodPnl", default=None)
    """P&L since the period-start stored valuation. When no valuation precedes the period, accounts (or tournament members) created inside the window use the initial balance as the baseline. Null for `all` and when no baseline exists."""

    unrealized_pnl: float = FieldInfo(alias="unrealizedPnl")

    total_account_value: float = FieldInfo(alias="totalAccountValue")

    total_holdings_value: float = FieldInfo(alias="totalHoldingsValue")

    total_cost_basis: float = FieldInfo(alias="totalCostBasis")

    roi: Optional[float] = None
    """Percentage return. Bounded periods: `periodPnl` over the period-start baseline. `all`: for global portfolios, return over total deposits (null when none are recorded); for an organization-bound key's default tournament, return over the tournament's initial virtual balance. Null when the baseline is missing or zero."""

    sharpe: Optional[float] = None
    """Mean daily return over its standard deviation, annualized by √252, from the stitched daily portfolio-value series within the period (including projection-backed history under engine authority). Null when the daily returns have no usable variance."""
