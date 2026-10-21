# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable, Union
from typing_extensions import Literal, overload

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform, strip_not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.dmm.tournaments.designated_market_maker_liquidity import DesignatedMarketMakerLiquidity
from ....types.dmm.tournaments.designated_market_maker_liquidity_level_param import (
    DesignatedMarketMakerLiquidityLevelParam,
)
from ....types.dmm.tournaments import exchange_create_liquidity_params
from ....types.dmm.tournaments.exchange_delete_liquidity_response import ExchangeDeleteLiquidityResponse

__all__ = ["ExchangesResource", "AsyncExchangesResource"]


class ExchangesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExchangesResourceWithRawResponse:
        return ExchangesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExchangesResourceWithStreamingResponse:
        return ExchangesResourceWithStreamingResponse(self)

    @overload
    def create_liquidity(
        self,
        exchange_id: str,
        *,
        slug: str,
        mode: Literal["append"],
        operation_key: str,
        bids: Iterable[DesignatedMarketMakerLiquidityLevelParam] | Omit = omit,
        asks: Iterable[DesignatedMarketMakerLiquidityLevelParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerLiquidity: ...

    @overload
    def create_liquidity(
        self,
        exchange_id: str,
        *,
        slug: str,
        mode: Literal["replace"],
        operation_key: str,
        bids: Iterable[DesignatedMarketMakerLiquidityLevelParam] | Omit = omit,
        asks: Iterable[DesignatedMarketMakerLiquidityLevelParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerLiquidity: ...

    def create_liquidity(
        self,
        exchange_id: str,
        *,
        slug: str,
        mode: Union[Literal["append"], Literal["replace"]],
        operation_key: str,
        bids: Iterable[DesignatedMarketMakerLiquidityLevelParam] | Omit = omit,
        asks: Iterable[DesignatedMarketMakerLiquidityLevelParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerLiquidity:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Endpoint for appending or replacing managed market-maker liquidity on one P2P tournament exchange orderbook. The API key needs the admin scope, and its owner must be a platform administrator or an owner/admin of the organization that owns the tournament. An explicitly organization-bound key is restricted to that organization. Submitted levels can match executable user liquidity, but market-maker self-matching is rejected. `append` and `replace` each require a client-supplied `operationKey` on both engine and legacy paths; retry the same mode and payload with the same key for replay, and expect 409 if that mode's key is reused with a changed payload. A completed request replays its stored status and body, so a stored 400, 404, or 409 outcome (for example an engine rejection or a closed market) is returned again for the same key and payload; send a new key once the cause is fixed. Retryable 503 outcomes are not stored. The key namespace is per operation type, so `append:K` and `replace:K` are independent and may both execute. For `replace`, existing rungs with the same side, price, and remaining quantity are retained with their order IDs and queue priority. Only changed or removed rungs are cancelled, so an identical re-quote is a no-op. `replace` may submit an empty book to clear managed liquidity; `append` must include at least one level. Prices must be unique per side, and submitted bids and asks must not cross: a highest bid at or above the lowest ask returns 400.

        Args:
            exchange_id: Exchange ID as a numeric string.
            slug: Tournament slug.
            mode: Body parameter.
            operation_key: Required client-supplied idempotency key for append retries on both engine and legacy paths. An identical payload replays the stored status and body of the completed request, including a stored 400, 404, or 409 error; after fixing the cause, retry with a new key. A changed payload returns 409. Append and replace use independent key namespaces, so the same key may be used once for each mode.
            bids: Outcome-perspective bid levels. Prices must be unique. Executed from highest price to lowest price.
            asks: Outcome-perspective ask levels. Prices must be unique. Executed from lowest price to highest price.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerLiquidity: Liquidity operation applied atomically.

        Example:
            ```python
            exchange = client.dmm.tournaments.exchanges.create_liquidity(
                slug="alpha-tournament",
                exchange_id="36",
                mode="append",
                operation_key="jerry-liquidity-2026-07-15-001",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if exchange_id is None or (isinstance(exchange_id, str) and not exchange_id):
            raise ValueError(f"Expected a non-empty value for `exchange_id` but received {exchange_id!r}")
        return self._post(
            path_template(
                "/dmm/tournaments/{slug}/exchanges/{exchangeId}/liquidity", **{"slug": slug, "exchangeId": exchange_id}
            ),
            body=maybe_transform(
                {
                    "mode": mode,
                    "operation_key": operation_key,
                    "bids": bids,
                    "asks": asks,
                },
                exchange_create_liquidity_params.ExchangeCreateLiquidityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DesignatedMarketMakerLiquidity,
        )

    def delete_liquidity(
        self,
        exchange_id: str,
        *,
        slug: str,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExchangeDeleteLiquidityResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Emergency risk-off for one tournament exchange orderbook. Cancels every `market_maker`-owned open order on `(tournamentSlug, exchangeId)`. No-op when nothing is resting. Same admin / org-ownership gates as the POST. The optional `Idempotency-Key` header identifies the sweep for safe retries; omission makes every request a new sweep.

        Args:
            exchange_id: Exchange ID as a numeric string.
            slug: Tournament slug.
            idempotency_key: Optional in this staged release. Reuse the same key only to retry the same sweep. On engine-routed tournaments, a retry with the same key reuses the original engine command and returns the original `sweptOrders` instead of sweeping again. A retry still passes the same checks as a new sweep: if the tournament has since ended or been archived, the market has settled, or engine synchronization is pending, the retry gets that 409 or 503 instead of the original result. Reusing a key for a different exchange or tournament returns 409. Omitting the header makes every request a new sweep.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ExchangeDeleteLiquidityResponse: Sweep applied.

        Example:
            ```python
            exchange = client.dmm.tournaments.exchanges.delete_liquidity(
                slug="alpha-tournament",
                exchange_id="36",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if exchange_id is None or (isinstance(exchange_id, str) and not exchange_id):
            raise ValueError(f"Expected a non-empty value for `exchange_id` but received {exchange_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._delete(
            path_template(
                "/dmm/tournaments/{slug}/exchanges/{exchangeId}/liquidity", **{"slug": slug, "exchangeId": exchange_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExchangeDeleteLiquidityResponse,
        )


class AsyncExchangesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExchangesResourceWithRawResponse:
        return AsyncExchangesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExchangesResourceWithStreamingResponse:
        return AsyncExchangesResourceWithStreamingResponse(self)

    @overload
    async def create_liquidity(
        self,
        exchange_id: str,
        *,
        slug: str,
        mode: Literal["append"],
        operation_key: str,
        bids: Iterable[DesignatedMarketMakerLiquidityLevelParam] | Omit = omit,
        asks: Iterable[DesignatedMarketMakerLiquidityLevelParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerLiquidity: ...

    @overload
    async def create_liquidity(
        self,
        exchange_id: str,
        *,
        slug: str,
        mode: Literal["replace"],
        operation_key: str,
        bids: Iterable[DesignatedMarketMakerLiquidityLevelParam] | Omit = omit,
        asks: Iterable[DesignatedMarketMakerLiquidityLevelParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerLiquidity: ...

    async def create_liquidity(
        self,
        exchange_id: str,
        *,
        slug: str,
        mode: Union[Literal["append"], Literal["replace"]],
        operation_key: str,
        bids: Iterable[DesignatedMarketMakerLiquidityLevelParam] | Omit = omit,
        asks: Iterable[DesignatedMarketMakerLiquidityLevelParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignatedMarketMakerLiquidity:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Endpoint for appending or replacing managed market-maker liquidity on one P2P tournament exchange orderbook. The API key needs the admin scope, and its owner must be a platform administrator or an owner/admin of the organization that owns the tournament. An explicitly organization-bound key is restricted to that organization. Submitted levels can match executable user liquidity, but market-maker self-matching is rejected. `append` and `replace` each require a client-supplied `operationKey` on both engine and legacy paths; retry the same mode and payload with the same key for replay, and expect 409 if that mode's key is reused with a changed payload. A completed request replays its stored status and body, so a stored 400, 404, or 409 outcome (for example an engine rejection or a closed market) is returned again for the same key and payload; send a new key once the cause is fixed. Retryable 503 outcomes are not stored. The key namespace is per operation type, so `append:K` and `replace:K` are independent and may both execute. For `replace`, existing rungs with the same side, price, and remaining quantity are retained with their order IDs and queue priority. Only changed or removed rungs are cancelled, so an identical re-quote is a no-op. `replace` may submit an empty book to clear managed liquidity; `append` must include at least one level. Prices must be unique per side, and submitted bids and asks must not cross: a highest bid at or above the lowest ask returns 400.

        Args:
            exchange_id: Exchange ID as a numeric string.
            slug: Tournament slug.
            mode: Body parameter.
            operation_key: Required client-supplied idempotency key for append retries on both engine and legacy paths. An identical payload replays the stored status and body of the completed request, including a stored 400, 404, or 409 error; after fixing the cause, retry with a new key. A changed payload returns 409. Append and replace use independent key namespaces, so the same key may be used once for each mode.
            bids: Outcome-perspective bid levels. Prices must be unique. Executed from highest price to lowest price.
            asks: Outcome-perspective ask levels. Prices must be unique. Executed from lowest price to highest price.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DesignatedMarketMakerLiquidity: Liquidity operation applied atomically.

        Example:
            ```python
            exchange = await client.dmm.tournaments.exchanges.create_liquidity(
                slug="alpha-tournament",
                exchange_id="36",
                mode="append",
                operation_key="jerry-liquidity-2026-07-15-001",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if exchange_id is None or (isinstance(exchange_id, str) and not exchange_id):
            raise ValueError(f"Expected a non-empty value for `exchange_id` but received {exchange_id!r}")
        return await self._post(
            path_template(
                "/dmm/tournaments/{slug}/exchanges/{exchangeId}/liquidity", **{"slug": slug, "exchangeId": exchange_id}
            ),
            body=await async_maybe_transform(
                {
                    "mode": mode,
                    "operation_key": operation_key,
                    "bids": bids,
                    "asks": asks,
                },
                exchange_create_liquidity_params.ExchangeCreateLiquidityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DesignatedMarketMakerLiquidity,
        )

    async def delete_liquidity(
        self,
        exchange_id: str,
        *,
        slug: str,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExchangeDeleteLiquidityResponse:
        """
        <p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

        Emergency risk-off for one tournament exchange orderbook. Cancels every `market_maker`-owned open order on `(tournamentSlug, exchangeId)`. No-op when nothing is resting. Same admin / org-ownership gates as the POST. The optional `Idempotency-Key` header identifies the sweep for safe retries; omission makes every request a new sweep.

        Args:
            exchange_id: Exchange ID as a numeric string.
            slug: Tournament slug.
            idempotency_key: Optional in this staged release. Reuse the same key only to retry the same sweep. On engine-routed tournaments, a retry with the same key reuses the original engine command and returns the original `sweptOrders` instead of sweeping again. A retry still passes the same checks as a new sweep: if the tournament has since ended or been archived, the market has settled, or engine synchronization is pending, the retry gets that 409 or 503 instead of the original result. Reusing a key for a different exchange or tournament returns 409. Omitting the header makes every request a new sweep.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ExchangeDeleteLiquidityResponse: Sweep applied.

        Example:
            ```python
            exchange = await client.dmm.tournaments.exchanges.delete_liquidity(
                slug="alpha-tournament",
                exchange_id="36",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if exchange_id is None or (isinstance(exchange_id, str) and not exchange_id):
            raise ValueError(f"Expected a non-empty value for `exchange_id` but received {exchange_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/dmm/tournaments/{slug}/exchanges/{exchangeId}/liquidity", **{"slug": slug, "exchangeId": exchange_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExchangeDeleteLiquidityResponse,
        )


class ExchangesResourceWithRawResponse:
    def __init__(self, exchanges: ExchangesResource) -> None:
        self._exchanges = exchanges

        self.create_liquidity = to_raw_response_wrapper(
            exchanges.create_liquidity,
        )
        self.delete_liquidity = to_raw_response_wrapper(
            exchanges.delete_liquidity,
        )


class AsyncExchangesResourceWithRawResponse:
    def __init__(self, exchanges: AsyncExchangesResource) -> None:
        self._exchanges = exchanges

        self.create_liquidity = async_to_raw_response_wrapper(
            exchanges.create_liquidity,
        )
        self.delete_liquidity = async_to_raw_response_wrapper(
            exchanges.delete_liquidity,
        )


class ExchangesResourceWithStreamingResponse:
    def __init__(self, exchanges: ExchangesResource) -> None:
        self._exchanges = exchanges

        self.create_liquidity = to_streamed_response_wrapper(
            exchanges.create_liquidity,
        )
        self.delete_liquidity = to_streamed_response_wrapper(
            exchanges.delete_liquidity,
        )


class AsyncExchangesResourceWithStreamingResponse:
    def __init__(self, exchanges: AsyncExchangesResource) -> None:
        self._exchanges = exchanges

        self.create_liquidity = async_to_streamed_response_wrapper(
            exchanges.create_liquidity,
        )
        self.delete_liquidity = async_to_streamed_response_wrapper(
            exchanges.delete_liquidity,
        )
