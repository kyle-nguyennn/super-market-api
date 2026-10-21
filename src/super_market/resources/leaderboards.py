# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Optional
from typing_extensions import Literal

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.leaderboard_list_response import LeaderboardListResponse
from ..types import leaderboard_list_params

__all__ = ["LeaderboardsResource", "AsyncLeaderboardsResource"]


class LeaderboardsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LeaderboardsResourceWithRawResponse:
        return LeaderboardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LeaderboardsResourceWithStreamingResponse:
        return LeaderboardsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        tournament_slug: str | Omit = omit,
        group_id: str | Omit = omit,
        period: Literal["1d", "7d", "30d", "quarter", "all"] | Omit = omit,
        sort: Literal["pnl", "roi", "winRate", "volume", "trades"] | Omit = omit,
        limit: int | Omit = omit,
        offset: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LeaderboardListResponse:
        """
        Returns a leaderboard ranked by P&L. When `tournamentSlug` is omitted, an organization-bound API key defaults to its organization's default tournament; an unbound key ranks across global trading (`tournament_id IS NULL`). When supplied, `tournamentSlug` explicitly scopes the response to that tournament's members. Tournament-scoped requests, whether explicit or organization-defaulted, unlock the `groupId` and `sort` filters. Ranks use standard competition ranking: tied entries share a rank and the positions that follow skip by the size of the tie (1-1-3).

        **Period semantics (calendar-aligned, UTC):**
        - `1d` — Today (since 00:00 UTC today)
        - `7d` — This Week (since 00:00 UTC on the most recent Sunday)
        - `30d` — This Month (since 00:00 UTC on the 1st of the current month)
        - `quarter` — Since 00:00 UTC on the first day of the current calendar quarter
        - `all` — All-time

        `groupId` and `sort` are rejected with 400 only when the request resolves to the global leaderboard (user groups are tournament-scoped; the global query path doesn't honor `sort` and always orders by P&L).

        Args:
            tournament_slug: Optional tournament/global tournament slug to scope to. When omitted, organization-bound keys use the organization's default tournament and unbound keys use the global leaderboard.
            group_id: Optional user-group filter. Requires an explicit tournament slug or an organization-bound key; the group must be bound to the resolved tournament.
            period: Calendar-aligned period (UTC).
            sort: Sort key. Honored for explicit or organization-defaulted tournament leaderboards; defaults to `pnl`.
            limit: Results per page (max 100).
            offset: Offset for pagination.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LeaderboardListResponse: Leaderboard.

        Example:
            ```python
            leaderboard = client.leaderboards.list(
                period="all",
                limit=50,
                offset=0,
            )
            ```
        """
        return self._get(
            "/leaderboards",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "tournament_slug": tournament_slug,
                        "group_id": group_id,
                        "period": period,
                        "sort": sort,
                        "limit": limit,
                        "offset": offset,
                    },
                    leaderboard_list_params.LeaderboardListParams,
                ),
            ),
            cast_to=LeaderboardListResponse,
        )


class AsyncLeaderboardsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLeaderboardsResourceWithRawResponse:
        return AsyncLeaderboardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLeaderboardsResourceWithStreamingResponse:
        return AsyncLeaderboardsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        tournament_slug: str | Omit = omit,
        group_id: str | Omit = omit,
        period: Literal["1d", "7d", "30d", "quarter", "all"] | Omit = omit,
        sort: Literal["pnl", "roi", "winRate", "volume", "trades"] | Omit = omit,
        limit: int | Omit = omit,
        offset: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LeaderboardListResponse:
        """
        Returns a leaderboard ranked by P&L. When `tournamentSlug` is omitted, an organization-bound API key defaults to its organization's default tournament; an unbound key ranks across global trading (`tournament_id IS NULL`). When supplied, `tournamentSlug` explicitly scopes the response to that tournament's members. Tournament-scoped requests, whether explicit or organization-defaulted, unlock the `groupId` and `sort` filters. Ranks use standard competition ranking: tied entries share a rank and the positions that follow skip by the size of the tie (1-1-3).

        **Period semantics (calendar-aligned, UTC):**
        - `1d` — Today (since 00:00 UTC today)
        - `7d` — This Week (since 00:00 UTC on the most recent Sunday)
        - `30d` — This Month (since 00:00 UTC on the 1st of the current month)
        - `quarter` — Since 00:00 UTC on the first day of the current calendar quarter
        - `all` — All-time

        `groupId` and `sort` are rejected with 400 only when the request resolves to the global leaderboard (user groups are tournament-scoped; the global query path doesn't honor `sort` and always orders by P&L).

        Args:
            tournament_slug: Optional tournament/global tournament slug to scope to. When omitted, organization-bound keys use the organization's default tournament and unbound keys use the global leaderboard.
            group_id: Optional user-group filter. Requires an explicit tournament slug or an organization-bound key; the group must be bound to the resolved tournament.
            period: Calendar-aligned period (UTC).
            sort: Sort key. Honored for explicit or organization-defaulted tournament leaderboards; defaults to `pnl`.
            limit: Results per page (max 100).
            offset: Offset for pagination.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LeaderboardListResponse: Leaderboard.

        Example:
            ```python
            leaderboard = await client.leaderboards.list(
                period="all",
                limit=50,
                offset=0,
            )
            ```
        """
        return await self._get(
            "/leaderboards",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "tournament_slug": tournament_slug,
                        "group_id": group_id,
                        "period": period,
                        "sort": sort,
                        "limit": limit,
                        "offset": offset,
                    },
                    leaderboard_list_params.LeaderboardListParams,
                ),
            ),
            cast_to=LeaderboardListResponse,
        )


class LeaderboardsResourceWithRawResponse:
    def __init__(self, leaderboards: LeaderboardsResource) -> None:
        self._leaderboards = leaderboards

        self.list = to_raw_response_wrapper(
            leaderboards.list,
        )


class AsyncLeaderboardsResourceWithRawResponse:
    def __init__(self, leaderboards: AsyncLeaderboardsResource) -> None:
        self._leaderboards = leaderboards

        self.list = async_to_raw_response_wrapper(
            leaderboards.list,
        )


class LeaderboardsResourceWithStreamingResponse:
    def __init__(self, leaderboards: LeaderboardsResource) -> None:
        self._leaderboards = leaderboards

        self.list = to_streamed_response_wrapper(
            leaderboards.list,
        )


class AsyncLeaderboardsResourceWithStreamingResponse:
    def __init__(self, leaderboards: AsyncLeaderboardsResource) -> None:
        self._leaderboards = leaderboards

        self.list = async_to_streamed_response_wrapper(
            leaderboards.list,
        )
