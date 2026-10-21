# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable, Union
from datetime import datetime
from typing_extensions import Literal

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.order_create_response import OrderCreateResponse
from ..types import (
    order_create_params,
    order_list_params,
    order_create_batch_params,
    order_create_multi_leg_params,
    order_create_cancel_all_params,
    order_list_fills_params,
)
from ..types.order_list_response import OrderListResponse
from ..types.order_create_batch_response import OrderCreateBatchResponse
from ..types.order_create_multi_leg_response import OrderCreateMultiLegResponse
from ..types.order import Order
from ..types.order_delete_response import OrderDeleteResponse
from ..types.order_create_cancel_all_response import OrderCreateCancelAllResponse
from ..types.order_list_fills_response import OrderListFillsResponse

__all__ = ["OrdersResource", "AsyncOrdersResource"]


class OrdersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrdersResourceWithRawResponse:
        return OrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrdersResourceWithStreamingResponse:
        return OrdersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        exchange_id: str,
        side: Literal["yes", "no"],
        action: Literal["buy", "sell"],
        quantity: int,
        price: float | Omit = omit,
        expiration_date: Union[str, datetime] | Omit = omit,
        tournament_id: str | Omit = omit,
        idempotency_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderCreateResponse:
        """
        Unaccepted current documents return 403 `TERMS_NOT_ACKNOWLEDGED` with `error.details.missingDocuments`; each entry contains `documentId`, `kind`, `version`, `organizationId`, `organizationSlug`, `organizationName`, `supportEmail`, `currencyName`, `url`, and `host`. Places a single limit or market order. A required client-supplied `idempotencyKey` identifies the logical placement: retrying the same key with the same resolved payload replays the exact stored response before mutable settlement or market preflights, while reuse with a different resolved payload returns 409. Fresh limit prices must be on the 0.005 tick between 0.005 and 0.995; `price: 1` for a buy and `price: 0` for a sell encode market orders, and off-tick values return 400 `VALIDATION_ERROR`. Omit `price` for a market order (fills at best available price). An organization-bound key defaults an omitted `tournamentId` to the organization's default tournament; an unbound key defaults to the public global context. On engine-routed scopes, an opposite-signed `BUY` nets against the existing position: it reduces or crosses the position at FIFO lot cost. Inspect `avgCost` and `lots` on the corresponding global or tournament portfolio-position read to understand the surviving position's display average and cost lots. On engine-routed scopes, a fully-backed `SELL` closes conventionally; a `SELL` that is flat, opposite the held side, or larger than the held quantity is canonicalized by the engine into its complement `BUY` (`sell yes q@p` ≡ `buy no q@(1−p)`), and the response's canonical `action`/`side`/`price`/`quantity` report the order as placed. Resting quotes on both sides are allowed; an order that would cross your own resting order fills other counterparties, then its crossing remainder is cancelled with `terminalReasonCode: "SelfTradePrevented"`. The nullable `all` response reports authoritative engine-calculated capital efficiency and collateral encumbrance for the execution. On engine-routed scopes a buy is admitted against your cash balance, and resting orders do not escrow cash: it moves only on fills. A buy the full balance cannot pay for even one share of is rejected with 400 `VALIDATION_ERROR` (insufficient funds). A buy is accepted as a no-op (`orderId: null`, `open: false`, nothing placed or traded) when your unexpired resting buys on the same exchange and tournament already commit the whole balance. Resting buys on other exchanges are not counted, so your resting buys across exchanges can add up to more than your balance. An order's resting remainder is sized to what your full current balance can cover, and a later balance decrease shrinks or cancels resting buys you can no longer afford. Buying the outcome opposite a position you hold nets the shares and credits 1 per netted share, so your balance change differs from `totalCost`.

        Args:
            exchange_id: Exchange ID as a numeric string.
            side: Body parameter.
            action: Body parameter.
            quantity: Number of shares, at most 2147483647 (the trading engine holds quantities as a signed 32-bit integer). Larger values are rejected with `VALIDATION_ERROR`.
            price: Limit price in [0, 1]. Limit prices must be on the 0.005 tick between 0.005 and 0.995. `1` with `action: "buy"` and `0` with `action: "sell"` mean a market order; omit `price` for a market order. Off-tick values are rejected with `VALIDATION_ERROR`.
            expiration_date: Optional future ISO 8601 datetime after which the limit order expires. Not supported for market orders.
            tournament_id: When provided, routes the order through that accessible tournament's isolated orderbook and balance. A first order in an open tournament, or by an owner or admin in any tournament of their organization, enrols the caller. When omitted, an organization-bound key uses its organization's default tournament; an unbound key uses the public global context.
            idempotency_key: Required client-supplied idempotency key. Reuse this key only when retrying the same logical request. An identical resolved payload replays the exact stored response; reuse with a different resolved payload returns 409.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrderCreateResponse: Order placed.

        Example:
            ```python
            order = client.orders.create(
                exchange_id="36",
                side="yes",
                action="buy",
                quantity=100,
                idempotency_key="order-placement-2026-07-23-001",
            )
            ```
        """
        return self._post(
            "/orders",
            body=maybe_transform(
                {
                    "exchange_id": exchange_id,
                    "side": side,
                    "action": action,
                    "quantity": quantity,
                    "price": price,
                    "expiration_date": expiration_date,
                    "tournament_id": tournament_id,
                    "idempotency_key": idempotency_key,
                },
                order_create_params.OrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderCreateResponse,
        )

    def list(
        self,
        *,
        status: Literal["open", "closed", "expired", "all"] | Omit = omit,
        exchange_id: str | Omit = omit,
        market_id: str | Omit = omit,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        tournament_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderListResponse:
        """
        Returns the authenticated user's orders. Defaults to open orders only. When `tournamentId` is omitted, an organization-bound key reads its organization's default tournament orders and an unbound key reads public global orders. Engine-backed responses include projection `coverage` metadata.

        Args:
            status: Filter by order status. `open` — resting orders that have not expired. `closed` — filled, cancelled, or expired orders. `expired` — legacy orders still stored as open but past their `expirationDate`, plus engine orders cancelled with reason `Expired` (reporting terminal reason code `Expired`). `all` — no filter.
            exchange_id: Filter to a specific exchange.
            market_id: Filter to all exchanges in a market.
            limit: Results per page (max 200).
            cursor: Pagination cursor from a previous response.
            tournament_id: Filter to orders placed in a specific accessible tournament. Omit to use the organization's default tournament for an organization-bound key or public global orders for an unbound key.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrderListResponse: Paginated list of orders.

        Example:
            ```python
            order = client.orders.list(
                status="open",
                limit=50,
            )
            ```
        """
        return self._get(
            "/orders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "status": status,
                        "exchange_id": exchange_id,
                        "market_id": market_id,
                        "limit": limit,
                        "cursor": cursor,
                        "tournament_id": tournament_id,
                    },
                    order_list_params.OrderListParams,
                ),
            ),
            cast_to=OrderListResponse,
        )

    def create_batch(
        self,
        *,
        idempotency_key: str,
        orders: Iterable[order_create_batch_params.Order],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderCreateBatchResponse:
        """
        Consent is checked per item: an unaccepted current document returns item status 403 with `data.error.code: TERMS_NOT_ACKNOWLEDGED` and `data.error.details.missingDocuments`. Other items can succeed. Places up to 50 orders in a single request under one required client-supplied `idempotencyKey`. For requests first bound after the original-routing rollout is enabled, completed batches retain each originally omitted tournament scope across organization default changes and backend routing changes; older requests without routing evidence retain their existing conflict behavior. Incomplete batches retain their original scope/backend retry fences. Reusing a key from another authenticated organization conflicts. The ordered, resolved batch is the request identity: a completed retry with the same key and payload replays the exact stored 200, 207, or 422 envelope without placing another order, while reuse with a different batch returns 409. Freshly executed engine-routed items report the canonical `action`/`side`/`price`/`quantity`/`terminalReasonCode` as placed; items stored before this change replay without those fields. If any item returns 429 or 5xx, the outer batch remains incomplete; retry with the same key to replay terminal indexes and resume only those non-terminal indexes. Orders are placed one at a time under a bounded execution budget: a batch that cannot finish within it stops issuing further orders and returns 503, keeping every order it already placed — retry with the same key to resume from where it stopped, as many times as needed until a final 200, 207, or 422. Large batches under heavy load are the case that reaches this. A batch with at least one success returns 207 with per-item statuses even when another item is transient. An item rate limited by the trading engine reports status 429 with `data.code: RATE_LIMITED`; nothing was placed for it. A failed item's `data` keeps the error payload of the placement path that rejected it rather than the top-level error envelope: commonly a bare `{ error: "…" }`, sometimes with a `code`; rate-limited items use `{ code: "RATE_LIMITED", error: "…" }`; and consent failures use `{ error: { code, message, details } }`. A zero-success batch returns 429 with the per-item results when every item was rate limited, 502 with per-item `ORDER_STATUS_UNKNOWN` codes when every item has an unknown dispatch outcome, and 503 for any other zero-success batch with a transient item, including a mix of terminal failures and rate-limited items. When a rate-limited item supplied a `Retry-After`, the 207, 429, or 503 response carries the longest one; it may be absent otherwise. After a completed 207, resubmit failed items under a new batch key. Fresh limit prices must be on the 0.005 tick between 0.005 and 0.995; `price: 1` for a buy and `price: 0` for a sell encode market orders, and off-tick values return 400 `VALIDATION_ERROR`. For an organization-bound key, each order that omits `tournamentId` defaults to the organization's default tournament; unbound keys retain the public global default. All orders are validated upfront — if any fail validation the entire request is rejected with 400 before any orders are placed. Execution is best-effort: each order is attempted independently and a failure does not roll back already-placed orders. Use /orders/multi-leg instead if you need an all-or-nothing guarantee. Returns 200 if all succeed, 207 when at least one succeeds and at least one fails (207 does not mean partial fills), 422 if all fail terminally, 429 if every item was rate limited, 502 if every item has an unknown dispatch outcome, or 503 when no item succeeds and another transient outcome remains or the batch stopped at its execution budget with orders still unissued.

        Args:
            idempotency_key: Required client-supplied idempotency key. Reuse this key only when retrying the same logical request. An identical resolved payload replays the exact stored response; reuse with a different resolved payload returns 409.
            orders: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrderCreateBatchResponse: All orders succeeded.

        Example:
            ```python
            order = client.orders.create_batch(
                idempotency_key="batch-placement-2026-07-23-001",
                orders=[
                    {"exchangeId": "36", "side": "yes", "action": "buy", "quantity": 100, "price": 0.42},
                    {
                        "exchangeId": "37",
                        "side": "no",
                        "action": "buy",
                        "quantity": 50,
                        "price": 0.3,
                        "tournamentId": "550e8400-e29b-41d4-a716-446655440000",
                    },
                ],
            )
            ```
        """
        return self._post(
            "/orders/batch",
            body=maybe_transform(
                {
                    "idempotency_key": idempotency_key,
                    "orders": orders,
                },
                order_create_batch_params.OrderCreateBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderCreateBatchResponse,
        )

    def create_multi_leg(
        self,
        *,
        legs: Iterable[order_create_multi_leg_params.Leg],
        idempotency_key: str,
        relationship_constraint: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderCreateMultiLegResponse:
        """
        Unaccepted current documents return 403 `TERMS_NOT_ACKNOWLEDGED` with `error.details.missingDocuments`; each entry contains `documentId`, `kind`, `version`, `organizationId`, `organizationSlug`, `organizationName`, `supportEmail`, `currencyName`, `url`, and `host`. Consent preflight checks the union of documents required by all legs before any leg executes. Places up to 10 orders atomically within a single transaction. For requests first bound after the original-routing rollout is enabled, a completed response retains originally omitted tournament scopes across organization default and backend changes. Ordered legs, explicit scope, relationshipConstraint, economics and original authenticated organization still identify the retry. Historical requests without routing evidence keep existing scope conflicts; incomplete requests retain their leases and backend routing fences. A required client-supplied `idempotencyKey` identifies the logical placement: the same key with the same resolved legs and constraint has no second economic effect in either scope, while reuse with a different payload returns 409. Fresh limit prices must be on the 0.005 tick between 0.005 and 0.995; `price: 1` for a buy and `price: 0` for a sell encode market orders, and off-tick values return 400 `VALIDATION_ERROR`. For an organization-bound key, each leg that omits `tournamentId` defaults to the organization's default tournament; unbound keys retain the public global default. All legs succeed or none are persisted — if any leg fails, the entire request rolls back and no orders are placed. Every leg must route to the same backend: a request mixing engine-routed and non-engine scopes returns 400 `VALIDATION_ERROR`. Engine-routed legs must all belong to the same organization; otherwise the request returns 400 `VALIDATION_ERROR`. Optional `relationshipConstraint` validates every leg against one active canonical ALL relationship using an engine preflight price snapshot taken immediately before dispatch. This validation is not held under the engine execution lock or re-evaluated atomically during execution, so a concurrent fill or graph change can create a later violation; observe subsequent violations through GET `/relationships/constraints` and violation broadcasts. When `relationshipConstraint` is supplied, duplicate legs for the same exchange in the same tournament scope return 400 `VALIDATION_ERROR` before engine state is read; without a constraint, duplicate legs are not rejected for that reason. Price validation evaluates every leg in YES terms: YES limit prices are unchanged, NO limit prices use their YES-complement price, and uncovered nodes or market orders use current engine prices. Exhaustive mutually exclusive relationships require sum(P) = 1; non-exhaustive mutually exclusive relationships require sum(P) ≤ 1. Unknown or inactive relationships, outsider exchanges, and violated price bounds return 422 `RELATIONSHIP_VIOLATION`; an unavailable engine graph or price read fails closed with 503. relationshipConstraint is part of the app-level idempotency request identity. An engine-routed retry with the same complete identity replays the recorded response before preflight is repeated; an incomplete claim after response loss resumes with the same engine key so the engine rehydrates the accepted command. Use /orders/batch instead if partial success is acceptable. Leg execution errors preserve their underlying v1 error status and include `details.leg` with the zero-based failed leg index. Each successful engine-routed leg includes per-leg `terminalReasonCode` when available. Each successful leg includes nullable authoritative `all` execution economics.

        Args:
            legs: Body parameter.
            idempotency_key: Required client-supplied idempotency key. Reuse this key only when retrying the same logical request. An identical resolved payload replays the exact stored response; reuse with a different resolved payload returns 409.
            relationship_constraint: Optional active ALL relationship UUID. Every leg exchange must belong to it, and an exchange may appear only once per tournament scope. Validation evaluates prices in YES terms: YES leg limit prices are unchanged, NO leg limit prices use their YES-complement price, and uncovered nodes or market orders use current engine prices. Exhaustive mutually exclusive relationships require sum(P) = 1; non-exhaustive mutually exclusive relationships require sum(P) ≤ 1.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrderCreateMultiLegResponse: All legs placed.

        Example:
            ```python
            order = client.orders.create_multi_leg(
                legs=[
                    {
                        "exchangeId": "36",
                        "side": "yes",
                        "action": "buy",
                        "quantity": 100,
                        "price": 0.42,
                        "tournamentId": "550e8400-e29b-41d4-a716-446655440000",
                    },
                    {
                        "exchangeId": "37",
                        "side": "no",
                        "action": "buy",
                        "quantity": 100,
                        "price": 0.42,
                        "tournamentId": "550e8400-e29b-41d4-a716-446655440000",
                    },
                ],
                idempotency_key="multi-leg-placement-2026-07-23-001",
                relationship_constraint="22222222-2222-2222-2222-222222222222",
            )
            ```
        """
        return self._post(
            "/orders/multi-leg",
            body=maybe_transform(
                {
                    "legs": legs,
                    "idempotency_key": idempotency_key,
                    "relationship_constraint": relationship_constraint,
                },
                order_create_multi_leg_params.OrderCreateMultiLegParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderCreateMultiLegResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Order:
        """
        Returns an order owned by the authenticated user. The order ID determines its trading context; organization-bound keys may only read orders in accessible tournaments belonging to their bound organization.

        Args:
            id: Order ID.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Order: Order detail.

        Example:
            ```python
            order = client.orders.retrieve(
                id="1001",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/orders/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Order,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderDeleteResponse:
        """
        Cancels an open order. The order ID determines its trading context; organization-bound keys may only cancel orders in accessible tournaments belonging to their bound organization.

        Args:
            id: Order ID.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrderDeleteResponse: Order cancelled.

        Example:
            ```python
            order = client.orders.delete(
                id="1001",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/orders/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderDeleteResponse,
        )

    def create_cancel_all(
        self,
        *,
        exchange_id: str | Omit = omit,
        market_id: str | Omit = omit,
        tournament_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderCreateCancelAllResponse:
        """
        Cancels open orders for the authenticated user in one trading context.

        Scoping behavior:
        - No body / empty body — an organization-bound key cancels its organization's default tournament orders; an unbound key cancels public global orders
        - `{ exchangeId }` — narrows that default context to one exchange
        - `{ marketId }` — narrows that default context to all exchanges in one market
        - `{ tournamentId }` — uses that explicit accessible tournament; combine with `exchangeId` or `marketId` to narrow further
        - `exchangeId` + `marketId` together — rejected with 400 (mutually exclusive)

        An omitted or empty body cancels every open order in the resolved context. A supplied body must be valid JSON matching the schema, whatever its Content-Type; otherwise the request is rejected with 400 and nothing is cancelled.

        Cancels the caller's open, unexpired orders in that context, in batches of up to 500. `cancelled` counts the orders this request removed; orders that were already filled or cancelled are not counted. Returns 200 once no targeted order remains open. Returns 503 if cancellation paused before it finished (the trading engine was briefly unavailable, or the request ran out of time); `error.details.cancelled` reports the progress so far. Retry the same request until it returns 200. A 503 without `error.details.cancelled` was refused before anything was cancelled and is safe to retry.

        Args:
            exchange_id: Scope cancellation to a specific exchange. Numeric string. Mutually exclusive with marketId.
            market_id: Scope cancellation to all exchanges in a market. Numeric string. Mutually exclusive with exchangeId.
            tournament_id: Scope cancellation to a specific accessible tournament. Omit for the organization's default tournament with an organization-bound key or public global orders with an unbound key.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrderCreateCancelAllResponse: Every targeted order is cancelled; none remains open.

        Example:
            ```python
            order = client.orders.create_cancel_all(
                exchange_id="36",
            )
            ```
        """
        return self._post(
            "/orders/cancel-all",
            body=maybe_transform(
                {
                    "exchange_id": exchange_id,
                    "market_id": market_id,
                    "tournament_id": tournament_id,
                },
                order_create_cancel_all_params.OrderCreateCancelAllParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderCreateCancelAllResponse,
        )

    def list_fills(
        self,
        id: str,
        *,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderListFillsResponse:
        """
        Returns one newest-first page of fills for a specific order. `totalQuantityFilled` and `avgFillPrice` are exact lifecycle totals for the whole order, independent of the current page. The order ID determines its trading context; organization-bound keys may only read fills for orders in accessible tournaments belonging to their bound organization.

        Args:
            id: Order ID.
            limit: Fills per page (max 200).
            cursor: Opaque pagination cursor from a previous response.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrderListFillsResponse: Fills for the order.

        Example:
            ```python
            order = client.orders.list_fills(
                id="1001",
                limit=50,
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/orders/{id}/fills", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit, "cursor": cursor}, order_list_fills_params.OrderListFillsParams),
            ),
            cast_to=OrderListFillsResponse,
        )


class AsyncOrdersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrdersResourceWithRawResponse:
        return AsyncOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrdersResourceWithStreamingResponse:
        return AsyncOrdersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        exchange_id: str,
        side: Literal["yes", "no"],
        action: Literal["buy", "sell"],
        quantity: int,
        price: float | Omit = omit,
        expiration_date: Union[str, datetime] | Omit = omit,
        tournament_id: str | Omit = omit,
        idempotency_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderCreateResponse:
        """
        Unaccepted current documents return 403 `TERMS_NOT_ACKNOWLEDGED` with `error.details.missingDocuments`; each entry contains `documentId`, `kind`, `version`, `organizationId`, `organizationSlug`, `organizationName`, `supportEmail`, `currencyName`, `url`, and `host`. Places a single limit or market order. A required client-supplied `idempotencyKey` identifies the logical placement: retrying the same key with the same resolved payload replays the exact stored response before mutable settlement or market preflights, while reuse with a different resolved payload returns 409. Fresh limit prices must be on the 0.005 tick between 0.005 and 0.995; `price: 1` for a buy and `price: 0` for a sell encode market orders, and off-tick values return 400 `VALIDATION_ERROR`. Omit `price` for a market order (fills at best available price). An organization-bound key defaults an omitted `tournamentId` to the organization's default tournament; an unbound key defaults to the public global context. On engine-routed scopes, an opposite-signed `BUY` nets against the existing position: it reduces or crosses the position at FIFO lot cost. Inspect `avgCost` and `lots` on the corresponding global or tournament portfolio-position read to understand the surviving position's display average and cost lots. On engine-routed scopes, a fully-backed `SELL` closes conventionally; a `SELL` that is flat, opposite the held side, or larger than the held quantity is canonicalized by the engine into its complement `BUY` (`sell yes q@p` ≡ `buy no q@(1−p)`), and the response's canonical `action`/`side`/`price`/`quantity` report the order as placed. Resting quotes on both sides are allowed; an order that would cross your own resting order fills other counterparties, then its crossing remainder is cancelled with `terminalReasonCode: "SelfTradePrevented"`. The nullable `all` response reports authoritative engine-calculated capital efficiency and collateral encumbrance for the execution. On engine-routed scopes a buy is admitted against your cash balance, and resting orders do not escrow cash: it moves only on fills. A buy the full balance cannot pay for even one share of is rejected with 400 `VALIDATION_ERROR` (insufficient funds). A buy is accepted as a no-op (`orderId: null`, `open: false`, nothing placed or traded) when your unexpired resting buys on the same exchange and tournament already commit the whole balance. Resting buys on other exchanges are not counted, so your resting buys across exchanges can add up to more than your balance. An order's resting remainder is sized to what your full current balance can cover, and a later balance decrease shrinks or cancels resting buys you can no longer afford. Buying the outcome opposite a position you hold nets the shares and credits 1 per netted share, so your balance change differs from `totalCost`.

        Args:
            exchange_id: Exchange ID as a numeric string.
            side: Body parameter.
            action: Body parameter.
            quantity: Number of shares, at most 2147483647 (the trading engine holds quantities as a signed 32-bit integer). Larger values are rejected with `VALIDATION_ERROR`.
            price: Limit price in [0, 1]. Limit prices must be on the 0.005 tick between 0.005 and 0.995. `1` with `action: "buy"` and `0` with `action: "sell"` mean a market order; omit `price` for a market order. Off-tick values are rejected with `VALIDATION_ERROR`.
            expiration_date: Optional future ISO 8601 datetime after which the limit order expires. Not supported for market orders.
            tournament_id: When provided, routes the order through that accessible tournament's isolated orderbook and balance. A first order in an open tournament, or by an owner or admin in any tournament of their organization, enrols the caller. When omitted, an organization-bound key uses its organization's default tournament; an unbound key uses the public global context.
            idempotency_key: Required client-supplied idempotency key. Reuse this key only when retrying the same logical request. An identical resolved payload replays the exact stored response; reuse with a different resolved payload returns 409.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrderCreateResponse: Order placed.

        Example:
            ```python
            order = await client.orders.create(
                exchange_id="36",
                side="yes",
                action="buy",
                quantity=100,
                idempotency_key="order-placement-2026-07-23-001",
            )
            ```
        """
        return await self._post(
            "/orders",
            body=await async_maybe_transform(
                {
                    "exchange_id": exchange_id,
                    "side": side,
                    "action": action,
                    "quantity": quantity,
                    "price": price,
                    "expiration_date": expiration_date,
                    "tournament_id": tournament_id,
                    "idempotency_key": idempotency_key,
                },
                order_create_params.OrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderCreateResponse,
        )

    async def list(
        self,
        *,
        status: Literal["open", "closed", "expired", "all"] | Omit = omit,
        exchange_id: str | Omit = omit,
        market_id: str | Omit = omit,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        tournament_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderListResponse:
        """
        Returns the authenticated user's orders. Defaults to open orders only. When `tournamentId` is omitted, an organization-bound key reads its organization's default tournament orders and an unbound key reads public global orders. Engine-backed responses include projection `coverage` metadata.

        Args:
            status: Filter by order status. `open` — resting orders that have not expired. `closed` — filled, cancelled, or expired orders. `expired` — legacy orders still stored as open but past their `expirationDate`, plus engine orders cancelled with reason `Expired` (reporting terminal reason code `Expired`). `all` — no filter.
            exchange_id: Filter to a specific exchange.
            market_id: Filter to all exchanges in a market.
            limit: Results per page (max 200).
            cursor: Pagination cursor from a previous response.
            tournament_id: Filter to orders placed in a specific accessible tournament. Omit to use the organization's default tournament for an organization-bound key or public global orders for an unbound key.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrderListResponse: Paginated list of orders.

        Example:
            ```python
            order = await client.orders.list(
                status="open",
                limit=50,
            )
            ```
        """
        return await self._get(
            "/orders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "status": status,
                        "exchange_id": exchange_id,
                        "market_id": market_id,
                        "limit": limit,
                        "cursor": cursor,
                        "tournament_id": tournament_id,
                    },
                    order_list_params.OrderListParams,
                ),
            ),
            cast_to=OrderListResponse,
        )

    async def create_batch(
        self,
        *,
        idempotency_key: str,
        orders: Iterable[order_create_batch_params.Order],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderCreateBatchResponse:
        """
        Consent is checked per item: an unaccepted current document returns item status 403 with `data.error.code: TERMS_NOT_ACKNOWLEDGED` and `data.error.details.missingDocuments`. Other items can succeed. Places up to 50 orders in a single request under one required client-supplied `idempotencyKey`. For requests first bound after the original-routing rollout is enabled, completed batches retain each originally omitted tournament scope across organization default changes and backend routing changes; older requests without routing evidence retain their existing conflict behavior. Incomplete batches retain their original scope/backend retry fences. Reusing a key from another authenticated organization conflicts. The ordered, resolved batch is the request identity: a completed retry with the same key and payload replays the exact stored 200, 207, or 422 envelope without placing another order, while reuse with a different batch returns 409. Freshly executed engine-routed items report the canonical `action`/`side`/`price`/`quantity`/`terminalReasonCode` as placed; items stored before this change replay without those fields. If any item returns 429 or 5xx, the outer batch remains incomplete; retry with the same key to replay terminal indexes and resume only those non-terminal indexes. Orders are placed one at a time under a bounded execution budget: a batch that cannot finish within it stops issuing further orders and returns 503, keeping every order it already placed — retry with the same key to resume from where it stopped, as many times as needed until a final 200, 207, or 422. Large batches under heavy load are the case that reaches this. A batch with at least one success returns 207 with per-item statuses even when another item is transient. An item rate limited by the trading engine reports status 429 with `data.code: RATE_LIMITED`; nothing was placed for it. A failed item's `data` keeps the error payload of the placement path that rejected it rather than the top-level error envelope: commonly a bare `{ error: "…" }`, sometimes with a `code`; rate-limited items use `{ code: "RATE_LIMITED", error: "…" }`; and consent failures use `{ error: { code, message, details } }`. A zero-success batch returns 429 with the per-item results when every item was rate limited, 502 with per-item `ORDER_STATUS_UNKNOWN` codes when every item has an unknown dispatch outcome, and 503 for any other zero-success batch with a transient item, including a mix of terminal failures and rate-limited items. When a rate-limited item supplied a `Retry-After`, the 207, 429, or 503 response carries the longest one; it may be absent otherwise. After a completed 207, resubmit failed items under a new batch key. Fresh limit prices must be on the 0.005 tick between 0.005 and 0.995; `price: 1` for a buy and `price: 0` for a sell encode market orders, and off-tick values return 400 `VALIDATION_ERROR`. For an organization-bound key, each order that omits `tournamentId` defaults to the organization's default tournament; unbound keys retain the public global default. All orders are validated upfront — if any fail validation the entire request is rejected with 400 before any orders are placed. Execution is best-effort: each order is attempted independently and a failure does not roll back already-placed orders. Use /orders/multi-leg instead if you need an all-or-nothing guarantee. Returns 200 if all succeed, 207 when at least one succeeds and at least one fails (207 does not mean partial fills), 422 if all fail terminally, 429 if every item was rate limited, 502 if every item has an unknown dispatch outcome, or 503 when no item succeeds and another transient outcome remains or the batch stopped at its execution budget with orders still unissued.

        Args:
            idempotency_key: Required client-supplied idempotency key. Reuse this key only when retrying the same logical request. An identical resolved payload replays the exact stored response; reuse with a different resolved payload returns 409.
            orders: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrderCreateBatchResponse: All orders succeeded.

        Example:
            ```python
            order = await client.orders.create_batch(
                idempotency_key="batch-placement-2026-07-23-001",
                orders=[
                    {"exchangeId": "36", "side": "yes", "action": "buy", "quantity": 100, "price": 0.42},
                    {
                        "exchangeId": "37",
                        "side": "no",
                        "action": "buy",
                        "quantity": 50,
                        "price": 0.3,
                        "tournamentId": "550e8400-e29b-41d4-a716-446655440000",
                    },
                ],
            )
            ```
        """
        return await self._post(
            "/orders/batch",
            body=await async_maybe_transform(
                {
                    "idempotency_key": idempotency_key,
                    "orders": orders,
                },
                order_create_batch_params.OrderCreateBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderCreateBatchResponse,
        )

    async def create_multi_leg(
        self,
        *,
        legs: Iterable[order_create_multi_leg_params.Leg],
        idempotency_key: str,
        relationship_constraint: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderCreateMultiLegResponse:
        """
        Unaccepted current documents return 403 `TERMS_NOT_ACKNOWLEDGED` with `error.details.missingDocuments`; each entry contains `documentId`, `kind`, `version`, `organizationId`, `organizationSlug`, `organizationName`, `supportEmail`, `currencyName`, `url`, and `host`. Consent preflight checks the union of documents required by all legs before any leg executes. Places up to 10 orders atomically within a single transaction. For requests first bound after the original-routing rollout is enabled, a completed response retains originally omitted tournament scopes across organization default and backend changes. Ordered legs, explicit scope, relationshipConstraint, economics and original authenticated organization still identify the retry. Historical requests without routing evidence keep existing scope conflicts; incomplete requests retain their leases and backend routing fences. A required client-supplied `idempotencyKey` identifies the logical placement: the same key with the same resolved legs and constraint has no second economic effect in either scope, while reuse with a different payload returns 409. Fresh limit prices must be on the 0.005 tick between 0.005 and 0.995; `price: 1` for a buy and `price: 0` for a sell encode market orders, and off-tick values return 400 `VALIDATION_ERROR`. For an organization-bound key, each leg that omits `tournamentId` defaults to the organization's default tournament; unbound keys retain the public global default. All legs succeed or none are persisted — if any leg fails, the entire request rolls back and no orders are placed. Every leg must route to the same backend: a request mixing engine-routed and non-engine scopes returns 400 `VALIDATION_ERROR`. Engine-routed legs must all belong to the same organization; otherwise the request returns 400 `VALIDATION_ERROR`. Optional `relationshipConstraint` validates every leg against one active canonical ALL relationship using an engine preflight price snapshot taken immediately before dispatch. This validation is not held under the engine execution lock or re-evaluated atomically during execution, so a concurrent fill or graph change can create a later violation; observe subsequent violations through GET `/relationships/constraints` and violation broadcasts. When `relationshipConstraint` is supplied, duplicate legs for the same exchange in the same tournament scope return 400 `VALIDATION_ERROR` before engine state is read; without a constraint, duplicate legs are not rejected for that reason. Price validation evaluates every leg in YES terms: YES limit prices are unchanged, NO limit prices use their YES-complement price, and uncovered nodes or market orders use current engine prices. Exhaustive mutually exclusive relationships require sum(P) = 1; non-exhaustive mutually exclusive relationships require sum(P) ≤ 1. Unknown or inactive relationships, outsider exchanges, and violated price bounds return 422 `RELATIONSHIP_VIOLATION`; an unavailable engine graph or price read fails closed with 503. relationshipConstraint is part of the app-level idempotency request identity. An engine-routed retry with the same complete identity replays the recorded response before preflight is repeated; an incomplete claim after response loss resumes with the same engine key so the engine rehydrates the accepted command. Use /orders/batch instead if partial success is acceptable. Leg execution errors preserve their underlying v1 error status and include `details.leg` with the zero-based failed leg index. Each successful engine-routed leg includes per-leg `terminalReasonCode` when available. Each successful leg includes nullable authoritative `all` execution economics.

        Args:
            legs: Body parameter.
            idempotency_key: Required client-supplied idempotency key. Reuse this key only when retrying the same logical request. An identical resolved payload replays the exact stored response; reuse with a different resolved payload returns 409.
            relationship_constraint: Optional active ALL relationship UUID. Every leg exchange must belong to it, and an exchange may appear only once per tournament scope. Validation evaluates prices in YES terms: YES leg limit prices are unchanged, NO leg limit prices use their YES-complement price, and uncovered nodes or market orders use current engine prices. Exhaustive mutually exclusive relationships require sum(P) = 1; non-exhaustive mutually exclusive relationships require sum(P) ≤ 1.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrderCreateMultiLegResponse: All legs placed.

        Example:
            ```python
            order = await client.orders.create_multi_leg(
                legs=[
                    {
                        "exchangeId": "36",
                        "side": "yes",
                        "action": "buy",
                        "quantity": 100,
                        "price": 0.42,
                        "tournamentId": "550e8400-e29b-41d4-a716-446655440000",
                    },
                    {
                        "exchangeId": "37",
                        "side": "no",
                        "action": "buy",
                        "quantity": 100,
                        "price": 0.42,
                        "tournamentId": "550e8400-e29b-41d4-a716-446655440000",
                    },
                ],
                idempotency_key="multi-leg-placement-2026-07-23-001",
                relationship_constraint="22222222-2222-2222-2222-222222222222",
            )
            ```
        """
        return await self._post(
            "/orders/multi-leg",
            body=await async_maybe_transform(
                {
                    "legs": legs,
                    "idempotency_key": idempotency_key,
                    "relationship_constraint": relationship_constraint,
                },
                order_create_multi_leg_params.OrderCreateMultiLegParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderCreateMultiLegResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Order:
        """
        Returns an order owned by the authenticated user. The order ID determines its trading context; organization-bound keys may only read orders in accessible tournaments belonging to their bound organization.

        Args:
            id: Order ID.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Order: Order detail.

        Example:
            ```python
            order = await client.orders.retrieve(
                id="1001",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/orders/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Order,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderDeleteResponse:
        """
        Cancels an open order. The order ID determines its trading context; organization-bound keys may only cancel orders in accessible tournaments belonging to their bound organization.

        Args:
            id: Order ID.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrderDeleteResponse: Order cancelled.

        Example:
            ```python
            order = await client.orders.delete(
                id="1001",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/orders/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderDeleteResponse,
        )

    async def create_cancel_all(
        self,
        *,
        exchange_id: str | Omit = omit,
        market_id: str | Omit = omit,
        tournament_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderCreateCancelAllResponse:
        """
        Cancels open orders for the authenticated user in one trading context.

        Scoping behavior:
        - No body / empty body — an organization-bound key cancels its organization's default tournament orders; an unbound key cancels public global orders
        - `{ exchangeId }` — narrows that default context to one exchange
        - `{ marketId }` — narrows that default context to all exchanges in one market
        - `{ tournamentId }` — uses that explicit accessible tournament; combine with `exchangeId` or `marketId` to narrow further
        - `exchangeId` + `marketId` together — rejected with 400 (mutually exclusive)

        An omitted or empty body cancels every open order in the resolved context. A supplied body must be valid JSON matching the schema, whatever its Content-Type; otherwise the request is rejected with 400 and nothing is cancelled.

        Cancels the caller's open, unexpired orders in that context, in batches of up to 500. `cancelled` counts the orders this request removed; orders that were already filled or cancelled are not counted. Returns 200 once no targeted order remains open. Returns 503 if cancellation paused before it finished (the trading engine was briefly unavailable, or the request ran out of time); `error.details.cancelled` reports the progress so far. Retry the same request until it returns 200. A 503 without `error.details.cancelled` was refused before anything was cancelled and is safe to retry.

        Args:
            exchange_id: Scope cancellation to a specific exchange. Numeric string. Mutually exclusive with marketId.
            market_id: Scope cancellation to all exchanges in a market. Numeric string. Mutually exclusive with exchangeId.
            tournament_id: Scope cancellation to a specific accessible tournament. Omit for the organization's default tournament with an organization-bound key or public global orders with an unbound key.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrderCreateCancelAllResponse: Every targeted order is cancelled; none remains open.

        Example:
            ```python
            order = await client.orders.create_cancel_all(
                exchange_id="36",
            )
            ```
        """
        return await self._post(
            "/orders/cancel-all",
            body=await async_maybe_transform(
                {
                    "exchange_id": exchange_id,
                    "market_id": market_id,
                    "tournament_id": tournament_id,
                },
                order_create_cancel_all_params.OrderCreateCancelAllParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderCreateCancelAllResponse,
        )

    async def list_fills(
        self,
        id: str,
        *,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderListFillsResponse:
        """
        Returns one newest-first page of fills for a specific order. `totalQuantityFilled` and `avgFillPrice` are exact lifecycle totals for the whole order, independent of the current page. The order ID determines its trading context; organization-bound keys may only read fills for orders in accessible tournaments belonging to their bound organization.

        Args:
            id: Order ID.
            limit: Fills per page (max 200).
            cursor: Opaque pagination cursor from a previous response.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrderListFillsResponse: Fills for the order.

        Example:
            ```python
            order = await client.orders.list_fills(
                id="1001",
                limit=50,
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/orders/{id}/fills", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit, "cursor": cursor}, order_list_fills_params.OrderListFillsParams
                ),
            ),
            cast_to=OrderListFillsResponse,
        )


class OrdersResourceWithRawResponse:
    def __init__(self, orders: OrdersResource) -> None:
        self._orders = orders

        self.create = to_raw_response_wrapper(
            orders.create,
        )
        self.list = to_raw_response_wrapper(
            orders.list,
        )
        self.create_batch = to_raw_response_wrapper(
            orders.create_batch,
        )
        self.create_multi_leg = to_raw_response_wrapper(
            orders.create_multi_leg,
        )
        self.retrieve = to_raw_response_wrapper(
            orders.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            orders.delete,
        )
        self.create_cancel_all = to_raw_response_wrapper(
            orders.create_cancel_all,
        )
        self.list_fills = to_raw_response_wrapper(
            orders.list_fills,
        )


class AsyncOrdersResourceWithRawResponse:
    def __init__(self, orders: AsyncOrdersResource) -> None:
        self._orders = orders

        self.create = async_to_raw_response_wrapper(
            orders.create,
        )
        self.list = async_to_raw_response_wrapper(
            orders.list,
        )
        self.create_batch = async_to_raw_response_wrapper(
            orders.create_batch,
        )
        self.create_multi_leg = async_to_raw_response_wrapper(
            orders.create_multi_leg,
        )
        self.retrieve = async_to_raw_response_wrapper(
            orders.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            orders.delete,
        )
        self.create_cancel_all = async_to_raw_response_wrapper(
            orders.create_cancel_all,
        )
        self.list_fills = async_to_raw_response_wrapper(
            orders.list_fills,
        )


class OrdersResourceWithStreamingResponse:
    def __init__(self, orders: OrdersResource) -> None:
        self._orders = orders

        self.create = to_streamed_response_wrapper(
            orders.create,
        )
        self.list = to_streamed_response_wrapper(
            orders.list,
        )
        self.create_batch = to_streamed_response_wrapper(
            orders.create_batch,
        )
        self.create_multi_leg = to_streamed_response_wrapper(
            orders.create_multi_leg,
        )
        self.retrieve = to_streamed_response_wrapper(
            orders.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            orders.delete,
        )
        self.create_cancel_all = to_streamed_response_wrapper(
            orders.create_cancel_all,
        )
        self.list_fills = to_streamed_response_wrapper(
            orders.list_fills,
        )


class AsyncOrdersResourceWithStreamingResponse:
    def __init__(self, orders: AsyncOrdersResource) -> None:
        self._orders = orders

        self.create = async_to_streamed_response_wrapper(
            orders.create,
        )
        self.list = async_to_streamed_response_wrapper(
            orders.list,
        )
        self.create_batch = async_to_streamed_response_wrapper(
            orders.create_batch,
        )
        self.create_multi_leg = async_to_streamed_response_wrapper(
            orders.create_multi_leg,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            orders.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            orders.delete,
        )
        self.create_cancel_all = async_to_streamed_response_wrapper(
            orders.create_cancel_all,
        )
        self.list_fills = async_to_streamed_response_wrapper(
            orders.list_fills,
        )
