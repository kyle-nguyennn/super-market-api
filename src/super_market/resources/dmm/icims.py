# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.dmm.designated_market_maker_icims_export import DesignatedMarketMakerIcimsExport
from ...types.dmm import icim_list_export_params

__all__ = ["IcimsResource", "AsyncIcimsResource"]


class IcimsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IcimsResourceWithRawResponse:
        return IcimsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IcimsResourceWithStreamingResponse:
        return IcimsResourceWithStreamingResponse(self)

    def list_export(
        self,
        *,
        organization_slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerIcimsExport:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Manual trigger for the org's iCIMS data export. Evaluates the configured tag rules against every organization member and returns the qualifying candidates with the iCIMS tags and job requisitions they earned, ordered by org-aggregate Smart Score (strongest first). Read-only — it never calls the iCIMS API, so it works even when the push integration is disabled or has no credentials. An organization-bound API key exports its own organization; it may pass its own `organizationSlug`, but naming another organization's slug returns 403 and an unknown slug returns 404. Platform administrators must pass `organizationSlug` to choose the organization.

        `contactOptIn` is true when the member opted in, false when the member registered without opting in, and null when no registration was collected for that organization.

        The admin Web UI consumes the same export as a CSV download.

        Args:
            organization_slug: Slug of the organization to export. Organization-bound keys may only name their own organization (defaults to it when omitted; another organization's slug returns 403, an unknown slug 404). Required for platform administrators.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerIcimsExport: The qualifying candidates.

        Example:
            ```python
            icim = client.dmm.icims.list_export()
            ```
        """
        return self._get(
            "/dmm/icims/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_slug": organization_slug}, icim_list_export_params.IcimListExportParams
                ),
            ),
            cast_to=DesignatedMarketMakerIcimsExport,
        )


class AsyncIcimsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIcimsResourceWithRawResponse:
        return AsyncIcimsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIcimsResourceWithStreamingResponse:
        return AsyncIcimsResourceWithStreamingResponse(self)

    async def list_export(
        self,
        *,
        organization_slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerIcimsExport:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Manual trigger for the org's iCIMS data export. Evaluates the configured tag rules against every organization member and returns the qualifying candidates with the iCIMS tags and job requisitions they earned, ordered by org-aggregate Smart Score (strongest first). Read-only — it never calls the iCIMS API, so it works even when the push integration is disabled or has no credentials. An organization-bound API key exports its own organization; it may pass its own `organizationSlug`, but naming another organization's slug returns 403 and an unknown slug returns 404. Platform administrators must pass `organizationSlug` to choose the organization.

        `contactOptIn` is true when the member opted in, false when the member registered without opting in, and null when no registration was collected for that organization.

        The admin Web UI consumes the same export as a CSV download.

        Args:
            organization_slug: Slug of the organization to export. Organization-bound keys may only name their own organization (defaults to it when omitted; another organization's slug returns 403, an unknown slug 404). Required for platform administrators.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerIcimsExport: The qualifying candidates.

        Example:
            ```python
            icim = await client.dmm.icims.list_export()
            ```
        """
        return await self._get(
            "/dmm/icims/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_slug": organization_slug}, icim_list_export_params.IcimListExportParams
                ),
            ),
            cast_to=DesignatedMarketMakerIcimsExport,
        )


class IcimsResourceWithRawResponse:
    def __init__(self, icims: IcimsResource) -> None:
        self._icims = icims

        self.list_export = to_raw_response_wrapper(
            icims.list_export,
        )


class AsyncIcimsResourceWithRawResponse:
    def __init__(self, icims: AsyncIcimsResource) -> None:
        self._icims = icims

        self.list_export = async_to_raw_response_wrapper(
            icims.list_export,
        )


class IcimsResourceWithStreamingResponse:
    def __init__(self, icims: IcimsResource) -> None:
        self._icims = icims

        self.list_export = to_streamed_response_wrapper(
            icims.list_export,
        )


class AsyncIcimsResourceWithStreamingResponse:
    def __init__(self, icims: AsyncIcimsResource) -> None:
        self._icims = icims

        self.list_export = async_to_streamed_response_wrapper(
            icims.list_export,
        )
