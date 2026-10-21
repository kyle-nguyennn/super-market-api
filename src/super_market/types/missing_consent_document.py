# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MissingConsentDocument"]


class MissingConsentDocument(BaseModel):
    document_id: str = FieldInfo(alias="documentId")

    kind: Literal["platform_terms", "org_terms", "org_rules"]

    version: str

    organization_id: Optional[str] = FieldInfo(alias="organizationId", default=None)

    organization_slug: Optional[str] = FieldInfo(alias="organizationSlug", default=None)
    """Slug of the organization that owns the document, or null for platform documents."""

    organization_name: Optional[str] = FieldInfo(alias="organizationName", default=None)

    support_email: Optional[str] = FieldInfo(alias="supportEmail", default=None)
    """Support address of the owning organization, or null when it has none or the document is a platform document."""

    currency_name: Optional[str] = FieldInfo(alias="currencyName", default=None)
    """Competition currency name of the owning organization, or null when it has none or the document is a platform document."""

    url: Optional[str] = None
    """Document URL, or null when the document is rendered on its host."""

    host: str
    """Base URL of the platform or organization hosting the document."""
