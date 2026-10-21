# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from .designated_market_maker_transaction import DesignatedMarketMakerTransaction

__all__ = ["DesignatedMarketMakerTransactionList"]


class DesignatedMarketMakerTransactionList(BaseModel):
    data: List[DesignatedMarketMakerTransaction]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
