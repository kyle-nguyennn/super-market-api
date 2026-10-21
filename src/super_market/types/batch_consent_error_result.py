# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from .._models import BaseModel

from .terms_not_acknowledged_error import TermsNotAcknowledgedError

__all__ = ["BatchConsentErrorResult"]


class BatchConsentErrorResult(BaseModel):
    index: int

    ok: Literal[False]

    status: Literal[403]

    data: TermsNotAcknowledgedError
