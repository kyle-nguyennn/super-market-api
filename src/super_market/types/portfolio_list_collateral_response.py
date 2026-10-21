# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from .._models import BaseModel

from .portfolio_collateral import PortfolioCollateral

__all__ = ["PortfolioListCollateralResponse"]


class PortfolioListCollateralResponse(BaseModel):
    data: List[PortfolioCollateral]
