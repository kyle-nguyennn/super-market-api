# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MarketThumbnailPatch"]


class MarketThumbnailPatch(BaseModel):
    video_still_active: bool = FieldInfo(alias="videoStillActive")
    """True when the market's existing header video remains active after replacing its thumbnail."""
