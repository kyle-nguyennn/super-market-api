# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .designated_market_maker_settlement_override_preview import DesignatedMarketMakerSettlementOverridePreview

__all__ = ["DesignatedMarketMakerSettlementOverrideExecution"]


class DesignatedMarketMakerSettlementOverrideExecution(DesignatedMarketMakerSettlementOverridePreview):
    transaction_group_id: str = FieldInfo(alias="transactionGroupId")

    corrections_created: int = FieldInfo(alias="correctionsCreated")

    snapshot_rows: int = FieldInfo(alias="snapshotRows")
    """Number of tournament portfolio snapshot rows refreshed at the original tournament end date."""
