# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.realtime_create_token_response import RealtimeCreateTokenResponse

__all__ = ["RealtimeResource", "AsyncRealtimeResource"]


class RealtimeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RealtimeResourceWithRawResponse:
        return RealtimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RealtimeResourceWithStreamingResponse:
        return RealtimeResourceWithStreamingResponse(self)

    def create_token(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RealtimeCreateTokenResponse:
        """
        Mints a short-lived (3 hour) JWT that authorizes the caller for Realtime private channels. The token carries a `realtime_profile_id` claim, and the `user:{profile_id}` channel is authorized against that claim. Tokens minted for organization-bound API keys also carry `realtime_org_id` and `realtime_key_org_id`; the latter limits tournament-channel authorization to tournaments in the key's organization. It does not change access to the caller's user channel or to the market and leaderboard topics, which any minted token can read.

        Realtime is a **best-effort low-latency feed**, not the financial source of truth and not a replayable event log. Engine market and account changes are coalesced into one pending batch per topic, published once its first change's one-second window closes, so normal flow creates at most one batch per topic per second. Each batch is sent once and never retried. A batch that is stale, oversized, or undeliverable is dropped, not delayed. The arrays still contain every trade, fill, and order change the batch covers, except in a batch flagged `resyncRequired` (see below).

        Every `market_batch` and `account_batch` has `delivery: { model, correlationId, revision, previousRevision, sourceSequenceFrom, sourceSequenceThrough }`, where `model` is always `"best-effort-authoritative-resync"`, and covers its topic's revisions after `previousRevision` through `revision`, normally exactly one. Keep the last accepted revision per topic. A batch whose `revision` is at or below it is a duplicate: ignore its arrays (its `books` still apply, see below). A message was missed only when `previousRevision` is greater than the last accepted revision: perform authoritative REST resynchronization before acting. Otherwise accept the batch and advance the last accepted revision to its `revision`. `delivery.correlationId` identifies the published batch for support diagnostics. `sourceSequenceFrom` and `sourceSequenceThrough` identify the engine-event range that produced the batch, but they are provenance, not a topic-local gap counter. A dropped batch shows up only as a gap in the next batch on its topic, so the final batch on a quiet topic can be lost with no gap to reveal it. Clients MUST therefore resynchronize on initial subscription, reconnect, token refresh, socket error, a revision gap, or a batch flagged `resyncRequired`, and periodically while subscribed (for example every one to two minutes). A missed broadcast never changes durable engine state or reporting history.

        Every channel requires the minted token. Apply it as the Realtime access token before subscribing to any channel — `supabase.realtime.setAuth(token)` in supabase-js or `await supabase.realtime.set_auth(token)` with the asynchronous supabase-py client. The `anonKey` only opens the connection; a join made without the token is refused.

        #### Channels

        All channels are Realtime **private** channels: subscribe with `{ config: { private: true } }` after `setAuth(token)`. The market, leaderboard, and global `relationships:violations` channels admit any token minted by this endpoint. Tournament, tournament-violation, and user channels add the rules in each channel's **Auth**. No channel accepts client broadcasts — payloads are server-signed via the service role, so a subscriber cannot forge a batch, tick, or violation.

        **`market:{exchange_id}`**

        - **Auth:** Requires the minted token — any token from this endpoint, applied with `setAuth`.
        - **Events:** `market_batch`; also `book_dirty`, `market_settled` (see below)
        - **Payload:** `{ trades[], bookDirty[], marketSettled[], delivery }` for the changes the batch covers.

        **`market:{market_id}:combined`**

        - **Auth:** Requires the minted token — any token from this endpoint, applied with `setAuth`.
        - **Events:** `market_batch`; also `book_dirty`, `market_settled`
        - **Payload:** Same as above. Lets a multi-outcome market page subscribe once for every contract; demux on `exchangeId`.

        **`tournament:{tournament_id}:market:{market_id}`**

        - **Auth:** Private — authorized by the tournament in the topic, and denied when that tournament is archived. The membership path, which also denies an actively banned profile, admits any profile token for an open tournament, enrolled members of a private tournament, and owners or admins of the tournament's organization (every tournament of that organization, before they join; service-account profiles do not get this owner/admin shortcut). When the tournament belongs to an organization, each of them must also be a member of that organization. An organization's **default** tournament is additionally readable by any token carrying that organization's `realtime_org_id` — see below. When `realtime_key_org_id` is present, every tournament channel is further restricted to that organization.
        - **Events:** `market_batch`; also `book_dirty`, `market_settled`
        - **Payload:** Same arrays for one market in that tournament, with `tournamentId` on each item, plus `books`: the versioned order book of every exchange the batch names (see below). Every exchange of a multi-outcome market shares the topic; demux on `exchangeId`. Not mirrored to global `market:*` channels. The bare `tournament:{tournament_id}` topic no longer carries market updates; to follow every market of a tournament, use `tournament:{tournament_id}:markets` below.

        **`tournament:{tournament_id}:markets`**

        - **Auth:** Private — exactly the rules of `tournament:{tournament_id}:market:{market_id}` for the tournament in the topic, the organization-default `realtime_org_id` path and the `realtime_key_org_id` restriction included.
        - **Events:** `markets_batch`; also `book_dirty`, `market_settled`
        - **Payload:** `{ markets: [{ marketId, batch }] }`: the batches of the tournament's markets that changed, each `batch` exactly the `market_batch` payload its market topic carries, with its own `delivery`. See below.

        **`leaderboard:all`**

        - **Auth:** Requires the minted token — any token from this endpoint, applied with `setAuth`.
        - **Events:** `tick`
        - **Payload:** `{ at }` dirty signal, sent directly rather than in a revisioned batch, so it has no revision or gap tracking — emitted when the global standings have been recomputed, not when the trade that dirtied them executed, so a refetch on `tick` reads the new standings rather than the ones it replaced. It therefore lags the matching fill by a few seconds, and consecutive moves coalesce into one tick. Subscribe regardless of which period you display and call `GET /leaderboards?period=1d|7d|30d|quarter|all` to refetch.

        **`relationships:violations`**

        - **Auth:** Requires the minted token — any token from this endpoint, applied with `setAuth`.
        - **Events:** `violation`
        - **Payload:** GLOBAL-scope constraint violations only: full public constraint evaluation plus `computedAt`; same object returned in `data[]` by `GET /relationships/constraints`, so no follow-up read is needed. See below.

        **`relationships:violations:{tournamentId}`**

        - **Auth:** Private — only the membership path of `tournament:{tournament_id}:market:{market_id}` (the same archived, ban, enrollment, owner/admin, organization-membership, and `realtime_key_org_id` rules). The organization-default `realtime_org_id` path does not apply, so a subdomain token without membership cannot read an organization's default-tournament violations.
        - **Events:** `violation`
        - **Payload:** Tournament-scope constraint violations for that tournament's prices — never mirrored on the public channel. Same payload shape.

        **`user:{profile_id}`**

        - **Auth:** Private — `realtime_profile_id` must match the channel profile id.
        - **Events:** `account_batch`; also `position_settled`, `refund` (see below), and `notification`
        - **Payload:** `account_batch`: `{ fills, orderUpdates, settlements, refunds, collateralChanges, delivery }` for the changes the batch covers. `notification`: `{ notificationId, type }`, sent on its own (outside `account_batch`, with no revision) each time an in-app notification is created for the profile.

        `price` on every `trades` item, and on every `fills` item where it is not null, is the **YES-denominated** execution price in `[0, 1]` — a single consistent series regardless of which side traded. For a NO position the effective per-share cost is `1 - price`.

        #### `market_batch`

        - `trades` contains the actual executions in the window. Each item is `{ id, sequence, exchangeId, marketId, price, quantity, executedAt, tournamentId? }`.
        - `id` (a string) and `sequence` (a number) identify the match: its engine event sequence, which is also the same id `GET /exchanges/{id}/trades` gives the trade, so one trade seen on both can be deduplicated and ordered. Rarely, the engine records a fill without a match event of its own; then `id` and `sequence` are null, the trade cannot be ordered against other reads, and the client must resynchronize that exchange's price and trade tape over REST.
        - `bookDirty` contains `{ exchangeId, marketId, tournamentId, at }` signals for books whose resting depth changed. On `market:*` topics, refetch those books with `GET /markets/{id}/orderbook`; on tournament market topics the batch carries them in `books`.
        - `marketSettled` contains `{ marketId, tournamentId, settledWith, at }` signals when a market scope settles or refunds.
        - `settledWith` is the market's stamped settlement value: the winning outcome label for a settlement, or `REFUND` for a refund.

        A `marketSettled` signal comes from the root engine settlement/refund event, so it fires even when the exchange has zero holders and therefore produces no per-user entries.
        Treat it as an invalidation hint and refetch the authoritative market state.

        An order that rests unfilled or is cancelled changes `bookDirty` without adding a trade. Book signals carry no private order details.

        `bookDirty` and `marketSettled` entries can repeat for the same scope within a batch: settlement signals are deduplicated per exchange but carry no `exchangeId`, so a multi-outcome market can report one `marketSettled` per settling exchange. Treat both as invalidation hints and coalesce them before refetching.
        A `bookDirty` entry may arrive in the same batch as a trade for the same order; refetch the book once.

        **Order expiry emits nothing.** Expired orders are filtered at read time, so the book changes without a batch. On tournament market topics, refetch an exchange's book after `nextExpiryAt` (below). On `market:*` topics, a client that has stopped polling entirely should set a timer to the earliest `expirationDate` it knows of and refetch then.

        #### Versioned books on tournament market topics

        On `tournament:{tournament_id}:market:{market_id}`, a `market_batch` whose `trades` or `bookDirty` name an exchange also carries `books`: one complete order book per named exchange, ascending by `exchangeId`. Each is `{ exchangeId, asOf: { sequence, at }, nextExpiryAt, bids: [{ price, quantity }], asks: [{ price, quantity }] }`, with `exchangeId` as a number. Levels use the same YES-normalized `{ price, quantity }` objects as the REST orderbooks: total resting depth from every participant, your own orders included, bids best (highest) first and asks best (lowest) first, with no depth cap. Exchanges the batch does not name carry no book and have not changed through it; a batch that names none (settlement only) has no `books`. `market:*` topics never carry books.

        - `asOf` is the engine version the book was read at: the last engine event applied (`sequence`) and the engine clock (`at`). Books are read when the batch is published, so a book can be newer than the batch's own trades, and the books in one batch can have different versions.
        - Keep one version per exchange and compare `asOf` by `sequence`, then `at` as an instant. Apply a pushed book only when it is newer than the book you hold, and keep the higher. Apply a batch's `books` even when its revision is a duplicate: a version never goes backwards, so a repeated book is harmless.
        - `nextExpiryAt` is the soonest expiry among the book's resting orders, or null when none expires. No event announces an expiry, so refetch that exchange's book over REST after `nextExpiryAt`.

        **Keeping a book in sync.** Subscribe, and once subscribed read the REST orderbook (`GET /markets/{id}/orderbook` or `GET /exchanges/{id}/orderbook` with the topic's `tournamentId`, and `depth=200` for the full depth the stream pushes); each exchange's book there carries its own `asOf`. Then apply every pushed book whose `asOf` is newer than the one you hold; a held book with a null `asOf` was served without an engine version, so any pushed book replaces it. Read the REST orderbook again after a revision gap, a batch flagged `resyncRequired`, a trade whose `sequence` is null, a reconnect or token refresh, after an exchange's `nextExpiryAt`, and periodically while subscribed.

        #### `resyncRequired`

        On a tournament market topic, a batch too large for the 768 KiB realtime message size limit cannot carry all its content. It is sent with `resyncRequired: true` and its usual `delivery`, keeping only what fits: its `books`, then as many of its `trades` as fit, in order, and no `bookDirty` or `marketSettled`. When even the books do not fit, it is the compact form `{ resyncRequired: true, delivery }`, with no arrays at all. This is the one exception to "the arrays contain every trade". Check `resyncRequired` before reading any array: apply the `books` it carries by version, advance the last accepted revision as usual, then resynchronize that market over REST.

        #### `markets_batch` on a tournament's markets topic

        `tournament:{tournament_id}:markets` gathers, into one feed, the batches of every market in the tournament that changed. Following many markets of a tournament, subscribe to it instead of the per-market topics, and do not hold both for the same markets: you would receive every batch twice. Following only a few markets, stay on their per-market topics: the markets topic delivers every changed market's batch, including the ones you do not follow.

        - `markets` lists `{ marketId, batch }` entries, one per market whose batch was published, in publication order. `marketId` is the market id as a string. `batch` is exactly the `market_batch` payload published on `tournament:{tournament_id}:market:{market_id}`, with the same `trades`, `bookDirty`, `marketSettled`, `books` and `delivery`.
        - Revisions stay per market: keep the last accepted revision **per `marketId`** and apply each entry's `delivery` by the rules above, and its `books` by `asOf`. The topic has no revision of its own.
        - A message is not a snapshot of the tournament. It carries only markets that changed, and one round of changes can span several messages, each within the 768 KiB realtime message size limit. A market with no changes sends nothing.
        - An entry's `batch` can be flagged `resyncRequired` like any batch, including the compact `{ resyncRequired: true, delivery }` when the entry alone would not fit in a message. Handle it as above, for that market.
        - The `book_dirty` and `market_settled` events that admin and settlement actions send individually on a tournament market topic arrive here too, unbatched and with the same payload. Treat them as invalidation hints for the market they name.

        Resynchronize every market you follow over REST on the occasions listed above: initial subscription, reconnect, token refresh, socket error, a revision gap or `resyncRequired` in that market's entry, and periodically.

        #### Organization default tournaments are surface-scoped

        An organization's configured default tournament follows the same host-relative rule as the REST surfaces: it is **public on that organization's own subdomain** and **members-only on the main platform**. When no default is configured, the legacy global tournament is the fallback. Tokens carry which surface applies.

        - A token minted from a request to the organization's subdomain carries a `realtime_org_id` claim, and that claim alone authorizes `tournament:{tournament_id}:market:{market_id}` for every market of that organization's default tournament. No identity is required, mirroring the fact that a logged-out visitor to that subdomain can already read the same market, prices, book and candles over REST.
        - A web token minted anywhere else carries no `realtime_org_id`, so the same channel falls back to the membership gate: the caller must be a member of the organization.

        This `realtime_org_id` entitlement applies **only** to the current default tournament, including a finite tournament when configured. Every other tournament, including a legacy global tournament that is no longer the default, stays membership-gated on every surface.

        Organization-bound API keys receive both `realtime_org_id` and `realtime_key_org_id` set to the key's organization. The key-org claim is a restriction across all tournament channels: even when the profile could personally read another organization's tournament, this token cannot. Organization-unbound API keys receive neither claim and retain the profile-based behavior. The restriction does not affect `user:{profile_id}`, `market:*`, or `leaderboard:all` topics.

        **Load-bearing invariant:** *an organization's default tournament is readable by anyone who can reach that organization's subdomain.* For web tokens, the org claim is minted from the host the caller arrived on and lives for the token's full 3 hours. Channel authorization resolves the current default from the database; the token does not pin an old default. The token is proof of arrival, arrival is unrestricted, and the same data is readable over REST by reloading the subdomain.

        If org subdomains ever become login- or membership-gated, this invariant breaks and **both** the RLS policy and the token minting must change together.

        #### `account_batch` payload arrays

        - `fills` — one item per executed trade row for the user. `{ orderId, exchangeId, marketId, price, quantity, executedAt, tournamentId }` `orderId` is null when the fill cannot be attributed to an order, and `price` is null when the fill carried no price; resynchronize that order or position over REST.
        - `orderUpdates` — the post-execution state of each order placed or cancelled in the window. `{ orderId, exchangeId, marketId, open, quantityTraded, totalCost, latestTradePrice, tournamentId, at }` A resting order that only fills produces a `fills` entry and no `orderUpdates` entry; track its remaining size from your fills, or read it with `GET /orders/{id}`.
        - `settlements` — per (user, exchange), including losses with `payout: 0`. `{ marketId, exchangeId, outcomeSide, shares, costBasis, payout, realizedPnl, settlementOutcome, tournamentId, at }` `costBasis`, `realizedPnl`, and `settlementOutcome` are null for engine-recorded settlements; `outcomeSide` is always set.
        - `refunds` — per (user, exchange) when a market resolves to `REFUND`. `{ marketId, exchangeId, shares, refundAmount, tournamentId, at }`
        - `collateralChanges` — when an ALL component advances, repays, or releases collateral. `{ delta, outstandingAdvanceAfter, componentId, tournamentId }`

        The per-trade and per-order events `trade`, `fill`, `order_update`, and `collateral` are retired; the batches carry them. Some admin and settlement actions still send `book_dirty` and `market_settled` individually on the market channels, and `position_settled` and `refund` individually on `user:{profile_id}`. Each of those payloads has the same shape as the matching `bookDirty`, `marketSettled`, `settlements`, or `refunds` batch item, so handle it the same way.

        #### `relationships:violations` event payload

        - `violation` — emitted after a processed fill batch when an active relationship touching one of the batch's exchanges currently evaluates to `evaluationStatus: "violated"`. The payload is `{ relationshipId, type, evaluationStatus, violationAmount, reason, bound, lowerBound, upperBound, currentValue, diagnostic, tournamentId, direction, constraint, observedPrices, suggestedCorrectiveTrades, computedAt }`. `type` includes auto-derived `conditional_if` and `boolean_expression` relationships. `lowerBound` and `upperBound` carry the engine-evaluated valid interval when applicable. `constraint` contains the human-readable rule and bound semantics; `observedPrices` and corrective trades include exchange, market, outcome, and current-price context.

        Each batch emits at most one event per relationship id. Satisfied constraints emit nothing, including when a previous violation clears; confirm current state or clearance with `GET /relationships/constraints`. Engine-originated payloads add `delivery: { model: "best-effort-authoritative-resync", correlationId, sourceSequence }`.

        #### Refused joins and connection limits

        - Check `response.ok` and a non-empty `token` before calling `setAuth`. An error response carries no token, and without one every join is refused.
        - The server refuses a join with `CHANNEL_ERROR` when the token is missing or does not authorize the topic (`Unauthorized`), or when the connection already holds 100 channels (`Too many channels`). A refusal does not fix itself, but by default supabase-js re-sends a refused join after 1, 2 and 5 seconds, then every 10 seconds, for as long as the socket stays open. Subscribe with a status callback; on a refused join, call `removeChannel` and do not subscribe to that channel again until the token or the channel count is fixed. A `CHANNEL_ERROR` from a dropped socket or network error is transient: let the client reconnect on its own, then resynchronize over REST.
        - A channel the server closed (after your token expired, say) stays closed: supabase-js drops it, and `setAuth` alone never brings it back. After applying a fresh token, re-create every channel the server closed, and every channel whose join it refused.
        - Use one long-lived client per process and refresh its token with `setAuth`; do not open a new client per subscription. One connection carries at most 100 channels, so subscribing to every market of a large tournament on one socket overflows it. To follow every market of a tournament, subscribe to `tournament:{tournament_id}:markets` instead; otherwise subscribe only to the markets you need, or spread the topics over more connections.

        Subscribe pattern (example in supabase-js):

        ```ts
        // One call returns everything needed to connect: supabaseUrl, anonKey (connection apikey), and token (realtime access token).
        const response = await fetch('/api/v1/realtime/token', { method: 'POST', headers: { Authorization: `Bearer ${API_KEY}` } })
        if (!response.ok) throw new Error(`Realtime token request failed: ${response.status}`)
        const { token, anonKey, supabaseUrl } = await response.json()
        if (!token) throw new Error('Realtime token response carried no token')

        // One long-lived client per process.
        const supabase = createClient(supabaseUrl, anonKey)

        // Every channel requires the minted token: apply it before the first subscribe.
        await supabase.realtime.setAuth(token)

        // A refused join is not transient; supabase-js would otherwise re-send it every 10 seconds.
        const isRefusedJoin = (err) => /Unauthorized|Too many channels/.test(err?.message ?? '')
        // Channels the server closed or refused (an expired token, say) stay gone: re-create them after the next setAuth.
        const channelsToRecreate = []
        function subscribe(makeChannel, onSubscribed) {
          const channel = makeChannel()
          let refused = false
          channel.subscribe((status, err) => {
            if (status === 'SUBSCRIBED') return onSubscribed() // initial state and every rejoin: resync over REST
            if (status === 'CHANNEL_ERROR' && isRefusedJoin(err)) {
              refused = true
              supabase.removeChannel(channel) // stop retrying until the token or channel count is fixed
              channelsToRecreate.push(() => subscribe(makeChannel, onSubscribed)) // a fresh token may fix it
              return onRefusedJoin(channel, err)
            }
            if (status === 'CLOSED' && !refused) channelsToRecreate.push(() => subscribe(makeChannel, onSubscribed))
            // A CHANNEL_ERROR or TIMED_OUT from the transport is transient: the client rejoins on its own.
          })
        }

        // Before the 3 hour expiry: mint a fresh token (checking response.ok and token as above), apply it,
        // then re-create every channel the server closed or refused meanwhile.
        async function refreshRealtimeToken() {
          const freshToken = await mintRealtimeToken()
          await supabase.realtime.setAuth(freshToken)
          for (const recreate of channelsToRecreate.splice(0)) recreate()
        }

        // Tournament market batches — tournament gate; carry versioned books. One last accepted revision per market.
        const lastRevision = new Map()
        function onMarketBatch(marketId, payload) {
          // Books apply by version (asOf.sequence, then asOf.at), even on a duplicate revision.
          for (const book of payload.books ?? []) applyBookIfNewer(book)
          const { revision, previousRevision } = payload.delivery
          const last = lastRevision.get(marketId) ?? null
          // Check resyncRequired before anything else: a compact one carries no arrays.
          if (payload.resyncRequired) {
            if (last === null || revision > last) lastRevision.set(marketId, revision)
            return resyncMarketFromRest(marketId)
          }
          if (last !== null && revision <= last) return // duplicate
          lastRevision.set(marketId, revision)
          if (last !== null && previousRevision > last) return resyncMarketFromRest(marketId)
          for (const trade of payload.trades) {
            if (trade.sequence === null) return resyncMarketFromRest(marketId)
            onTrade(trade)
          }
        }

        // Following a few markets: one tournament market topic each.
        const marketChannel = (marketId) => () => supabase
          .channel(`tournament:${tournamentId}:market:${marketId}`, { config: { private: true } })
          .on('broadcast', { event: 'market_batch' }, ({ payload }) => onMarketBatch(String(marketId), payload))
        subscribe(marketChannel(marketId), () => resyncMarketFromRest(String(marketId)))

        // Following many markets: the tournament's markets topic instead, never alongside their market topics.
        const marketsChannel = () => supabase
          .channel(`tournament:${tournamentId}:markets`, { config: { private: true } })
          .on('broadcast', { event: 'markets_batch' }, ({ payload }) => {
            for (const { marketId, batch } of payload.markets) onMarketBatch(marketId, batch)
          })
          // Individually sent hints arrive unbatched on the same topic.
          .on('broadcast', { event: 'book_dirty' }, ({ payload }) => refetchBook(payload.exchangeId))
          .on('broadcast', { event: 'market_settled' }, ({ payload }) => resyncMarketFromRest(String(payload.marketId)))
        subscribe(marketsChannel, resyncFollowedMarketsFromRest)

        // User feed — realtime_profile_id must match the channel profile id
        const userChannel = () => supabase
          .channel(`user:${profileId}`, { config: { private: true } })
          .on('broadcast', { event: 'account_batch' }, ({ payload }) => {
            for (const fill of payload.fills) onFill(fill)
            for (const order of payload.orderUpdates) onOrderUpdate(order)
          })
        subscribe(userChannel, resyncAccountFromRest)
        ```

        Subscribe pattern (async supabase-py):

        ```python
        import asyncio

        import httpx
        from realtime import RealtimeSubscribeStates
        from supabase import acreate_client

        async with httpx.AsyncClient() as http:
            response = await http.post(f"{base_url}/realtime/token", headers={"Authorization": f"Bearer {api_key}"})
        response.raise_for_status()
        body = response.json()
        token = body.get("token")
        if not token:
            raise RuntimeError("Realtime token response carried no token")

        supabase = await acreate_client(body["supabaseUrl"], body["anonKey"])
        await supabase.realtime.set_auth(token)  # every channel requires the minted token

        channel = supabase.channel("market:42", {"config": {"private": True}})

        def on_status(status, err):
            refused = err is not None and ("Unauthorized" in str(err) or "Too many channels" in str(err))
            if status == RealtimeSubscribeStates.CHANNEL_ERROR and refused:
                # Stop retrying until the token or the channel count is fixed.
                asyncio.create_task(supabase.remove_channel(channel))

        await channel.subscribe(on_status)
        ```

        Following every market of a tournament (async supabase-py):

        ```python
        last_revision = {}  # last accepted revision per market id

        def on_market_batch(market_id, batch):
            for book in batch.get("books", []):
                apply_book_if_newer(book)  # by asOf, even on a duplicate revision
            revision, previous = batch["delivery"]["revision"], batch["delivery"]["previousRevision"]
            last = last_revision.get(market_id)
            if batch.get("resyncRequired"):  # check first: a compact one carries no arrays
                if last is None or revision > last:
                    last_revision[market_id] = revision
                return resync_market_from_rest(market_id)
            if last is not None and revision <= last:
                return  # duplicate
            last_revision[market_id] = revision
            if last is not None and previous > last:
                return resync_market_from_rest(market_id)
            for trade in batch["trades"]:
                if trade["sequence"] is None:
                    return resync_market_from_rest(market_id)
                on_trade(trade)

        def on_markets_batch(message):
            for entry in message["payload"]["markets"]:
                on_market_batch(entry["marketId"], entry["batch"])

        markets = supabase.channel(f"tournament:{tournament_id}:markets", {"config": {"private": True}})
        markets.on_broadcast("markets_batch", on_markets_batch)
        markets.on_broadcast("book_dirty", lambda message: refetch_book(message["payload"]["exchangeId"]))
        markets.on_broadcast("market_settled", lambda message: resync_market_from_rest(str(message["payload"]["marketId"])))

        def on_markets_status(status, err):
            refused = err is not None and ("Unauthorized" in str(err) or "Too many channels" in str(err))
            if status == RealtimeSubscribeStates.SUBSCRIBED:
                asyncio.create_task(resync_followed_markets_from_rest())  # initial state and every rejoin
            elif status == RealtimeSubscribeStates.CHANNEL_ERROR and refused:
                asyncio.create_task(supabase.remove_channel(markets))

        await markets.subscribe(on_markets_status)
        ```

        Tokens expire after 3 hours. Call this endpoint again before expiry to refresh, apply the new token with `setAuth`, then re-create any channel the server closed or refused meanwhile. Each call counts as one write against the per-account rate budget.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RealtimeCreateTokenResponse: Token minted.

        Example:
            ```python
            realtime = client.realtime.create_token()
            ```
        """
        return self._post(
            "/realtime/token",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RealtimeCreateTokenResponse,
        )


class AsyncRealtimeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRealtimeResourceWithRawResponse:
        return AsyncRealtimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRealtimeResourceWithStreamingResponse:
        return AsyncRealtimeResourceWithStreamingResponse(self)

    async def create_token(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RealtimeCreateTokenResponse:
        """
        Mints a short-lived (3 hour) JWT that authorizes the caller for Realtime private channels. The token carries a `realtime_profile_id` claim, and the `user:{profile_id}` channel is authorized against that claim. Tokens minted for organization-bound API keys also carry `realtime_org_id` and `realtime_key_org_id`; the latter limits tournament-channel authorization to tournaments in the key's organization. It does not change access to the caller's user channel or to the market and leaderboard topics, which any minted token can read.

        Realtime is a **best-effort low-latency feed**, not the financial source of truth and not a replayable event log. Engine market and account changes are coalesced into one pending batch per topic, published once its first change's one-second window closes, so normal flow creates at most one batch per topic per second. Each batch is sent once and never retried. A batch that is stale, oversized, or undeliverable is dropped, not delayed. The arrays still contain every trade, fill, and order change the batch covers, except in a batch flagged `resyncRequired` (see below).

        Every `market_batch` and `account_batch` has `delivery: { model, correlationId, revision, previousRevision, sourceSequenceFrom, sourceSequenceThrough }`, where `model` is always `"best-effort-authoritative-resync"`, and covers its topic's revisions after `previousRevision` through `revision`, normally exactly one. Keep the last accepted revision per topic. A batch whose `revision` is at or below it is a duplicate: ignore its arrays (its `books` still apply, see below). A message was missed only when `previousRevision` is greater than the last accepted revision: perform authoritative REST resynchronization before acting. Otherwise accept the batch and advance the last accepted revision to its `revision`. `delivery.correlationId` identifies the published batch for support diagnostics. `sourceSequenceFrom` and `sourceSequenceThrough` identify the engine-event range that produced the batch, but they are provenance, not a topic-local gap counter. A dropped batch shows up only as a gap in the next batch on its topic, so the final batch on a quiet topic can be lost with no gap to reveal it. Clients MUST therefore resynchronize on initial subscription, reconnect, token refresh, socket error, a revision gap, or a batch flagged `resyncRequired`, and periodically while subscribed (for example every one to two minutes). A missed broadcast never changes durable engine state or reporting history.

        Every channel requires the minted token. Apply it as the Realtime access token before subscribing to any channel — `supabase.realtime.setAuth(token)` in supabase-js or `await supabase.realtime.set_auth(token)` with the asynchronous supabase-py client. The `anonKey` only opens the connection; a join made without the token is refused.

        #### Channels

        All channels are Realtime **private** channels: subscribe with `{ config: { private: true } }` after `setAuth(token)`. The market, leaderboard, and global `relationships:violations` channels admit any token minted by this endpoint. Tournament, tournament-violation, and user channels add the rules in each channel's **Auth**. No channel accepts client broadcasts — payloads are server-signed via the service role, so a subscriber cannot forge a batch, tick, or violation.

        **`market:{exchange_id}`**

        - **Auth:** Requires the minted token — any token from this endpoint, applied with `setAuth`.
        - **Events:** `market_batch`; also `book_dirty`, `market_settled` (see below)
        - **Payload:** `{ trades[], bookDirty[], marketSettled[], delivery }` for the changes the batch covers.

        **`market:{market_id}:combined`**

        - **Auth:** Requires the minted token — any token from this endpoint, applied with `setAuth`.
        - **Events:** `market_batch`; also `book_dirty`, `market_settled`
        - **Payload:** Same as above. Lets a multi-outcome market page subscribe once for every contract; demux on `exchangeId`.

        **`tournament:{tournament_id}:market:{market_id}`**

        - **Auth:** Private — authorized by the tournament in the topic, and denied when that tournament is archived. The membership path, which also denies an actively banned profile, admits any profile token for an open tournament, enrolled members of a private tournament, and owners or admins of the tournament's organization (every tournament of that organization, before they join; service-account profiles do not get this owner/admin shortcut). When the tournament belongs to an organization, each of them must also be a member of that organization. An organization's **default** tournament is additionally readable by any token carrying that organization's `realtime_org_id` — see below. When `realtime_key_org_id` is present, every tournament channel is further restricted to that organization.
        - **Events:** `market_batch`; also `book_dirty`, `market_settled`
        - **Payload:** Same arrays for one market in that tournament, with `tournamentId` on each item, plus `books`: the versioned order book of every exchange the batch names (see below). Every exchange of a multi-outcome market shares the topic; demux on `exchangeId`. Not mirrored to global `market:*` channels. The bare `tournament:{tournament_id}` topic no longer carries market updates; to follow every market of a tournament, use `tournament:{tournament_id}:markets` below.

        **`tournament:{tournament_id}:markets`**

        - **Auth:** Private — exactly the rules of `tournament:{tournament_id}:market:{market_id}` for the tournament in the topic, the organization-default `realtime_org_id` path and the `realtime_key_org_id` restriction included.
        - **Events:** `markets_batch`; also `book_dirty`, `market_settled`
        - **Payload:** `{ markets: [{ marketId, batch }] }`: the batches of the tournament's markets that changed, each `batch` exactly the `market_batch` payload its market topic carries, with its own `delivery`. See below.

        **`leaderboard:all`**

        - **Auth:** Requires the minted token — any token from this endpoint, applied with `setAuth`.
        - **Events:** `tick`
        - **Payload:** `{ at }` dirty signal, sent directly rather than in a revisioned batch, so it has no revision or gap tracking — emitted when the global standings have been recomputed, not when the trade that dirtied them executed, so a refetch on `tick` reads the new standings rather than the ones it replaced. It therefore lags the matching fill by a few seconds, and consecutive moves coalesce into one tick. Subscribe regardless of which period you display and call `GET /leaderboards?period=1d|7d|30d|quarter|all` to refetch.

        **`relationships:violations`**

        - **Auth:** Requires the minted token — any token from this endpoint, applied with `setAuth`.
        - **Events:** `violation`
        - **Payload:** GLOBAL-scope constraint violations only: full public constraint evaluation plus `computedAt`; same object returned in `data[]` by `GET /relationships/constraints`, so no follow-up read is needed. See below.

        **`relationships:violations:{tournamentId}`**

        - **Auth:** Private — only the membership path of `tournament:{tournament_id}:market:{market_id}` (the same archived, ban, enrollment, owner/admin, organization-membership, and `realtime_key_org_id` rules). The organization-default `realtime_org_id` path does not apply, so a subdomain token without membership cannot read an organization's default-tournament violations.
        - **Events:** `violation`
        - **Payload:** Tournament-scope constraint violations for that tournament's prices — never mirrored on the public channel. Same payload shape.

        **`user:{profile_id}`**

        - **Auth:** Private — `realtime_profile_id` must match the channel profile id.
        - **Events:** `account_batch`; also `position_settled`, `refund` (see below), and `notification`
        - **Payload:** `account_batch`: `{ fills, orderUpdates, settlements, refunds, collateralChanges, delivery }` for the changes the batch covers. `notification`: `{ notificationId, type }`, sent on its own (outside `account_batch`, with no revision) each time an in-app notification is created for the profile.

        `price` on every `trades` item, and on every `fills` item where it is not null, is the **YES-denominated** execution price in `[0, 1]` — a single consistent series regardless of which side traded. For a NO position the effective per-share cost is `1 - price`.

        #### `market_batch`

        - `trades` contains the actual executions in the window. Each item is `{ id, sequence, exchangeId, marketId, price, quantity, executedAt, tournamentId? }`.
        - `id` (a string) and `sequence` (a number) identify the match: its engine event sequence, which is also the same id `GET /exchanges/{id}/trades` gives the trade, so one trade seen on both can be deduplicated and ordered. Rarely, the engine records a fill without a match event of its own; then `id` and `sequence` are null, the trade cannot be ordered against other reads, and the client must resynchronize that exchange's price and trade tape over REST.
        - `bookDirty` contains `{ exchangeId, marketId, tournamentId, at }` signals for books whose resting depth changed. On `market:*` topics, refetch those books with `GET /markets/{id}/orderbook`; on tournament market topics the batch carries them in `books`.
        - `marketSettled` contains `{ marketId, tournamentId, settledWith, at }` signals when a market scope settles or refunds.
        - `settledWith` is the market's stamped settlement value: the winning outcome label for a settlement, or `REFUND` for a refund.

        A `marketSettled` signal comes from the root engine settlement/refund event, so it fires even when the exchange has zero holders and therefore produces no per-user entries.
        Treat it as an invalidation hint and refetch the authoritative market state.

        An order that rests unfilled or is cancelled changes `bookDirty` without adding a trade. Book signals carry no private order details.

        `bookDirty` and `marketSettled` entries can repeat for the same scope within a batch: settlement signals are deduplicated per exchange but carry no `exchangeId`, so a multi-outcome market can report one `marketSettled` per settling exchange. Treat both as invalidation hints and coalesce them before refetching.
        A `bookDirty` entry may arrive in the same batch as a trade for the same order; refetch the book once.

        **Order expiry emits nothing.** Expired orders are filtered at read time, so the book changes without a batch. On tournament market topics, refetch an exchange's book after `nextExpiryAt` (below). On `market:*` topics, a client that has stopped polling entirely should set a timer to the earliest `expirationDate` it knows of and refetch then.

        #### Versioned books on tournament market topics

        On `tournament:{tournament_id}:market:{market_id}`, a `market_batch` whose `trades` or `bookDirty` name an exchange also carries `books`: one complete order book per named exchange, ascending by `exchangeId`. Each is `{ exchangeId, asOf: { sequence, at }, nextExpiryAt, bids: [{ price, quantity }], asks: [{ price, quantity }] }`, with `exchangeId` as a number. Levels use the same YES-normalized `{ price, quantity }` objects as the REST orderbooks: total resting depth from every participant, your own orders included, bids best (highest) first and asks best (lowest) first, with no depth cap. Exchanges the batch does not name carry no book and have not changed through it; a batch that names none (settlement only) has no `books`. `market:*` topics never carry books.

        - `asOf` is the engine version the book was read at: the last engine event applied (`sequence`) and the engine clock (`at`). Books are read when the batch is published, so a book can be newer than the batch's own trades, and the books in one batch can have different versions.
        - Keep one version per exchange and compare `asOf` by `sequence`, then `at` as an instant. Apply a pushed book only when it is newer than the book you hold, and keep the higher. Apply a batch's `books` even when its revision is a duplicate: a version never goes backwards, so a repeated book is harmless.
        - `nextExpiryAt` is the soonest expiry among the book's resting orders, or null when none expires. No event announces an expiry, so refetch that exchange's book over REST after `nextExpiryAt`.

        **Keeping a book in sync.** Subscribe, and once subscribed read the REST orderbook (`GET /markets/{id}/orderbook` or `GET /exchanges/{id}/orderbook` with the topic's `tournamentId`, and `depth=200` for the full depth the stream pushes); each exchange's book there carries its own `asOf`. Then apply every pushed book whose `asOf` is newer than the one you hold; a held book with a null `asOf` was served without an engine version, so any pushed book replaces it. Read the REST orderbook again after a revision gap, a batch flagged `resyncRequired`, a trade whose `sequence` is null, a reconnect or token refresh, after an exchange's `nextExpiryAt`, and periodically while subscribed.

        #### `resyncRequired`

        On a tournament market topic, a batch too large for the 768 KiB realtime message size limit cannot carry all its content. It is sent with `resyncRequired: true` and its usual `delivery`, keeping only what fits: its `books`, then as many of its `trades` as fit, in order, and no `bookDirty` or `marketSettled`. When even the books do not fit, it is the compact form `{ resyncRequired: true, delivery }`, with no arrays at all. This is the one exception to "the arrays contain every trade". Check `resyncRequired` before reading any array: apply the `books` it carries by version, advance the last accepted revision as usual, then resynchronize that market over REST.

        #### `markets_batch` on a tournament's markets topic

        `tournament:{tournament_id}:markets` gathers, into one feed, the batches of every market in the tournament that changed. Following many markets of a tournament, subscribe to it instead of the per-market topics, and do not hold both for the same markets: you would receive every batch twice. Following only a few markets, stay on their per-market topics: the markets topic delivers every changed market's batch, including the ones you do not follow.

        - `markets` lists `{ marketId, batch }` entries, one per market whose batch was published, in publication order. `marketId` is the market id as a string. `batch` is exactly the `market_batch` payload published on `tournament:{tournament_id}:market:{market_id}`, with the same `trades`, `bookDirty`, `marketSettled`, `books` and `delivery`.
        - Revisions stay per market: keep the last accepted revision **per `marketId`** and apply each entry's `delivery` by the rules above, and its `books` by `asOf`. The topic has no revision of its own.
        - A message is not a snapshot of the tournament. It carries only markets that changed, and one round of changes can span several messages, each within the 768 KiB realtime message size limit. A market with no changes sends nothing.
        - An entry's `batch` can be flagged `resyncRequired` like any batch, including the compact `{ resyncRequired: true, delivery }` when the entry alone would not fit in a message. Handle it as above, for that market.
        - The `book_dirty` and `market_settled` events that admin and settlement actions send individually on a tournament market topic arrive here too, unbatched and with the same payload. Treat them as invalidation hints for the market they name.

        Resynchronize every market you follow over REST on the occasions listed above: initial subscription, reconnect, token refresh, socket error, a revision gap or `resyncRequired` in that market's entry, and periodically.

        #### Organization default tournaments are surface-scoped

        An organization's configured default tournament follows the same host-relative rule as the REST surfaces: it is **public on that organization's own subdomain** and **members-only on the main platform**. When no default is configured, the legacy global tournament is the fallback. Tokens carry which surface applies.

        - A token minted from a request to the organization's subdomain carries a `realtime_org_id` claim, and that claim alone authorizes `tournament:{tournament_id}:market:{market_id}` for every market of that organization's default tournament. No identity is required, mirroring the fact that a logged-out visitor to that subdomain can already read the same market, prices, book and candles over REST.
        - A web token minted anywhere else carries no `realtime_org_id`, so the same channel falls back to the membership gate: the caller must be a member of the organization.

        This `realtime_org_id` entitlement applies **only** to the current default tournament, including a finite tournament when configured. Every other tournament, including a legacy global tournament that is no longer the default, stays membership-gated on every surface.

        Organization-bound API keys receive both `realtime_org_id` and `realtime_key_org_id` set to the key's organization. The key-org claim is a restriction across all tournament channels: even when the profile could personally read another organization's tournament, this token cannot. Organization-unbound API keys receive neither claim and retain the profile-based behavior. The restriction does not affect `user:{profile_id}`, `market:*`, or `leaderboard:all` topics.

        **Load-bearing invariant:** *an organization's default tournament is readable by anyone who can reach that organization's subdomain.* For web tokens, the org claim is minted from the host the caller arrived on and lives for the token's full 3 hours. Channel authorization resolves the current default from the database; the token does not pin an old default. The token is proof of arrival, arrival is unrestricted, and the same data is readable over REST by reloading the subdomain.

        If org subdomains ever become login- or membership-gated, this invariant breaks and **both** the RLS policy and the token minting must change together.

        #### `account_batch` payload arrays

        - `fills` — one item per executed trade row for the user. `{ orderId, exchangeId, marketId, price, quantity, executedAt, tournamentId }` `orderId` is null when the fill cannot be attributed to an order, and `price` is null when the fill carried no price; resynchronize that order or position over REST.
        - `orderUpdates` — the post-execution state of each order placed or cancelled in the window. `{ orderId, exchangeId, marketId, open, quantityTraded, totalCost, latestTradePrice, tournamentId, at }` A resting order that only fills produces a `fills` entry and no `orderUpdates` entry; track its remaining size from your fills, or read it with `GET /orders/{id}`.
        - `settlements` — per (user, exchange), including losses with `payout: 0`. `{ marketId, exchangeId, outcomeSide, shares, costBasis, payout, realizedPnl, settlementOutcome, tournamentId, at }` `costBasis`, `realizedPnl`, and `settlementOutcome` are null for engine-recorded settlements; `outcomeSide` is always set.
        - `refunds` — per (user, exchange) when a market resolves to `REFUND`. `{ marketId, exchangeId, shares, refundAmount, tournamentId, at }`
        - `collateralChanges` — when an ALL component advances, repays, or releases collateral. `{ delta, outstandingAdvanceAfter, componentId, tournamentId }`

        The per-trade and per-order events `trade`, `fill`, `order_update`, and `collateral` are retired; the batches carry them. Some admin and settlement actions still send `book_dirty` and `market_settled` individually on the market channels, and `position_settled` and `refund` individually on `user:{profile_id}`. Each of those payloads has the same shape as the matching `bookDirty`, `marketSettled`, `settlements`, or `refunds` batch item, so handle it the same way.

        #### `relationships:violations` event payload

        - `violation` — emitted after a processed fill batch when an active relationship touching one of the batch's exchanges currently evaluates to `evaluationStatus: "violated"`. The payload is `{ relationshipId, type, evaluationStatus, violationAmount, reason, bound, lowerBound, upperBound, currentValue, diagnostic, tournamentId, direction, constraint, observedPrices, suggestedCorrectiveTrades, computedAt }`. `type` includes auto-derived `conditional_if` and `boolean_expression` relationships. `lowerBound` and `upperBound` carry the engine-evaluated valid interval when applicable. `constraint` contains the human-readable rule and bound semantics; `observedPrices` and corrective trades include exchange, market, outcome, and current-price context.

        Each batch emits at most one event per relationship id. Satisfied constraints emit nothing, including when a previous violation clears; confirm current state or clearance with `GET /relationships/constraints`. Engine-originated payloads add `delivery: { model: "best-effort-authoritative-resync", correlationId, sourceSequence }`.

        #### Refused joins and connection limits

        - Check `response.ok` and a non-empty `token` before calling `setAuth`. An error response carries no token, and without one every join is refused.
        - The server refuses a join with `CHANNEL_ERROR` when the token is missing or does not authorize the topic (`Unauthorized`), or when the connection already holds 100 channels (`Too many channels`). A refusal does not fix itself, but by default supabase-js re-sends a refused join after 1, 2 and 5 seconds, then every 10 seconds, for as long as the socket stays open. Subscribe with a status callback; on a refused join, call `removeChannel` and do not subscribe to that channel again until the token or the channel count is fixed. A `CHANNEL_ERROR` from a dropped socket or network error is transient: let the client reconnect on its own, then resynchronize over REST.
        - A channel the server closed (after your token expired, say) stays closed: supabase-js drops it, and `setAuth` alone never brings it back. After applying a fresh token, re-create every channel the server closed, and every channel whose join it refused.
        - Use one long-lived client per process and refresh its token with `setAuth`; do not open a new client per subscription. One connection carries at most 100 channels, so subscribing to every market of a large tournament on one socket overflows it. To follow every market of a tournament, subscribe to `tournament:{tournament_id}:markets` instead; otherwise subscribe only to the markets you need, or spread the topics over more connections.

        Subscribe pattern (example in supabase-js):

        ```ts
        // One call returns everything needed to connect: supabaseUrl, anonKey (connection apikey), and token (realtime access token).
        const response = await fetch('/api/v1/realtime/token', { method: 'POST', headers: { Authorization: `Bearer ${API_KEY}` } })
        if (!response.ok) throw new Error(`Realtime token request failed: ${response.status}`)
        const { token, anonKey, supabaseUrl } = await response.json()
        if (!token) throw new Error('Realtime token response carried no token')

        // One long-lived client per process.
        const supabase = createClient(supabaseUrl, anonKey)

        // Every channel requires the minted token: apply it before the first subscribe.
        await supabase.realtime.setAuth(token)

        // A refused join is not transient; supabase-js would otherwise re-send it every 10 seconds.
        const isRefusedJoin = (err) => /Unauthorized|Too many channels/.test(err?.message ?? '')
        // Channels the server closed or refused (an expired token, say) stay gone: re-create them after the next setAuth.
        const channelsToRecreate = []
        function subscribe(makeChannel, onSubscribed) {
          const channel = makeChannel()
          let refused = false
          channel.subscribe((status, err) => {
            if (status === 'SUBSCRIBED') return onSubscribed() // initial state and every rejoin: resync over REST
            if (status === 'CHANNEL_ERROR' && isRefusedJoin(err)) {
              refused = true
              supabase.removeChannel(channel) // stop retrying until the token or channel count is fixed
              channelsToRecreate.push(() => subscribe(makeChannel, onSubscribed)) // a fresh token may fix it
              return onRefusedJoin(channel, err)
            }
            if (status === 'CLOSED' && !refused) channelsToRecreate.push(() => subscribe(makeChannel, onSubscribed))
            // A CHANNEL_ERROR or TIMED_OUT from the transport is transient: the client rejoins on its own.
          })
        }

        // Before the 3 hour expiry: mint a fresh token (checking response.ok and token as above), apply it,
        // then re-create every channel the server closed or refused meanwhile.
        async function refreshRealtimeToken() {
          const freshToken = await mintRealtimeToken()
          await supabase.realtime.setAuth(freshToken)
          for (const recreate of channelsToRecreate.splice(0)) recreate()
        }

        // Tournament market batches — tournament gate; carry versioned books. One last accepted revision per market.
        const lastRevision = new Map()
        function onMarketBatch(marketId, payload) {
          // Books apply by version (asOf.sequence, then asOf.at), even on a duplicate revision.
          for (const book of payload.books ?? []) applyBookIfNewer(book)
          const { revision, previousRevision } = payload.delivery
          const last = lastRevision.get(marketId) ?? null
          // Check resyncRequired before anything else: a compact one carries no arrays.
          if (payload.resyncRequired) {
            if (last === null || revision > last) lastRevision.set(marketId, revision)
            return resyncMarketFromRest(marketId)
          }
          if (last !== null && revision <= last) return // duplicate
          lastRevision.set(marketId, revision)
          if (last !== null && previousRevision > last) return resyncMarketFromRest(marketId)
          for (const trade of payload.trades) {
            if (trade.sequence === null) return resyncMarketFromRest(marketId)
            onTrade(trade)
          }
        }

        // Following a few markets: one tournament market topic each.
        const marketChannel = (marketId) => () => supabase
          .channel(`tournament:${tournamentId}:market:${marketId}`, { config: { private: true } })
          .on('broadcast', { event: 'market_batch' }, ({ payload }) => onMarketBatch(String(marketId), payload))
        subscribe(marketChannel(marketId), () => resyncMarketFromRest(String(marketId)))

        // Following many markets: the tournament's markets topic instead, never alongside their market topics.
        const marketsChannel = () => supabase
          .channel(`tournament:${tournamentId}:markets`, { config: { private: true } })
          .on('broadcast', { event: 'markets_batch' }, ({ payload }) => {
            for (const { marketId, batch } of payload.markets) onMarketBatch(marketId, batch)
          })
          // Individually sent hints arrive unbatched on the same topic.
          .on('broadcast', { event: 'book_dirty' }, ({ payload }) => refetchBook(payload.exchangeId))
          .on('broadcast', { event: 'market_settled' }, ({ payload }) => resyncMarketFromRest(String(payload.marketId)))
        subscribe(marketsChannel, resyncFollowedMarketsFromRest)

        // User feed — realtime_profile_id must match the channel profile id
        const userChannel = () => supabase
          .channel(`user:${profileId}`, { config: { private: true } })
          .on('broadcast', { event: 'account_batch' }, ({ payload }) => {
            for (const fill of payload.fills) onFill(fill)
            for (const order of payload.orderUpdates) onOrderUpdate(order)
          })
        subscribe(userChannel, resyncAccountFromRest)
        ```

        Subscribe pattern (async supabase-py):

        ```python
        import asyncio

        import httpx
        from realtime import RealtimeSubscribeStates
        from supabase import acreate_client

        async with httpx.AsyncClient() as http:
            response = await http.post(f"{base_url}/realtime/token", headers={"Authorization": f"Bearer {api_key}"})
        response.raise_for_status()
        body = response.json()
        token = body.get("token")
        if not token:
            raise RuntimeError("Realtime token response carried no token")

        supabase = await acreate_client(body["supabaseUrl"], body["anonKey"])
        await supabase.realtime.set_auth(token)  # every channel requires the minted token

        channel = supabase.channel("market:42", {"config": {"private": True}})

        def on_status(status, err):
            refused = err is not None and ("Unauthorized" in str(err) or "Too many channels" in str(err))
            if status == RealtimeSubscribeStates.CHANNEL_ERROR and refused:
                # Stop retrying until the token or the channel count is fixed.
                asyncio.create_task(supabase.remove_channel(channel))

        await channel.subscribe(on_status)
        ```

        Following every market of a tournament (async supabase-py):

        ```python
        last_revision = {}  # last accepted revision per market id

        def on_market_batch(market_id, batch):
            for book in batch.get("books", []):
                apply_book_if_newer(book)  # by asOf, even on a duplicate revision
            revision, previous = batch["delivery"]["revision"], batch["delivery"]["previousRevision"]
            last = last_revision.get(market_id)
            if batch.get("resyncRequired"):  # check first: a compact one carries no arrays
                if last is None or revision > last:
                    last_revision[market_id] = revision
                return resync_market_from_rest(market_id)
            if last is not None and revision <= last:
                return  # duplicate
            last_revision[market_id] = revision
            if last is not None and previous > last:
                return resync_market_from_rest(market_id)
            for trade in batch["trades"]:
                if trade["sequence"] is None:
                    return resync_market_from_rest(market_id)
                on_trade(trade)

        def on_markets_batch(message):
            for entry in message["payload"]["markets"]:
                on_market_batch(entry["marketId"], entry["batch"])

        markets = supabase.channel(f"tournament:{tournament_id}:markets", {"config": {"private": True}})
        markets.on_broadcast("markets_batch", on_markets_batch)
        markets.on_broadcast("book_dirty", lambda message: refetch_book(message["payload"]["exchangeId"]))
        markets.on_broadcast("market_settled", lambda message: resync_market_from_rest(str(message["payload"]["marketId"])))

        def on_markets_status(status, err):
            refused = err is not None and ("Unauthorized" in str(err) or "Too many channels" in str(err))
            if status == RealtimeSubscribeStates.SUBSCRIBED:
                asyncio.create_task(resync_followed_markets_from_rest())  # initial state and every rejoin
            elif status == RealtimeSubscribeStates.CHANNEL_ERROR and refused:
                asyncio.create_task(supabase.remove_channel(markets))

        await markets.subscribe(on_markets_status)
        ```

        Tokens expire after 3 hours. Call this endpoint again before expiry to refresh, apply the new token with `setAuth`, then re-create any channel the server closed or refused meanwhile. Each call counts as one write against the per-account rate budget.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RealtimeCreateTokenResponse: Token minted.

        Example:
            ```python
            realtime = await client.realtime.create_token()
            ```
        """
        return await self._post(
            "/realtime/token",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RealtimeCreateTokenResponse,
        )


class RealtimeResourceWithRawResponse:
    def __init__(self, realtime: RealtimeResource) -> None:
        self._realtime = realtime

        self.create_token = to_raw_response_wrapper(
            realtime.create_token,
        )


class AsyncRealtimeResourceWithRawResponse:
    def __init__(self, realtime: AsyncRealtimeResource) -> None:
        self._realtime = realtime

        self.create_token = async_to_raw_response_wrapper(
            realtime.create_token,
        )


class RealtimeResourceWithStreamingResponse:
    def __init__(self, realtime: RealtimeResource) -> None:
        self._realtime = realtime

        self.create_token = to_streamed_response_wrapper(
            realtime.create_token,
        )


class AsyncRealtimeResourceWithStreamingResponse:
    def __init__(self, realtime: AsyncRealtimeResource) -> None:
        self._realtime = realtime

        self.create_token = async_to_streamed_response_wrapper(
            realtime.create_token,
        )
