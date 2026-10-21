# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["IcimListExportParams"]


class IcimListExportParams(TypedDict, total=False):
    organization_slug: Annotated[str, PropertyInfo(alias="organizationSlug")]
    """Slug of the organization to export. Organization-bound keys may only name their own organization (defaults to it when omitted; another organization's slug returns 403, an unknown slug 404). Required for platform administrators."""
