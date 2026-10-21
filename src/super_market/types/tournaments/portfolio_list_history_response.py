# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from .tournament_portfolio_history_point import TournamentPortfolioHistoryPoint

__all__ = ["PortfolioListHistoryResponse"]


class PortfolioListHistoryResponse(BaseModel):
    interval: Literal["1h", "6h", "1d", "1w", "all"]

    from_: str = FieldInfo(alias="from")

    to: str

    data: List[TournamentPortfolioHistoryPoint]
