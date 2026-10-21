# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable

from ...._types import Body, Query, Headers, NotGiven, not_given
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
from ....types.dmm.tournaments.designated_market_maker_settlement_override_preview import (
    DesignatedMarketMakerSettlementOverridePreview,
)
from ....types.dmm.tournaments import settlement_override_create_preview_params, settlement_override_create_params
from ....types.dmm.tournaments.designated_market_maker_settlement_override_execution import (
    DesignatedMarketMakerSettlementOverrideExecution,
)

__all__ = ["SettlementOverridesResource", "AsyncSettlementOverridesResource"]


class SettlementOverridesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SettlementOverridesResourceWithRawResponse:
        return SettlementOverridesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettlementOverridesResourceWithStreamingResponse:
        return SettlementOverridesResourceWithStreamingResponse(self)

    def create_preview(
        self,
        slug: str,
        *,
        reason: str,
        overrides: Iterable[settlement_override_create_preview_params.Override],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerSettlementOverridePreview:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Non-mutating preview for retrospective settlement valuation corrections after tournament end-settlement has already paid out an exchange. The API key needs the admin scope, and its owner must be a platform administrator or an owner/admin of the tournament's organization. An explicitly organization-bound key is restricted to that organization. Only ended tournaments are eligible. Each target exchange must already be closed out with no open tournament holdings. Use this endpoint to review per-member deltas before calling the execute endpoint.

        Args:
            slug: Tournament slug.
            reason: Operator-visible audit reason stored on every correction transaction.
            overrides: Batch of exchange corrections within this one tournament. Duplicate exchange IDs are rejected.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerSettlementOverridePreview: Correction preview payload.

        Example:
            ```python
            settlement_override = client.dmm.tournaments.settlement_overrides.create_preview(
                slug="alpha-tournament",
                reason="Corrected official final valuation from settlement desk review.",
                overrides=[{"exchange_id": "1234", "price": 0.75}],
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._post(
            path_template("/dmm/tournaments/{slug}/settlement-overrides/preview", **{"slug": slug}),
            body=maybe_transform(
                {
                    "reason": reason,
                    "overrides": overrides,
                },
                settlement_override_create_preview_params.SettlementOverrideCreatePreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DesignatedMarketMakerSettlementOverridePreview,
        )

    def create(
        self,
        slug: str,
        *,
        reason: str,
        overrides: Iterable[settlement_override_create_params.Override],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerSettlementOverrideExecution:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Atomically applies retrospective settlement valuation corrections after tournament end-settlement has already paid out an exchange. The API key needs the admin scope, and its owner must be a platform administrator or an owner/admin of the tournament's organization. An explicitly organization-bound key is restricted to that organization. Execution writes signed MARKET_SETTLEMENT_CORRECTION audit rows, increments affected tournament-member balances, updates exchange valuation state, and refreshes downstream tournament portfolio snapshots at the original tournament end date. Concurrent corrections for the same tournament/exchanges are serialized.

        Args:
            slug: Tournament slug.
            reason: Operator-visible audit reason stored on every correction transaction.
            overrides: Batch of exchange corrections within this one tournament. Duplicate exchange IDs are rejected.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerSettlementOverrideExecution: Correction applied atomically.

        Example:
            ```python
            settlement_override = client.dmm.tournaments.settlement_overrides.create(
                slug="alpha-tournament",
                reason="Corrected official final valuation from settlement desk review.",
                overrides=[{"exchange_id": "1234", "price": 0.75}],
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._post(
            path_template("/dmm/tournaments/{slug}/settlement-overrides", **{"slug": slug}),
            body=maybe_transform(
                {
                    "reason": reason,
                    "overrides": overrides,
                },
                settlement_override_create_params.SettlementOverrideCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DesignatedMarketMakerSettlementOverrideExecution,
        )


class AsyncSettlementOverridesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSettlementOverridesResourceWithRawResponse:
        return AsyncSettlementOverridesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettlementOverridesResourceWithStreamingResponse:
        return AsyncSettlementOverridesResourceWithStreamingResponse(self)

    async def create_preview(
        self,
        slug: str,
        *,
        reason: str,
        overrides: Iterable[settlement_override_create_preview_params.Override],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerSettlementOverridePreview:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Non-mutating preview for retrospective settlement valuation corrections after tournament end-settlement has already paid out an exchange. The API key needs the admin scope, and its owner must be a platform administrator or an owner/admin of the tournament's organization. An explicitly organization-bound key is restricted to that organization. Only ended tournaments are eligible. Each target exchange must already be closed out with no open tournament holdings. Use this endpoint to review per-member deltas before calling the execute endpoint.

        Args:
            slug: Tournament slug.
            reason: Operator-visible audit reason stored on every correction transaction.
            overrides: Batch of exchange corrections within this one tournament. Duplicate exchange IDs are rejected.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerSettlementOverridePreview: Correction preview payload.

        Example:
            ```python
            settlement_override = await client.dmm.tournaments.settlement_overrides.create_preview(
                slug="alpha-tournament",
                reason="Corrected official final valuation from settlement desk review.",
                overrides=[{"exchange_id": "1234", "price": 0.75}],
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._post(
            path_template("/dmm/tournaments/{slug}/settlement-overrides/preview", **{"slug": slug}),
            body=await async_maybe_transform(
                {
                    "reason": reason,
                    "overrides": overrides,
                },
                settlement_override_create_preview_params.SettlementOverrideCreatePreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DesignatedMarketMakerSettlementOverridePreview,
        )

    async def create(
        self,
        slug: str,
        *,
        reason: str,
        overrides: Iterable[settlement_override_create_params.Override],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerSettlementOverrideExecution:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Atomically applies retrospective settlement valuation corrections after tournament end-settlement has already paid out an exchange. The API key needs the admin scope, and its owner must be a platform administrator or an owner/admin of the tournament's organization. An explicitly organization-bound key is restricted to that organization. Execution writes signed MARKET_SETTLEMENT_CORRECTION audit rows, increments affected tournament-member balances, updates exchange valuation state, and refreshes downstream tournament portfolio snapshots at the original tournament end date. Concurrent corrections for the same tournament/exchanges are serialized.

        Args:
            slug: Tournament slug.
            reason: Operator-visible audit reason stored on every correction transaction.
            overrides: Batch of exchange corrections within this one tournament. Duplicate exchange IDs are rejected.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerSettlementOverrideExecution: Correction applied atomically.

        Example:
            ```python
            settlement_override = await client.dmm.tournaments.settlement_overrides.create(
                slug="alpha-tournament",
                reason="Corrected official final valuation from settlement desk review.",
                overrides=[{"exchange_id": "1234", "price": 0.75}],
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._post(
            path_template("/dmm/tournaments/{slug}/settlement-overrides", **{"slug": slug}),
            body=await async_maybe_transform(
                {
                    "reason": reason,
                    "overrides": overrides,
                },
                settlement_override_create_params.SettlementOverrideCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DesignatedMarketMakerSettlementOverrideExecution,
        )


class SettlementOverridesResourceWithRawResponse:
    def __init__(self, settlement_overrides: SettlementOverridesResource) -> None:
        self._settlement_overrides = settlement_overrides

        self.create_preview = to_raw_response_wrapper(
            settlement_overrides.create_preview,
        )
        self.create = to_raw_response_wrapper(
            settlement_overrides.create,
        )


class AsyncSettlementOverridesResourceWithRawResponse:
    def __init__(self, settlement_overrides: AsyncSettlementOverridesResource) -> None:
        self._settlement_overrides = settlement_overrides

        self.create_preview = async_to_raw_response_wrapper(
            settlement_overrides.create_preview,
        )
        self.create = async_to_raw_response_wrapper(
            settlement_overrides.create,
        )


class SettlementOverridesResourceWithStreamingResponse:
    def __init__(self, settlement_overrides: SettlementOverridesResource) -> None:
        self._settlement_overrides = settlement_overrides

        self.create_preview = to_streamed_response_wrapper(
            settlement_overrides.create_preview,
        )
        self.create = to_streamed_response_wrapper(
            settlement_overrides.create,
        )


class AsyncSettlementOverridesResourceWithStreamingResponse:
    def __init__(self, settlement_overrides: AsyncSettlementOverridesResource) -> None:
        self._settlement_overrides = settlement_overrides

        self.create_preview = async_to_streamed_response_wrapper(
            settlement_overrides.create_preview,
        )
        self.create = async_to_streamed_response_wrapper(
            settlement_overrides.create,
        )
