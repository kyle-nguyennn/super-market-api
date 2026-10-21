# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from ..._models import BaseModel

from .tournament_transaction import TournamentTransaction
from .tournament_pagination import TournamentPagination
from .tournament_economic_command_coverage import TournamentEconomicCommandCoverage

__all__ = ["PortfolioListTransactionsResponse"]


class PortfolioListTransactionsResponse(BaseModel):
    data: List[TournamentTransaction]

    pagination: TournamentPagination

    coverage: TournamentEconomicCommandCoverage
