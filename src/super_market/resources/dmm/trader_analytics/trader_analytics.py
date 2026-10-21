# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from ....types.dmm.dmm_trader_analytics_elite_summary import DmmTraderAnalyticsEliteSummary
from ....types.dmm import trader_analytic_list_elite_summary_params

__all__ = ["TraderAnalyticsResource", "AsyncTraderAnalyticsResource"]


class TraderAnalyticsResource(SyncAPIResource):
    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> TraderAnalyticsResourceWithRawResponse:
        return TraderAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TraderAnalyticsResourceWithStreamingResponse:
        return TraderAnalyticsResourceWithStreamingResponse(self)

    def list_elite_summary(
        self,
        *,
        tournament_id: str | Omit = omit,
        market_type: str | Omit = omit,
        organization_slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmmTraderAnalyticsEliteSummary:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Snapshot of the elite cohort for the caller's organization (or a specific tournament when `tournamentId` is supplied): latest cut timestamp, cohort size and smart-score band, the platform-wide thresholds used by the scoring pipeline, and the top 10 elites by decayed smart score.

        When `tournamentId` is supplied the cohort and top performers are read from `tournament_elites` / `tournament_trader_metrics`; otherwise from `organization_elites` / `organization_trader_metrics`.

        Args:
            tournament_id: Query parameter.
            market_type: Query parameter.
            organization_slug: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DmmTraderAnalyticsEliteSummary: Elite summary.

        Example:
            ```python
            trader_analytic = client.dmm.trader_analytics.list_elite_summary()
            ```
        """
        return self._get(
            "/dmm/trader-analytics/elite-summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "tournament_id": tournament_id,
                        "market_type": market_type,
                        "organization_slug": organization_slug,
                    },
                    trader_analytic_list_elite_summary_params.TraderAnalyticListEliteSummaryParams,
                ),
            ),
            cast_to=DmmTraderAnalyticsEliteSummary,
        )


class AsyncTraderAnalyticsResource(AsyncAPIResource):
    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTraderAnalyticsResourceWithRawResponse:
        return AsyncTraderAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTraderAnalyticsResourceWithStreamingResponse:
        return AsyncTraderAnalyticsResourceWithStreamingResponse(self)

    async def list_elite_summary(
        self,
        *,
        tournament_id: str | Omit = omit,
        market_type: str | Omit = omit,
        organization_slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmmTraderAnalyticsEliteSummary:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Snapshot of the elite cohort for the caller's organization (or a specific tournament when `tournamentId` is supplied): latest cut timestamp, cohort size and smart-score band, the platform-wide thresholds used by the scoring pipeline, and the top 10 elites by decayed smart score.

        When `tournamentId` is supplied the cohort and top performers are read from `tournament_elites` / `tournament_trader_metrics`; otherwise from `organization_elites` / `organization_trader_metrics`.

        Args:
            tournament_id: Query parameter.
            market_type: Query parameter.
            organization_slug: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DmmTraderAnalyticsEliteSummary: Elite summary.

        Example:
            ```python
            trader_analytic = await client.dmm.trader_analytics.list_elite_summary()
            ```
        """
        return await self._get(
            "/dmm/trader-analytics/elite-summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "tournament_id": tournament_id,
                        "market_type": market_type,
                        "organization_slug": organization_slug,
                    },
                    trader_analytic_list_elite_summary_params.TraderAnalyticListEliteSummaryParams,
                ),
            ),
            cast_to=DmmTraderAnalyticsEliteSummary,
        )


class TraderAnalyticsResourceWithRawResponse:
    def __init__(self, trader_analytics: TraderAnalyticsResource) -> None:
        self._trader_analytics = trader_analytics

        self.list_elite_summary = to_raw_response_wrapper(
            trader_analytics.list_elite_summary,
        )

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._trader_analytics.users)


class AsyncTraderAnalyticsResourceWithRawResponse:
    def __init__(self, trader_analytics: AsyncTraderAnalyticsResource) -> None:
        self._trader_analytics = trader_analytics

        self.list_elite_summary = async_to_raw_response_wrapper(
            trader_analytics.list_elite_summary,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._trader_analytics.users)


class TraderAnalyticsResourceWithStreamingResponse:
    def __init__(self, trader_analytics: TraderAnalyticsResource) -> None:
        self._trader_analytics = trader_analytics

        self.list_elite_summary = to_streamed_response_wrapper(
            trader_analytics.list_elite_summary,
        )

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._trader_analytics.users)


class AsyncTraderAnalyticsResourceWithStreamingResponse:
    def __init__(self, trader_analytics: AsyncTraderAnalyticsResource) -> None:
        self._trader_analytics = trader_analytics

        self.list_elite_summary = async_to_streamed_response_wrapper(
            trader_analytics.list_elite_summary,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._trader_analytics.users)
