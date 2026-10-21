# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from .designated_market_maker_icims_export_candidate import DesignatedMarketMakerIcimsExportCandidate

__all__ = ["DesignatedMarketMakerIcimsExport"]


class DesignatedMarketMakerIcimsExport(BaseModel):
    organization_id: str = FieldInfo(alias="organizationId")

    organization_slug: Optional[str] = FieldInfo(alias="organizationSlug", default=None)

    organization_name: Optional[str] = FieldInfo(alias="organizationName", default=None)

    evaluated: int
    """Total org members evaluated against the tag rules."""

    total: int
    """Number of qualifying candidates returned."""

    candidates: List[DesignatedMarketMakerIcimsExportCandidate]
