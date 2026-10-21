# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from ..._models import BaseModel

from .tournament_settlement_entry import TournamentSettlementEntry
from .tournament_pagination import TournamentPagination
from .tournament_economic_command_coverage import TournamentEconomicCommandCoverage

__all__ = ["PortfolioListSettlementsResponse"]


class PortfolioListSettlementsResponse(BaseModel):
    data: List[TournamentSettlementEntry]

    pagination: TournamentPagination

    coverage: TournamentEconomicCommandCoverage
