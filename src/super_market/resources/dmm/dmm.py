# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Optional
from typing_extensions import Literal

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
from .tournaments import (
    TournamentsResource,
    AsyncTournamentsResource,
    TournamentsResourceWithRawResponse,
    AsyncTournamentsResourceWithRawResponse,
    TournamentsResourceWithStreamingResponse,
    AsyncTournamentsResourceWithStreamingResponse,
)
from .relationships import (
    RelationshipsResource,
    AsyncRelationshipsResource,
    RelationshipsResourceWithRawResponse,
    AsyncRelationshipsResourceWithRawResponse,
    RelationshipsResourceWithStreamingResponse,
    AsyncRelationshipsResourceWithStreamingResponse,
)
from .icims import (
    IcimsResource,
    AsyncIcimsResource,
    IcimsResourceWithRawResponse,
    AsyncIcimsResourceWithRawResponse,
    IcimsResourceWithStreamingResponse,
    AsyncIcimsResourceWithStreamingResponse,
)
from .trader_analytics import (
    TraderAnalyticsResource,
    AsyncTraderAnalyticsResource,
    TraderAnalyticsResourceWithRawResponse,
    AsyncTraderAnalyticsResourceWithRawResponse,
    TraderAnalyticsResourceWithStreamingResponse,
    AsyncTraderAnalyticsResourceWithStreamingResponse,
)
from .groups import (
    GroupsResource,
    AsyncGroupsResource,
    GroupsResourceWithRawResponse,
    AsyncGroupsResourceWithRawResponse,
    GroupsResourceWithStreamingResponse,
    AsyncGroupsResourceWithStreamingResponse,
)
from ...types.designated_market_maker_failed_settlement_list import DesignatedMarketMakerFailedSettlementList
from ...types import dmm_list_failed_autosettlement_params, dmm_list_rankings_params
from ...types.designated_market_maker_org_rankings import DesignatedMarketMakerOrgRankings

__all__ = ["DmmResource", "AsyncDmmResource"]


class DmmResource(SyncAPIResource):
    @cached_property
    def tournaments(self) -> TournamentsResource:
        return TournamentsResource(self._client)

    @cached_property
    def relationships(self) -> RelationshipsResource:
        return RelationshipsResource(self._client)

    @cached_property
    def icims(self) -> IcimsResource:
        return IcimsResource(self._client)

    @cached_property
    def trader_analytics(self) -> TraderAnalyticsResource:
        return TraderAnalyticsResource(self._client)

    @cached_property
    def groups(self) -> GroupsResource:
        return GroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DmmResourceWithRawResponse:
        return DmmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DmmResourceWithStreamingResponse:
        return DmmResourceWithStreamingResponse(self)

    def list_failed_autosettlement(
        self,
        *,
        limit: int | Omit = omit,
        offset: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerFailedSettlementList:
        """
        <p class="api-access-notice"><span class="api-access-badge">Platform admin only</span><span class="api-access-detail">Unavailable to organization API keys.</span></p>

        Queue of contracts the autosettlers couldn't resolve (`settlement_failed = true` and still unsettled). Use the existing market settle UI to manually resolve them — this endpoint is read-only.

        For platform administrators only: the queue spans every organization, so organization owners and admins receive 403.

        Sorted by `settlementRetryCount` descending, so abandoned contracts (retry count at the cap) come first, then by oldest `lastCheckAttempt`, then by contract ID. Abandoned contracts will not be retried by cron — manual resolution is the only path forward.

        Args:
            limit: Page size (default 50, max 200).
            offset: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerFailedSettlementList: Queue page.

        Example:
            ```python
            dmm = client.dmm.list_failed_autosettlement()
            ```
        """
        return self._get(
            "/dmm/failed-autosettlement",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"limit": limit, "offset": offset},
                    dmm_list_failed_autosettlement_params.DmmListFailedAutosettlementParams,
                ),
            ),
            cast_to=DesignatedMarketMakerFailedSettlementList,
        )

    def list_rankings(
        self,
        *,
        organization_slug: str | Omit = omit,
        market_type: Literal[
            "global",
            "Election Outcome",
            "Financial Product",
            "Freeform",
            "Economic Indicator",
            "Sports Outcome",
            "Corporate Earnings",
            "Imported Market",
        ]
        | Omit = omit,
        sort_by: Literal[
            "smartScore",
            "smartScoreRaw",
            "roi",
            "sharpe",
            "winRate",
            "realizedPnl",
            "unrealizedPnl",
            "totalStake",
            "trades",
        ]
        | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        limit: int | Omit = omit,
        offset: Optional[int] | Omit = omit,
        user_group_id: str | Omit = omit,
        market_group_id: str | Omit = omit,
        period: Literal["1d", "7d", "30d", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerOrgRankings:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Cross-tournament user rankings scoped to a single organization. An organization-bound API key reads its own organization; it may pass its own `organizationSlug`, but naming another organization's slug returns 403 and an unknown slug returns 404. Platform administrators must pass `organizationSlug` to choose the organization. Reads from the latest `organization_trader_metrics` snapshot for the requested `marketType` by default. Returns one row per org member with rank, Smart Score, ROI, Sharpe (scaled), win rate, realized/unrealized PnL, stake, trade counts, and elite flag.

        In each member row, `hasSetUsername` indicates the handle is finalized and displayable — chosen by the participant or generated by the organization's automatic-username policy.

        Pass `userGroupId` to restrict rows to members of a user group inside this organization; ranks are recomputed within the filtered set.

        Pass `marketGroupId` and/or `period` to switch to an on-demand recompute that scopes trader metrics to trades inside that market group and/or within the calendar-aligned window. The response `computed` field indicates which path served the request. Ranks use standard competition ranking: tied entries share a rank and the positions that follow skip by the size of the tie (1-1-3).

        Args:
            organization_slug: Slug of the organization to read rankings for. Organization-bound keys may only name their own organization (defaults to it when omitted; another organization's slug returns 403, an unknown slug 404). Required for platform administrators.
            market_type: Trader-metrics bucket: `global` aggregates across all market types; any other value restricts metrics to that market type. Defaults to `global`.
            sort_by: Column to rank by. `smartScore` is the time-decayed composite; `smartScoreRaw` is the undecayed raw score.
            order: Query parameter.
            limit: Query parameter.
            offset: Query parameter.
            user_group_id: Optional user-group filter. Must be a `user_group` belonging to the target organization; otherwise the request is rejected with a validation error. Ranks are recomputed within the filtered set.
            market_group_id: Optional market-group filter. Must be a `market_group` belonging to the target organization; otherwise the request is rejected with a validation error. Switches the response to on-demand metrics scoped to trades within the group.
            period: Calendar-aligned period filter (UTC). `1d` = today, `7d` = since most recent Sunday, `30d` = since 1st of the current month, `all` = no time filter. When set to anything other than `all`, metrics are recomputed on-demand and `computed` will be `on-demand`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerOrgRankings: Org rankings page.

        Example:
            ```python
            dmm = client.dmm.list_rankings()
            ```
        """
        return self._get(
            "/dmm/rankings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_slug": organization_slug,
                        "market_type": market_type,
                        "sort_by": sort_by,
                        "order": order,
                        "limit": limit,
                        "offset": offset,
                        "user_group_id": user_group_id,
                        "market_group_id": market_group_id,
                        "period": period,
                    },
                    dmm_list_rankings_params.DmmListRankingsParams,
                ),
            ),
            cast_to=DesignatedMarketMakerOrgRankings,
        )


class AsyncDmmResource(AsyncAPIResource):
    @cached_property
    def tournaments(self) -> AsyncTournamentsResource:
        return AsyncTournamentsResource(self._client)

    @cached_property
    def relationships(self) -> AsyncRelationshipsResource:
        return AsyncRelationshipsResource(self._client)

    @cached_property
    def icims(self) -> AsyncIcimsResource:
        return AsyncIcimsResource(self._client)

    @cached_property
    def trader_analytics(self) -> AsyncTraderAnalyticsResource:
        return AsyncTraderAnalyticsResource(self._client)

    @cached_property
    def groups(self) -> AsyncGroupsResource:
        return AsyncGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDmmResourceWithRawResponse:
        return AsyncDmmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDmmResourceWithStreamingResponse:
        return AsyncDmmResourceWithStreamingResponse(self)

    async def list_failed_autosettlement(
        self,
        *,
        limit: int | Omit = omit,
        offset: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerFailedSettlementList:
        """
        <p class="api-access-notice"><span class="api-access-badge">Platform admin only</span><span class="api-access-detail">Unavailable to organization API keys.</span></p>

        Queue of contracts the autosettlers couldn't resolve (`settlement_failed = true` and still unsettled). Use the existing market settle UI to manually resolve them — this endpoint is read-only.

        For platform administrators only: the queue spans every organization, so organization owners and admins receive 403.

        Sorted by `settlementRetryCount` descending, so abandoned contracts (retry count at the cap) come first, then by oldest `lastCheckAttempt`, then by contract ID. Abandoned contracts will not be retried by cron — manual resolution is the only path forward.

        Args:
            limit: Page size (default 50, max 200).
            offset: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerFailedSettlementList: Queue page.

        Example:
            ```python
            dmm = await client.dmm.list_failed_autosettlement()
            ```
        """
        return await self._get(
            "/dmm/failed-autosettlement",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit, "offset": offset},
                    dmm_list_failed_autosettlement_params.DmmListFailedAutosettlementParams,
                ),
            ),
            cast_to=DesignatedMarketMakerFailedSettlementList,
        )

    async def list_rankings(
        self,
        *,
        organization_slug: str | Omit = omit,
        market_type: Literal[
            "global",
            "Election Outcome",
            "Financial Product",
            "Freeform",
            "Economic Indicator",
            "Sports Outcome",
            "Corporate Earnings",
            "Imported Market",
        ]
        | Omit = omit,
        sort_by: Literal[
            "smartScore",
            "smartScoreRaw",
            "roi",
            "sharpe",
            "winRate",
            "realizedPnl",
            "unrealizedPnl",
            "totalStake",
            "trades",
        ]
        | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        limit: int | Omit = omit,
        offset: Optional[int] | Omit = omit,
        user_group_id: str | Omit = omit,
        market_group_id: str | Omit = omit,
        period: Literal["1d", "7d", "30d", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerOrgRankings:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Cross-tournament user rankings scoped to a single organization. An organization-bound API key reads its own organization; it may pass its own `organizationSlug`, but naming another organization's slug returns 403 and an unknown slug returns 404. Platform administrators must pass `organizationSlug` to choose the organization. Reads from the latest `organization_trader_metrics` snapshot for the requested `marketType` by default. Returns one row per org member with rank, Smart Score, ROI, Sharpe (scaled), win rate, realized/unrealized PnL, stake, trade counts, and elite flag.

        In each member row, `hasSetUsername` indicates the handle is finalized and displayable — chosen by the participant or generated by the organization's automatic-username policy.

        Pass `userGroupId` to restrict rows to members of a user group inside this organization; ranks are recomputed within the filtered set.

        Pass `marketGroupId` and/or `period` to switch to an on-demand recompute that scopes trader metrics to trades inside that market group and/or within the calendar-aligned window. The response `computed` field indicates which path served the request. Ranks use standard competition ranking: tied entries share a rank and the positions that follow skip by the size of the tie (1-1-3).

        Args:
            organization_slug: Slug of the organization to read rankings for. Organization-bound keys may only name their own organization (defaults to it when omitted; another organization's slug returns 403, an unknown slug 404). Required for platform administrators.
            market_type: Trader-metrics bucket: `global` aggregates across all market types; any other value restricts metrics to that market type. Defaults to `global`.
            sort_by: Column to rank by. `smartScore` is the time-decayed composite; `smartScoreRaw` is the undecayed raw score.
            order: Query parameter.
            limit: Query parameter.
            offset: Query parameter.
            user_group_id: Optional user-group filter. Must be a `user_group` belonging to the target organization; otherwise the request is rejected with a validation error. Ranks are recomputed within the filtered set.
            market_group_id: Optional market-group filter. Must be a `market_group` belonging to the target organization; otherwise the request is rejected with a validation error. Switches the response to on-demand metrics scoped to trades within the group.
            period: Calendar-aligned period filter (UTC). `1d` = today, `7d` = since most recent Sunday, `30d` = since 1st of the current month, `all` = no time filter. When set to anything other than `all`, metrics are recomputed on-demand and `computed` will be `on-demand`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerOrgRankings: Org rankings page.

        Example:
            ```python
            dmm = await client.dmm.list_rankings()
            ```
        """
        return await self._get(
            "/dmm/rankings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_slug": organization_slug,
                        "market_type": market_type,
                        "sort_by": sort_by,
                        "order": order,
                        "limit": limit,
                        "offset": offset,
                        "user_group_id": user_group_id,
                        "market_group_id": market_group_id,
                        "period": period,
                    },
                    dmm_list_rankings_params.DmmListRankingsParams,
                ),
            ),
            cast_to=DesignatedMarketMakerOrgRankings,
        )


class DmmResourceWithRawResponse:
    def __init__(self, dmm: DmmResource) -> None:
        self._dmm = dmm

        self.list_failed_autosettlement = to_raw_response_wrapper(
            dmm.list_failed_autosettlement,
        )
        self.list_rankings = to_raw_response_wrapper(
            dmm.list_rankings,
        )

    @cached_property
    def tournaments(self) -> TournamentsResourceWithRawResponse:
        return TournamentsResourceWithRawResponse(self._dmm.tournaments)

    @cached_property
    def relationships(self) -> RelationshipsResourceWithRawResponse:
        return RelationshipsResourceWithRawResponse(self._dmm.relationships)

    @cached_property
    def icims(self) -> IcimsResourceWithRawResponse:
        return IcimsResourceWithRawResponse(self._dmm.icims)

    @cached_property
    def trader_analytics(self) -> TraderAnalyticsResourceWithRawResponse:
        return TraderAnalyticsResourceWithRawResponse(self._dmm.trader_analytics)

    @cached_property
    def groups(self) -> GroupsResourceWithRawResponse:
        return GroupsResourceWithRawResponse(self._dmm.groups)


class AsyncDmmResourceWithRawResponse:
    def __init__(self, dmm: AsyncDmmResource) -> None:
        self._dmm = dmm

        self.list_failed_autosettlement = async_to_raw_response_wrapper(
            dmm.list_failed_autosettlement,
        )
        self.list_rankings = async_to_raw_response_wrapper(
            dmm.list_rankings,
        )

    @cached_property
    def tournaments(self) -> AsyncTournamentsResourceWithRawResponse:
        return AsyncTournamentsResourceWithRawResponse(self._dmm.tournaments)

    @cached_property
    def relationships(self) -> AsyncRelationshipsResourceWithRawResponse:
        return AsyncRelationshipsResourceWithRawResponse(self._dmm.relationships)

    @cached_property
    def icims(self) -> AsyncIcimsResourceWithRawResponse:
        return AsyncIcimsResourceWithRawResponse(self._dmm.icims)

    @cached_property
    def trader_analytics(self) -> AsyncTraderAnalyticsResourceWithRawResponse:
        return AsyncTraderAnalyticsResourceWithRawResponse(self._dmm.trader_analytics)

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithRawResponse:
        return AsyncGroupsResourceWithRawResponse(self._dmm.groups)


class DmmResourceWithStreamingResponse:
    def __init__(self, dmm: DmmResource) -> None:
        self._dmm = dmm

        self.list_failed_autosettlement = to_streamed_response_wrapper(
            dmm.list_failed_autosettlement,
        )
        self.list_rankings = to_streamed_response_wrapper(
            dmm.list_rankings,
        )

    @cached_property
    def tournaments(self) -> TournamentsResourceWithStreamingResponse:
        return TournamentsResourceWithStreamingResponse(self._dmm.tournaments)

    @cached_property
    def relationships(self) -> RelationshipsResourceWithStreamingResponse:
        return RelationshipsResourceWithStreamingResponse(self._dmm.relationships)

    @cached_property
    def icims(self) -> IcimsResourceWithStreamingResponse:
        return IcimsResourceWithStreamingResponse(self._dmm.icims)

    @cached_property
    def trader_analytics(self) -> TraderAnalyticsResourceWithStreamingResponse:
        return TraderAnalyticsResourceWithStreamingResponse(self._dmm.trader_analytics)

    @cached_property
    def groups(self) -> GroupsResourceWithStreamingResponse:
        return GroupsResourceWithStreamingResponse(self._dmm.groups)


class AsyncDmmResourceWithStreamingResponse:
    def __init__(self, dmm: AsyncDmmResource) -> None:
        self._dmm = dmm

        self.list_failed_autosettlement = async_to_streamed_response_wrapper(
            dmm.list_failed_autosettlement,
        )
        self.list_rankings = async_to_streamed_response_wrapper(
            dmm.list_rankings,
        )

    @cached_property
    def tournaments(self) -> AsyncTournamentsResourceWithStreamingResponse:
        return AsyncTournamentsResourceWithStreamingResponse(self._dmm.tournaments)

    @cached_property
    def relationships(self) -> AsyncRelationshipsResourceWithStreamingResponse:
        return AsyncRelationshipsResourceWithStreamingResponse(self._dmm.relationships)

    @cached_property
    def icims(self) -> AsyncIcimsResourceWithStreamingResponse:
        return AsyncIcimsResourceWithStreamingResponse(self._dmm.icims)

    @cached_property
    def trader_analytics(self) -> AsyncTraderAnalyticsResourceWithStreamingResponse:
        return AsyncTraderAnalyticsResourceWithStreamingResponse(self._dmm.trader_analytics)

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithStreamingResponse:
        return AsyncGroupsResourceWithStreamingResponse(self._dmm.groups)
