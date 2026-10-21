# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["SeasonDescriptor"]


class SeasonDescriptor(BaseModel):
    """Season descriptor for Ongoing Play tournaments; null for other tournaments."""

    season_key: str

    archived: bool
