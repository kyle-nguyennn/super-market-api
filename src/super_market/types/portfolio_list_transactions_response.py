# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from .._models import BaseModel

from .transaction import Transaction
from .portfolio_pagination import PortfolioPagination
from .economic_command_coverage import EconomicCommandCoverage

__all__ = ["PortfolioListTransactionsResponse"]


class PortfolioListTransactionsResponse(BaseModel):
    data: List[Transaction]

    pagination: PortfolioPagination

    coverage: EconomicCommandCoverage
