# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from .designated_market_maker_icims_export_tag import DesignatedMarketMakerIcimsExportTag

__all__ = ["DesignatedMarketMakerIcimsExportCandidate"]


class DesignatedMarketMakerIcimsExportCandidate(BaseModel):
    rank: int
    """1-based position in the exported, score-ordered list."""

    profile_id: str = FieldInfo(alias="profileId")

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    email: Optional[str] = None

    smart_score: Optional[float] = FieldInfo(alias="smartScore", default=None)
    """Org-aggregate Smart Score the export is ordered by; null when the member has no metric snapshot."""

    phone: Optional[str] = None
    """Optional phone number supplied during SIG registration; null when not provided."""

    contact_opt_in: Optional[bool] = FieldInfo(alias="contactOptIn", default=None)
    """Contact consent state for this organization: true when the member opted in, false when the member registered without opting in, and null when no registration was collected."""

    tags: List[DesignatedMarketMakerIcimsExportTag]

    application_job_requisition_ids: List[str] = FieldInfo(alias="applicationJobRequisitionIds")
    """iCIMS job requisition ids the candidate qualifies to be submitted against."""
