# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .missing_consent_document import MissingConsentDocument

__all__ = ["TermsNotAcknowledgedError", "Error", "ErrorDetails"]


class ErrorDetails(BaseModel):
    missing_documents: List[MissingConsentDocument] = FieldInfo(alias="missingDocuments")


class Error(BaseModel):
    code: Literal["TERMS_NOT_ACKNOWLEDGED"]

    message: str

    details: ErrorDetails


class TermsNotAcknowledgedError(BaseModel):
    error: Error
