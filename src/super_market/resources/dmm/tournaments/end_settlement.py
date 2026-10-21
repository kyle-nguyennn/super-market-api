# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable

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
from ....types.dmm.tournaments.designated_market_maker_end_settlement_preview import (
    DesignatedMarketMakerEndSettlementPreview,
)
from ....types.dmm.tournaments.designated_market_maker_end_settlement_queue import (
    DesignatedMarketMakerEndSettlementQueue,
)
from ....types.dmm.tournaments import end_settlement_create_params
from ....types.dmm.tournaments.designated_market_maker_settlement_status import DesignatedMarketMakerSettlementStatus

__all__ = ["EndSettlementResource", "AsyncEndSettlementResource"]


class EndSettlementResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EndSettlementResourceWithRawResponse:
        return EndSettlementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EndSettlementResourceWithStreamingResponse:
        return EndSettlementResourceWithStreamingResponse(self)

    def list(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerEndSettlementPreview:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Preview prices for closing out tournament-scoped positions in markets that haven't yet resolved at tournament end. Review before calling POST. Available only once the tournament has ended.

        Per exchange: `proposedPrice` (5h VWAP default), `proposedPriceSource` (`vwap` / `cfmm_pool` / `seed` / `backfilled` / `admin_override` / `dmm_submission` / `missing` — treat `seed`/`missing` with suspicion), `lastTradePrice` (for divergence-spotting), and `needsSubmittedPrice` (`true` when engine trading activity or nonzero app holdings exist without a valuation: POST must supply a `submittedPrices` row for that exchange). Untraded tournament scopes with no app holdings are reset automatically during closeout.

        Args:
            slug: Tournament slug.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerEndSettlementPreview: Preview payload.

        Example:
            ```python
            end_settlement = client.dmm.tournaments.end_settlement.list(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/dmm/tournaments/{slug}/end-settlement", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DesignatedMarketMakerEndSettlementPreview,
        )

    def create(
        self,
        slug: str,
        *,
        submitted_prices: Iterable[end_settlement_create_params.SubmittedPrice] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerEndSettlementQueue:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Queues the strict tournament end-settlement closeout. The worker writes submitted missing final prices, cancels open tournament orders, settles tournament-scoped engine positions and app holdings, deletes app holdings and position lots, enqueues untraded-scope resets in the transactional engine outbox, and refreshes the final snapshot in one all-or-failed transaction. The POST response is `202 Accepted` after the background event is dispatched; use the status endpoint to poll lifecycle progress.

        Exchanges flagged `needsSubmittedPrice` in the preview must be supplied in `submittedPrices`; boundary prices 0 and 1 are accepted. A `resolved_outcomes` tournament with unresolved attached markets returns a 409 `awaiting_market_resolution` response with the unresolved market list. Submitting prices for exchanges that already have a proposed valuation returns 409. Already settled tournaments reject another initial end-settlement command; use retrospective settlement overrides after payout.

        Args:
            slug: Tournament slug.
            submitted_prices: Submitted prices for exchanges flagged with `needsSubmittedPrice` in the GET preview. Accepted only when the tournament scope has engine trading activity or nonzero app holdings and no final valuation price.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerEndSettlementQueue: Settlement queued, or an active settlement attempt already exists.

        Example:
            ```python
            end_settlement = client.dmm.tournaments.end_settlement.create(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._post(
            path_template("/dmm/tournaments/{slug}/end-settlement", **{"slug": slug}),
            body=maybe_transform(
                {"submitted_prices": submitted_prices},
                end_settlement_create_params.EndSettlementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DesignatedMarketMakerEndSettlementQueue,
        )

    def list_status(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerSettlementStatus:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Returns the current asynchronous final-settlement lifecycle and redacted attempt view for an ended tournament. DMM responses expose safe aggregate status, missing-price blockers, retry/action flags, and sanitized errors; they do not expose stack traces, member-level payout detail, or raw API-key identifiers.

        Args:
            slug: Tournament slug.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerSettlementStatus: Settlement lifecycle status.

        Example:
            ```python
            end_settlement = client.dmm.tournaments.end_settlement.list_status(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/dmm/tournaments/{slug}/end-settlement/status", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DesignatedMarketMakerSettlementStatus,
        )


class AsyncEndSettlementResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEndSettlementResourceWithRawResponse:
        return AsyncEndSettlementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEndSettlementResourceWithStreamingResponse:
        return AsyncEndSettlementResourceWithStreamingResponse(self)

    async def list(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerEndSettlementPreview:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Preview prices for closing out tournament-scoped positions in markets that haven't yet resolved at tournament end. Review before calling POST. Available only once the tournament has ended.

        Per exchange: `proposedPrice` (5h VWAP default), `proposedPriceSource` (`vwap` / `cfmm_pool` / `seed` / `backfilled` / `admin_override` / `dmm_submission` / `missing` — treat `seed`/`missing` with suspicion), `lastTradePrice` (for divergence-spotting), and `needsSubmittedPrice` (`true` when engine trading activity or nonzero app holdings exist without a valuation: POST must supply a `submittedPrices` row for that exchange). Untraded tournament scopes with no app holdings are reset automatically during closeout.

        Args:
            slug: Tournament slug.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerEndSettlementPreview: Preview payload.

        Example:
            ```python
            end_settlement = await client.dmm.tournaments.end_settlement.list(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/dmm/tournaments/{slug}/end-settlement", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DesignatedMarketMakerEndSettlementPreview,
        )

    async def create(
        self,
        slug: str,
        *,
        submitted_prices: Iterable[end_settlement_create_params.SubmittedPrice] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerEndSettlementQueue:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Queues the strict tournament end-settlement closeout. The worker writes submitted missing final prices, cancels open tournament orders, settles tournament-scoped engine positions and app holdings, deletes app holdings and position lots, enqueues untraded-scope resets in the transactional engine outbox, and refreshes the final snapshot in one all-or-failed transaction. The POST response is `202 Accepted` after the background event is dispatched; use the status endpoint to poll lifecycle progress.

        Exchanges flagged `needsSubmittedPrice` in the preview must be supplied in `submittedPrices`; boundary prices 0 and 1 are accepted. A `resolved_outcomes` tournament with unresolved attached markets returns a 409 `awaiting_market_resolution` response with the unresolved market list. Submitting prices for exchanges that already have a proposed valuation returns 409. Already settled tournaments reject another initial end-settlement command; use retrospective settlement overrides after payout.

        Args:
            slug: Tournament slug.
            submitted_prices: Submitted prices for exchanges flagged with `needsSubmittedPrice` in the GET preview. Accepted only when the tournament scope has engine trading activity or nonzero app holdings and no final valuation price.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerEndSettlementQueue: Settlement queued, or an active settlement attempt already exists.

        Example:
            ```python
            end_settlement = await client.dmm.tournaments.end_settlement.create(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._post(
            path_template("/dmm/tournaments/{slug}/end-settlement", **{"slug": slug}),
            body=await async_maybe_transform(
                {"submitted_prices": submitted_prices},
                end_settlement_create_params.EndSettlementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DesignatedMarketMakerEndSettlementQueue,
        )

    async def list_status(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerSettlementStatus:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Returns the current asynchronous final-settlement lifecycle and redacted attempt view for an ended tournament. DMM responses expose safe aggregate status, missing-price blockers, retry/action flags, and sanitized errors; they do not expose stack traces, member-level payout detail, or raw API-key identifiers.

        Args:
            slug: Tournament slug.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerSettlementStatus: Settlement lifecycle status.

        Example:
            ```python
            end_settlement = await client.dmm.tournaments.end_settlement.list_status(
                slug="alpha-tournament",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/dmm/tournaments/{slug}/end-settlement/status", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DesignatedMarketMakerSettlementStatus,
        )


class EndSettlementResourceWithRawResponse:
    def __init__(self, end_settlement: EndSettlementResource) -> None:
        self._end_settlement = end_settlement

        self.list = to_raw_response_wrapper(
            end_settlement.list,
        )
        self.create = to_raw_response_wrapper(
            end_settlement.create,
        )
        self.list_status = to_raw_response_wrapper(
            end_settlement.list_status,
        )


class AsyncEndSettlementResourceWithRawResponse:
    def __init__(self, end_settlement: AsyncEndSettlementResource) -> None:
        self._end_settlement = end_settlement

        self.list = async_to_raw_response_wrapper(
            end_settlement.list,
        )
        self.create = async_to_raw_response_wrapper(
            end_settlement.create,
        )
        self.list_status = async_to_raw_response_wrapper(
            end_settlement.list_status,
        )


class EndSettlementResourceWithStreamingResponse:
    def __init__(self, end_settlement: EndSettlementResource) -> None:
        self._end_settlement = end_settlement

        self.list = to_streamed_response_wrapper(
            end_settlement.list,
        )
        self.create = to_streamed_response_wrapper(
            end_settlement.create,
        )
        self.list_status = to_streamed_response_wrapper(
            end_settlement.list_status,
        )


class AsyncEndSettlementResourceWithStreamingResponse:
    def __init__(self, end_settlement: AsyncEndSettlementResource) -> None:
        self._end_settlement = end_settlement

        self.list = async_to_streamed_response_wrapper(
            end_settlement.list,
        )
        self.create = async_to_streamed_response_wrapper(
            end_settlement.create,
        )
        self.list_status = async_to_streamed_response_wrapper(
            end_settlement.list_status,
        )
