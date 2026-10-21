# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from .._models import BaseModel

from .settlement_entry import SettlementEntry
from .portfolio_pagination import PortfolioPagination
from .economic_command_coverage import EconomicCommandCoverage

__all__ = ["PortfolioListSettlementsResponse"]


class PortfolioListSettlementsResponse(BaseModel):
    data: List[SettlementEntry]

    pagination: PortfolioPagination

    coverage: EconomicCommandCoverage
