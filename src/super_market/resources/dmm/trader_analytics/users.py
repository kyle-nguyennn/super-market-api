# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Optional, Union
from datetime import datetime
from typing_extensions import Literal

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.dmm.trader_analytics.dmm_trader_analytics_users_list import DmmTraderAnalyticsUsersList
from ....types.dmm.trader_analytics import user_list_params, user_retrieve_params
from ....types.dmm.trader_analytics.dmm_trader_analytics_user_detail import DmmTraderAnalyticsUserDetail

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        tournament_id: str | Omit = omit,
        group_id: str | Omit = omit,
        market_group_id: str | Omit = omit,
        market_type: str | Omit = omit,
        period: Literal["day", "week", "month", "quarter", "all"] | Omit = omit,
        period_start: Union[str, datetime] | Omit = omit,
        period_end: Union[str, datetime] | Omit = omit,
        min_smart_score: Optional[float] | Omit = omit,
        min_trades: Optional[int] | Omit = omit,
        elite_only: Literal["true", "false"] | Omit = omit,
        sort: Literal["smart_score_desc", "profit_desc", "roi_desc", "sharpe_desc", "win_rate_desc", "trades_desc"]
        | Omit = omit,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        organization_slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmmTraderAnalyticsUsersList:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Org-scoped trader analytics with optional tournament / user-group / market-group / period filters and elite / score / trade thresholds.

        Pass `tournamentId` to scope to a single tournament (must belong to your organization); otherwise the request is org-wide.

        Metrics are recomputed on-demand for each request from the trade fact tables — they reflect the current scope and window, not the persisted daily snapshot. `computedAsOf` reflects the recompute timestamp.

        Args:
            tournament_id: Tournament id (must belong to your organization).
            group_id: User-group id (must belong to your organization).
            market_group_id: Market-group id (must belong to your organization).
            market_type: Trader-metrics bucket. Defaults to `global`.
            period: Calendar-aligned period (UTC). `day` = today, `week` = since the most recent Sunday, `month` = since the 1st of the current month, `quarter` = since the 1st of the current calendar quarter, `all` = no time filter.
            period_start: Custom window start (ISO 8601). Mutually exclusive with `period` when `period != all`.
            period_end: Custom window end (ISO 8601). Metrics are computed as of this instant, with open positions marked at prices as of `periodEnd`. Requires `period` to be omitted or `all`, and must be after `periodStart` when both are sent.
            min_smart_score: Query parameter.
            min_trades: Query parameter.
            elite_only: Query parameter.
            sort: Query parameter.
            limit: Query parameter.
            cursor: Opaque pagination cursor from a prior response.
            organization_slug: Required for platform administrators when `tournamentId` is omitted.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DmmTraderAnalyticsUsersList: Trader analytics page.

        Example:
            ```python
            dmm_trader_analytics_users = client.dmm.trader_analytics.users.list()
            ```
        """
        return self._get(
            "/dmm/trader-analytics/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "tournament_id": tournament_id,
                        "group_id": group_id,
                        "market_group_id": market_group_id,
                        "market_type": market_type,
                        "period": period,
                        "period_start": period_start,
                        "period_end": period_end,
                        "min_smart_score": min_smart_score,
                        "min_trades": min_trades,
                        "elite_only": elite_only,
                        "sort": sort,
                        "limit": limit,
                        "cursor": cursor,
                        "organization_slug": organization_slug,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=DmmTraderAnalyticsUsersList,
        )

    def retrieve(
        self,
        profile_id: str,
        *,
        tournament_id: str | Omit = omit,
        market_group_id: str | Omit = omit,
        market_type: str | Omit = omit,
        period: Literal["day", "week", "month", "quarter", "all"] | Omit = omit,
        period_start: Union[str, datetime] | Omit = omit,
        period_end: Union[str, datetime] | Omit = omit,
        include_history: Literal["true", "false"] | Omit = omit,
        organization_slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmmTraderAnalyticsUserDetail:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Returns the on-demand metrics row for a single trader in the requested scope, plus a per-market-type breakdown from the latest persisted snapshot and an optional daily smart-score history (up to 30 points).

        The trader must be a member of the resolved org (or, when `tournamentId` is supplied, the tournament). The `categories` and `history` arrays are always read from `organization_trader_metrics` and therefore reflect organization-wide data even when the metrics row itself is tournament-scoped.

        Args:
            profile_id: Path parameter.
            tournament_id: Query parameter.
            market_group_id: Query parameter.
            market_type: Query parameter.
            period: Calendar-aligned period (UTC). `day` = today, `week` = since the most recent Sunday, `month` = since the 1st of the current month, `quarter` = since the 1st of the current calendar quarter, `all` = no time filter.
            period_start: Custom window start (ISO 8601). Mutually exclusive with `period` when `period != all`.
            period_end: Custom window end (ISO 8601). Metrics are computed as of this instant, with open positions marked at prices as of `periodEnd`. Requires `period` to be omitted or `all`, and must be after `periodStart` when both are sent.
            include_history: Query parameter.
            organization_slug: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DmmTraderAnalyticsUserDetail: Trader detail.

        Example:
            ```python
            user = client.dmm.trader_analytics.users.retrieve(
                profile_id="550e8400-e29b-41d4-a716-446655440000",
            )
            ```
        """
        if profile_id is None or (isinstance(profile_id, str) and not profile_id):
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._get(
            path_template("/dmm/trader-analytics/users/{profileId}", **{"profileId": profile_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "tournament_id": tournament_id,
                        "market_group_id": market_group_id,
                        "market_type": market_type,
                        "period": period,
                        "period_start": period_start,
                        "period_end": period_end,
                        "include_history": include_history,
                        "organization_slug": organization_slug,
                    },
                    user_retrieve_params.UserRetrieveParams,
                ),
            ),
            cast_to=DmmTraderAnalyticsUserDetail,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        tournament_id: str | Omit = omit,
        group_id: str | Omit = omit,
        market_group_id: str | Omit = omit,
        market_type: str | Omit = omit,
        period: Literal["day", "week", "month", "quarter", "all"] | Omit = omit,
        period_start: Union[str, datetime] | Omit = omit,
        period_end: Union[str, datetime] | Omit = omit,
        min_smart_score: Optional[float] | Omit = omit,
        min_trades: Optional[int] | Omit = omit,
        elite_only: Literal["true", "false"] | Omit = omit,
        sort: Literal["smart_score_desc", "profit_desc", "roi_desc", "sharpe_desc", "win_rate_desc", "trades_desc"]
        | Omit = omit,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        organization_slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmmTraderAnalyticsUsersList:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Org-scoped trader analytics with optional tournament / user-group / market-group / period filters and elite / score / trade thresholds.

        Pass `tournamentId` to scope to a single tournament (must belong to your organization); otherwise the request is org-wide.

        Metrics are recomputed on-demand for each request from the trade fact tables — they reflect the current scope and window, not the persisted daily snapshot. `computedAsOf` reflects the recompute timestamp.

        Args:
            tournament_id: Tournament id (must belong to your organization).
            group_id: User-group id (must belong to your organization).
            market_group_id: Market-group id (must belong to your organization).
            market_type: Trader-metrics bucket. Defaults to `global`.
            period: Calendar-aligned period (UTC). `day` = today, `week` = since the most recent Sunday, `month` = since the 1st of the current month, `quarter` = since the 1st of the current calendar quarter, `all` = no time filter.
            period_start: Custom window start (ISO 8601). Mutually exclusive with `period` when `period != all`.
            period_end: Custom window end (ISO 8601). Metrics are computed as of this instant, with open positions marked at prices as of `periodEnd`. Requires `period` to be omitted or `all`, and must be after `periodStart` when both are sent.
            min_smart_score: Query parameter.
            min_trades: Query parameter.
            elite_only: Query parameter.
            sort: Query parameter.
            limit: Query parameter.
            cursor: Opaque pagination cursor from a prior response.
            organization_slug: Required for platform administrators when `tournamentId` is omitted.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DmmTraderAnalyticsUsersList: Trader analytics page.

        Example:
            ```python
            dmm_trader_analytics_users = await client.dmm.trader_analytics.users.list()
            ```
        """
        return await self._get(
            "/dmm/trader-analytics/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "tournament_id": tournament_id,
                        "group_id": group_id,
                        "market_group_id": market_group_id,
                        "market_type": market_type,
                        "period": period,
                        "period_start": period_start,
                        "period_end": period_end,
                        "min_smart_score": min_smart_score,
                        "min_trades": min_trades,
                        "elite_only": elite_only,
                        "sort": sort,
                        "limit": limit,
                        "cursor": cursor,
                        "organization_slug": organization_slug,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=DmmTraderAnalyticsUsersList,
        )

    async def retrieve(
        self,
        profile_id: str,
        *,
        tournament_id: str | Omit = omit,
        market_group_id: str | Omit = omit,
        market_type: str | Omit = omit,
        period: Literal["day", "week", "month", "quarter", "all"] | Omit = omit,
        period_start: Union[str, datetime] | Omit = omit,
        period_end: Union[str, datetime] | Omit = omit,
        include_history: Literal["true", "false"] | Omit = omit,
        organization_slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmmTraderAnalyticsUserDetail:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Returns the on-demand metrics row for a single trader in the requested scope, plus a per-market-type breakdown from the latest persisted snapshot and an optional daily smart-score history (up to 30 points).

        The trader must be a member of the resolved org (or, when `tournamentId` is supplied, the tournament). The `categories` and `history` arrays are always read from `organization_trader_metrics` and therefore reflect organization-wide data even when the metrics row itself is tournament-scoped.

        Args:
            profile_id: Path parameter.
            tournament_id: Query parameter.
            market_group_id: Query parameter.
            market_type: Query parameter.
            period: Calendar-aligned period (UTC). `day` = today, `week` = since the most recent Sunday, `month` = since the 1st of the current month, `quarter` = since the 1st of the current calendar quarter, `all` = no time filter.
            period_start: Custom window start (ISO 8601). Mutually exclusive with `period` when `period != all`.
            period_end: Custom window end (ISO 8601). Metrics are computed as of this instant, with open positions marked at prices as of `periodEnd`. Requires `period` to be omitted or `all`, and must be after `periodStart` when both are sent.
            include_history: Query parameter.
            organization_slug: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DmmTraderAnalyticsUserDetail: Trader detail.

        Example:
            ```python
            user = await client.dmm.trader_analytics.users.retrieve(
                profile_id="550e8400-e29b-41d4-a716-446655440000",
            )
            ```
        """
        if profile_id is None or (isinstance(profile_id, str) and not profile_id):
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._get(
            path_template("/dmm/trader-analytics/users/{profileId}", **{"profileId": profile_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "tournament_id": tournament_id,
                        "market_group_id": market_group_id,
                        "market_type": market_type,
                        "period": period,
                        "period_start": period_start,
                        "period_end": period_end,
                        "include_history": include_history,
                        "organization_slug": organization_slug,
                    },
                    user_retrieve_params.UserRetrieveParams,
                ),
            ),
            cast_to=DmmTraderAnalyticsUserDetail,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.list = to_raw_response_wrapper(
            users.list,
        )
        self.retrieve = to_raw_response_wrapper(
            users.retrieve,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.list = async_to_raw_response_wrapper(
            users.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            users.retrieve,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.list = to_streamed_response_wrapper(
            users.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            users.retrieve,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            users.retrieve,
        )
