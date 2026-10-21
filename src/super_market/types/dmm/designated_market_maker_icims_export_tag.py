# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DesignatedMarketMakerIcimsExportTag"]


class DesignatedMarketMakerIcimsExportTag(BaseModel):
    tag_id: str = FieldInfo(alias="tagId")
    """iCIMS tag id earned by the candidate."""

    tag_label: Optional[str] = FieldInfo(alias="tagLabel", default=None)
    """Human-readable label for the tag; null when the rule has no label."""
