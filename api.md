# Super Market Python API

Complete reference of every operation, grouped by resource. See [the README](./README.md) for usage and configuration.

## Contents

- [`Markets`](#markets)
  - [List markets](#list-markets)
  - [Create market](#create-market)
  - [Get market](#get-market)
  - [Replace market thumbnail](#replace-market-thumbnail)
  - [Get market orderbook](#get-market-orderbook)
  - [Get market node tree](#get-market-node-tree)
- [`Exchanges`](#exchanges)
  - [List exchanges](#list-exchanges)
  - [Get exchange price](#get-exchange-price)
  - [Get exchange orderbook](#get-exchange-orderbook)
  - [Get exchange price history](#get-exchange-price-history)
  - [Get exchange trade tape](#get-exchange-trade-tape)
  - [Bulk price snapshot](#bulk-price-snapshot)
- [`Orders`](#orders)
  - [Place order](#place-order)
  - [List orders](#list-orders)
  - [Place batch orders](#place-batch-orders)
  - [Place multi-leg order](#place-multi-leg-order)
  - [Get order](#get-order)
  - [Cancel order](#cancel-order)
  - [Cancel all orders](#cancel-all-orders)
  - [Get order fills](#get-order-fills)
- [`Portfolio`](#portfolio)
  - [Get ALL collateral](#get-all-collateral)
  - [Get open positions](#get-open-positions)
  - [Get P&L summary](#get-pl-summary)
  - [Get portfolio value history](#get-portfolio-value-history)
  - [Get transaction history](#get-transaction-history)
  - [List settlements](#list-settlements)
  - [List fills](#list-fills)
- [`Account`](#account)
  - [Get account](#get-account)
- [`Tournaments`](#tournaments)
  - [List my tournaments](#list-my-tournaments)
  - [Get tournament](#get-tournament)
  - [Get tournament leaderboard](#get-tournament-leaderboard)
  - [List tournament seasons](#list-tournament-seasons)
  - [`Tournaments Markets`](#tournaments-markets)
    - [List tournament markets](#list-tournament-markets)
    - [Get tournament market](#get-tournament-market)
  - [`Tournaments Portfolio`](#tournaments-portfolio)
    - [Get tournament positions](#get-tournament-positions)
    - [Get tournament transactions](#get-tournament-transactions)
    - [List tournament fills](#list-tournament-fills)
    - [Get tournament portfolio value history](#get-tournament-portfolio-value-history)
    - [List tournament settlements](#list-tournament-settlements)
    - [Get tournament P&L](#get-tournament-pl)
  - [`Tournaments Me`](#tournaments-me)
    - [Get my tournament smart score](#get-my-tournament-smart-score)
- [`Leaderboards`](#leaderboards)
  - [Get a leaderboard (global or tournament-scoped)](#get-a-leaderboard-global-or-tournament-scoped)
- [`Dmm`](#dmm)
  - [List failed autosettlements](#list-failed-autosettlements)
  - [Get org-wide user rankings](#get-org-wide-user-rankings)
  - [`Dmm Tournaments`](#dmm-tournaments)
    - [List tournaments](#list-tournaments)
    - [Create tournament](#create-tournament)
    - [Update tournament](#update-tournament)
    - [Delete draft tournament](#delete-draft-tournament)
    - [Reset tournament balances](#reset-tournament-balances)
    - [Get per-tournament user rankings](#get-per-tournament-user-rankings)
    - [List tournament market assignments](#list-tournament-market-assignments)
    - [List executed trades](#list-executed-trades)
    - [List orders](#list-orders-1)
    - [List virtual-balance ledger](#list-virtual-balance-ledger)
    - [Market-maker inventory and exposure](#market-maker-inventory-and-exposure)
    - [`Dmm Tournaments EndSettlement`](#dmm-tournaments-endsettlement)
      - [Preview end-settlement](#preview-end-settlement)
      - [Queue end-settlement](#queue-end-settlement)
      - [Get end-settlement status](#get-end-settlement-status)
    - [`Dmm Tournaments SettlementOverrides`](#dmm-tournaments-settlementoverrides)
      - [Preview settlement corrections](#preview-settlement-corrections)
      - [Execute settlement corrections](#execute-settlement-corrections)
    - [`Dmm Tournaments Markets`](#dmm-tournaments-markets)
      - [List tournament market assignments (deprecated)](#list-tournament-market-assignments-deprecated)
      - [Add market to tournament](#add-market-to-tournament)
      - [Remove market from tournament](#remove-market-from-tournament)
    - [`Dmm Tournaments Members`](#dmm-tournaments-members)
      - [List tournament members](#list-tournament-members)
      - [Add tournament member](#add-tournament-member)
      - [Remove tournament member](#remove-tournament-member)
    - [`Dmm Tournaments MarketGroups`](#dmm-tournaments-marketgroups)
      - [List org market groups (with binding status)](#list-org-market-groups-with-binding-status)
      - [Bind market group](#bind-market-group)
      - [Unbind market group](#unbind-market-group)
    - [`Dmm Tournaments UserGroups`](#dmm-tournaments-usergroups)
      - [List org user groups (with binding status)](#list-org-user-groups-with-binding-status)
      - [Bind user group](#bind-user-group)
      - [Unbind user group](#unbind-user-group)
    - [`Dmm Tournaments Exchanges`](#dmm-tournaments-exchanges)
      - [Seed tournament exchange liquidity](#seed-tournament-exchange-liquidity)
      - [Sweep tournament exchange liquidity](#sweep-tournament-exchange-liquidity)
  - [`Dmm Relationships`](#dmm-relationships)
    - [Establish an ALL relationship](#establish-an-all-relationship)
    - [Deactivate an ALL relationship](#deactivate-an-all-relationship)
    - [Get an ALL relationship operation](#get-an-all-relationship-operation)
    - [Reconcile organization-derived ALL relationships](#reconcile-organization-derived-all-relationships)
  - [`Dmm Icims`](#dmm-icims)
    - [Export iCIMS-qualified candidates](#export-icims-qualified-candidates)
  - [`Dmm TraderAnalytics`](#dmm-traderanalytics)
    - [Elite cohort summary](#elite-cohort-summary)
    - [`Dmm TraderAnalytics Users`](#dmm-traderanalytics-users)
      - [List trader analytics](#list-trader-analytics)
      - [Get trader analytics for a single user](#get-trader-analytics-for-a-single-user)
  - [`Dmm Groups`](#dmm-groups)
    - [`Dmm Groups Markets`](#dmm-groups-markets)
      - [List market groups](#list-market-groups)
      - [Create market group](#create-market-group)
      - [Get market group](#get-market-group)
      - [Update market group](#update-market-group)
      - [Delete market group](#delete-market-group)
      - [List market group members](#list-market-group-members)
      - [Add market group members](#add-market-group-members)
      - [Remove market group members](#remove-market-group-members)
    - [`Dmm Groups Users`](#dmm-groups-users)
      - [List user groups](#list-user-groups)
      - [Create user group](#create-user-group)
      - [Get user group](#get-user-group)
      - [Update user group](#update-user-group)
      - [Delete user group](#delete-user-group)
      - [List user group members](#list-user-group-members)
      - [Add user group members](#add-user-group-members)
      - [Remove user group members](#remove-user-group-members)
- [`Realtime`](#realtime)
  - [Mint realtime token](#mint-realtime-token)
- [`RelationshipsAll`](#relationshipsall)
  - [List market relationships](#list-market-relationships)
  - [Get a market relationship graph](#get-a-market-relationship-graph)
  - [Evaluate relationship price constraints](#evaluate-relationship-price-constraints)

## Setup

```python
import os

from super_market import SuperMarketAPI

client = SuperMarketAPI(
    bearer_auth=os.environ.get("BEARER_AUTH"),
)
```

## `Markets`

Browse prediction markets, their metadata, orderbooks, and exchange structure. Markets are containers for one or more exchanges (tradable contracts).

### List markets

Canonical discovery endpoint. With an unbound API key, returns public globally visible markets with one public context. With an organization-bound API key, returns one deduplicated row per market directly attached to any accessible tournament in that organization; each row's `contexts` contain tournament metadata, currency, and context-specific exchange prices. Markets present only through a bound market group are not included until assigned to the tournament. Pass `tournamentId` to return only that accessible tournament context; `/tournaments/{slug}/markets` provides the equivalent slug-based view.

| Direction | Type |
| --- | --- |
| Request | [`MarketListParams`](./src/super_market/types/market_list_params.py) |
| Response | [`MarketListResponse`](./src/super_market/types/market_list_response.py) |

```python
market = client.markets.list(
    limit=20,
    sort="recent",
    status="any",
)
```

### Create market

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Unaccepted current documents return 403 `TERMS_NOT_ACKNOWLEDGED` with `error.details.missingDocuments` containing `documentId`, `kind`, `version`, `organizationId`, `organizationSlug`, `organizationName`, `supportEmail`, `currencyName`, `url`, and `host`; `error.details.legacyCode` is also `TERMS_NOT_ACKNOWLEDGED`. Create a prediction market. The API-key owner is recorded as the creator. Unbound keys pay creation fees from the owner's balance. Organization-bound keys create markets free of charge, including free `generateVideo`; `superSignal: true` and positive `liquidityAmount` are rejected. With an organization-bound key, omitting all tournament fields requires organization owner/admin authority and atomically creates a tournament-only market attached to that organization's default tournament. Supplying an explicit tournament field attaches only to the requested context; it does not also add the market to the organization's default tournament. **Required scope:** `trade`; explicit tournament fields additionally require `admin`.

| Direction | Type |
| --- | --- |
| Request | [`MarketCreateParams`](./src/super_market/types/market_create_params.py) |
| Response | [`MarketCreate`](./src/super_market/types/market_create.py) |

```python
market = client.markets.create(
    market_submission={"title": "Will it rain tomorrow in NYC?", "root_node": {"node_type": "contract", "position": 0}},
)
```

### Get market

Returns the canonical market in the same public, organization-wide, or explicit tournament scope as `GET /markets`, including its accessible pricing contexts.

| Direction | Type |
| --- | --- |
| Request | [`MarketRetrieveParams`](./src/super_market/types/market_retrieve_params.py) |
| Response | [`Market`](./src/super_market/types/market.py) |

```python
market = client.markets.retrieve(
    id="26",
)
```

### Replace market thumbnail

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Replace a market thumbnail with an owned URL or uploaded file. Organization-bound keys may update only markets exclusive to their organization; unbound platform keys may update any market. Existing video status fields are preserved. Returns `409 CONFLICT` while media generation is in progress. **Required scope:** `trade`.

| Direction | Type |
| --- | --- |
| Request | [`MarketUpdateParams`](./src/super_market/types/market_update_params.py) |
| Response | [`MarketThumbnailPatch`](./src/super_market/types/market_thumbnail_patch.py) |

```python
market = client.markets.update(
    id="26",
    thumbnail_url="https://r2.thesuper.market/market-thumbnails/platform/123e4567-e89b-12d3-a456-426614174000.webp",
)
```

### Get market orderbook

Returns YES-perspective orderbooks for every exchange in the market, plus overround. Each side is capped at `depth` price rungs. Each exchange's book, including those in `contexts[]`, carries its own `asOf`: the engine version it was read at, `{ sequence, at }`, the same version realtime `books` carry (compare by `sequence`, then `at`). `asOf` is null when the book is served without an engine version. Organization-bound requests include one `contexts` entry per accessible attached tournament; the legacy top-level fields mirror the organization's default tournament when the market is attached there, otherwise the first accessible context. Pass `tournamentId` for one explicit context. Unbound requests retain the public orderbook context.

| Direction | Type |
| --- | --- |
| Request | [`MarketListOrderbookParams`](./src/super_market/types/market_list_orderbook_params.py) |
| Response | [`MarketListOrderbookResponse`](./src/super_market/types/market_list_orderbook_response.py) |

```python
market = client.markets.list_orderbook(
    id="26",
)
```

### Get market node tree

Returns the resolution logic tree in the same public, organization-wide, or explicit tournament visibility scope as market discovery. Contract (leaf) nodes carry the contract type, settlement date, settled outcome and contract-type-specific details. Operator nodes (AND / OR / NOT / IF) combine their children.

| Direction | Type |
| --- | --- |
| Request | [`MarketListNodesParams`](./src/super_market/types/market_list_nodes_params.py) |
| Response | [`MarketListNodesResponse`](./src/super_market/types/market_list_nodes_response.py) |

```python
market = client.markets.list_nodes(
    id="26",
)
```

## `Exchanges`

Access price snapshots, orderbook depth, and OHLCV candle history for individual exchanges. An exchange is the API's atomic tradable contract; every order and trade references an exchange ID.

### List exchanges

Paginated list of tradable exchanges in the same scope as canonical market discovery. Unbound keys receive public exchanges with one public context. Organization-bound keys receive canonical, deduplicated exchanges from every accessible attached tournament, with context-specific prices in `contexts`. Pass `tournamentId` to return only one accessible tournament context. `marketId` and `ids` are mutually exclusive filters.

| Direction | Type |
| --- | --- |
| Request | [`ExchangeListParams`](./src/super_market/types/exchange_list_params.py) |
| Response | [`ExchangeListResponse`](./src/super_market/types/exchange_list_response.py) |

```python
exchange = client.exchanges.list(
    limit=50,
)
```

### Get exchange price

Returns the latest price, best bid, best ask, and spread for a single exchange (the API's tradable-contract unit). Best bid, best ask, and spread come from the same resting order book as `/exchanges/{id}/orderbook`. All prices are YES-normalized (0–1 probability). Pass `tournamentId` to get that tournament's price and bid/ask. When an organization-bound key omits it, this singular endpoint deterministically uses the organization's default tournament; an unbound key uses the public context. In tournament context, `latestPrice` is null until a tournament trade establishes a price; resting bids or asks may still exist, and the value never falls back to the global price.

| Direction | Type |
| --- | --- |
| Request | [`ExchangeListPriceParams`](./src/super_market/types/exchange_list_price_params.py) |
| Response | [`ExchangeListPriceResponse`](./src/super_market/types/exchange_list_price_response.py) |

```python
exchange = client.exchanges.list_price(
    id="36",
)
```

### Get exchange orderbook

Returns the limit order book for a single exchange (tradable contract). Prices are YES-normalized (0–1). Bids are sorted descending, asks ascending. `asOf` is the engine version the book was read at, `{ sequence, at }`, the same version realtime `books` carry (compare by `sequence`, then `at`); it is null when the book is served without an engine version. Pass `tournamentId` for one explicit tournament-isolated book. When an organization-bound key omits it, this singular endpoint deterministically uses the organization's default tournament; an unbound key uses the public book.

| Direction | Type |
| --- | --- |
| Request | [`ExchangeListOrderbookParams`](./src/super_market/types/exchange_list_orderbook_params.py) |
| Response | [`ExchangeListOrderbookResponse`](./src/super_market/types/exchange_list_orderbook_response.py) |

```python
exchange = client.exchanges.list_orderbook(
    id="36",
    depth=20,
)
```

### Get exchange price history

Returns OHLCV candles computed from trade history. All prices are YES-normalized, and buckets with no trades are omitted (sparse series). Without `from`, the response contains the newest `limit` candles ending at `to`. With `from`, candles are returned forward from that timestamp; if the requested window exceeds the bucket cap, the response contains the oldest `limit` candles and `coverage.complete` is false. For a capped explicit-from page, response `to` is the next candle's start and is an exclusive continuation boundary. Response `from` and `to` describe the window actually served. An explicit `from` or `to` is floored to the selected resolution's candle boundary; a range whose floored end is not after its floored start returns 400 `VALIDATION_ERROR`. Pass `tournamentId` for one explicit accessible tournament. When an organization-bound key omits it, the request uses the organization's default tournament; an unbound key uses public-global trade history.

| Direction | Type |
| --- | --- |
| Request | [`ExchangeListPriceHistoryParams`](./src/super_market/types/exchange_list_price_history_params.py) |
| Response | [`ExchangeListPriceHistoryResponse`](./src/super_market/types/exchange_list_price_history_response.py) |

```python
exchange = client.exchanges.list_price_history(
    id="36",
    resolution="1h",
    limit=200,
)
```

### Get exchange trade tape

Returns the trade tape for a single exchange, newest first, cursor-paginated. Prices are YES-normalized so the series is directly comparable to `/price` and `/price-history`. Pass `tournamentId` for one explicit accessible tournament. When an organization-bound key omits it, the request uses the organization's default tournament; an unbound key uses public-global trades.

| Direction | Type |
| --- | --- |
| Request | [`ExchangeListTradesParams`](./src/super_market/types/exchange_list_trades_params.py) |
| Response | [`ExchangeListTradesResponse`](./src/super_market/types/exchange_list_trades_response.py) |

```python
exchange = client.exchanges.list_trades(
    id="36",
    limit=50,
)
```

### Bulk price snapshot

Returns latest price, best bid, best ask, and spread for up to 100 exchanges in a single round-trip. Same per-exchange shape as `/exchanges/{id}/price`; each quote comes from the same resting order book as `/exchanges/{id}/orderbook`. Pass `tournamentId` for one explicit accessible tournament. When an organization-bound key omits it, the request uses the organization's default tournament; an unbound key uses the public-global context. IDs outside the resolved context are returned in `missingIds`, and response `data` preserves request order.

| Direction | Type |
| --- | --- |
| Request | [`ExchangeListPricesParams`](./src/super_market/types/exchange_list_prices_params.py) |
| Response | [`ExchangeListPricesResponse`](./src/super_market/types/exchange_list_prices_response.py) |

```python
exchange = client.exchanges.list_prices(
    ids="36,37,42",
)
```

## `Orders`

Place, inspect, and cancel limit or market orders.

### Place order

Unaccepted current documents return 403 `TERMS_NOT_ACKNOWLEDGED` with `error.details.missingDocuments`; each entry contains `documentId`, `kind`, `version`, `organizationId`, `organizationSlug`, `organizationName`, `supportEmail`, `currencyName`, `url`, and `host`. Places a single limit or market order. A required client-supplied `idempotencyKey` identifies the logical placement: retrying the same key with the same resolved payload replays the exact stored response before mutable settlement or market preflights, while reuse with a different resolved payload returns 409. Fresh limit prices must be on the 0.005 tick between 0.005 and 0.995; `price: 1` for a buy and `price: 0` for a sell encode market orders, and off-tick values return 400 `VALIDATION_ERROR`. Omit `price` for a market order (fills at best available price). An organization-bound key defaults an omitted `tournamentId` to the organization's default tournament; an unbound key defaults to the public global context. On engine-routed scopes, an opposite-signed `BUY` nets against the existing position: it reduces or crosses the position at FIFO lot cost. Inspect `avgCost` and `lots` on the corresponding global or tournament portfolio-position read to understand the surviving position's display average and cost lots. On engine-routed scopes, a fully-backed `SELL` closes conventionally; a `SELL` that is flat, opposite the held side, or larger than the held quantity is canonicalized by the engine into its complement `BUY` (`sell yes q@p` ≡ `buy no q@(1−p)`), and the response's canonical `action`/`side`/`price`/`quantity` report the order as placed. Resting quotes on both sides are allowed; an order that would cross your own resting order fills other counterparties, then its crossing remainder is cancelled with `terminalReasonCode: "SelfTradePrevented"`. The nullable `all` response reports authoritative engine-calculated capital efficiency and collateral encumbrance for the execution. On engine-routed scopes a buy is admitted against your cash balance, and resting orders do not escrow cash: it moves only on fills. A buy the full balance cannot pay for even one share of is rejected with 400 `VALIDATION_ERROR` (insufficient funds). A buy is accepted as a no-op (`orderId: null`, `open: false`, nothing placed or traded) when your unexpired resting buys on the same exchange and tournament already commit the whole balance. Resting buys on other exchanges are not counted, so your resting buys across exchanges can add up to more than your balance. An order's resting remainder is sized to what your full current balance can cover, and a later balance decrease shrinks or cancels resting buys you can no longer afford. Buying the outcome opposite a position you hold nets the shares and credits 1 per netted share, so your balance change differs from `totalCost`.

| Direction | Type |
| --- | --- |
| Request | [`OrderCreateParams`](./src/super_market/types/order_create_params.py) |
| Response | [`OrderCreateResponse`](./src/super_market/types/order_create_response.py) |

```python
order = client.orders.create(
    exchange_id="36",
    side="yes",
    action="buy",
    quantity=100,
    idempotency_key="order-placement-2026-07-23-001",
)
```

### List orders

Returns the authenticated user's orders. Defaults to open orders only. When `tournamentId` is omitted, an organization-bound key reads its organization's default tournament orders and an unbound key reads public global orders. Engine-backed responses include projection `coverage` metadata.

| Direction | Type |
| --- | --- |
| Request | [`OrderListParams`](./src/super_market/types/order_list_params.py) |
| Response | [`OrderListResponse`](./src/super_market/types/order_list_response.py) |

```python
order = client.orders.list(
    status="open",
    limit=50,
)
```

### Place batch orders

Consent is checked per item: an unaccepted current document returns item status 403 with `data.error.code: TERMS_NOT_ACKNOWLEDGED` and `data.error.details.missingDocuments`. Other items can succeed. Places up to 50 orders in a single request under one required client-supplied `idempotencyKey`. For requests first bound after the original-routing rollout is enabled, completed batches retain each originally omitted tournament scope across organization default changes and backend routing changes; older requests without routing evidence retain their existing conflict behavior. Incomplete batches retain their original scope/backend retry fences. Reusing a key from another authenticated organization conflicts. The ordered, resolved batch is the request identity: a completed retry with the same key and payload replays the exact stored 200, 207, or 422 envelope without placing another order, while reuse with a different batch returns 409. Freshly executed engine-routed items report the canonical `action`/`side`/`price`/`quantity`/`terminalReasonCode` as placed; items stored before this change replay without those fields. If any item returns 429 or 5xx, the outer batch remains incomplete; retry with the same key to replay terminal indexes and resume only those non-terminal indexes. Orders are placed one at a time under a bounded execution budget: a batch that cannot finish within it stops issuing further orders and returns 503, keeping every order it already placed — retry with the same key to resume from where it stopped, as many times as needed until a final 200, 207, or 422. Large batches under heavy load are the case that reaches this. A batch with at least one success returns 207 with per-item statuses even when another item is transient. An item rate limited by the trading engine reports status 429 with `data.code: RATE_LIMITED`; nothing was placed for it. A failed item's `data` keeps the error payload of the placement path that rejected it rather than the top-level error envelope: commonly a bare `{ error: "…" }`, sometimes with a `code`; rate-limited items use `{ code: "RATE_LIMITED", error: "…" }`; and consent failures use `{ error: { code, message, details } }`. A zero-success batch returns 429 with the per-item results when every item was rate limited, 502 with per-item `ORDER_STATUS_UNKNOWN` codes when every item has an unknown dispatch outcome, and 503 for any other zero-success batch with a transient item, including a mix of terminal failures and rate-limited items. When a rate-limited item supplied a `Retry-After`, the 207, 429, or 503 response carries the longest one; it may be absent otherwise. After a completed 207, resubmit failed items under a new batch key. Fresh limit prices must be on the 0.005 tick between 0.005 and 0.995; `price: 1` for a buy and `price: 0` for a sell encode market orders, and off-tick values return 400 `VALIDATION_ERROR`. For an organization-bound key, each order that omits `tournamentId` defaults to the organization's default tournament; unbound keys retain the public global default. All orders are validated upfront — if any fail validation the entire request is rejected with 400 before any orders are placed. Execution is best-effort: each order is attempted independently and a failure does not roll back already-placed orders. Use /orders/multi-leg instead if you need an all-or-nothing guarantee. Returns 200 if all succeed, 207 when at least one succeeds and at least one fails (207 does not mean partial fills), 422 if all fail terminally, 429 if every item was rate limited, 502 if every item has an unknown dispatch outcome, or 503 when no item succeeds and another transient outcome remains or the batch stopped at its execution budget with orders still unissued.

| Direction | Type |
| --- | --- |
| Request | [`OrderCreateBatchParams`](./src/super_market/types/order_create_batch_params.py) |
| Response | [`OrderCreateBatchResponse`](./src/super_market/types/order_create_batch_response.py) |

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

### Place multi-leg order

Unaccepted current documents return 403 `TERMS_NOT_ACKNOWLEDGED` with `error.details.missingDocuments`; each entry contains `documentId`, `kind`, `version`, `organizationId`, `organizationSlug`, `organizationName`, `supportEmail`, `currencyName`, `url`, and `host`. Consent preflight checks the union of documents required by all legs before any leg executes. Places up to 10 orders atomically within a single transaction. For requests first bound after the original-routing rollout is enabled, a completed response retains originally omitted tournament scopes across organization default and backend changes. Ordered legs, explicit scope, relationshipConstraint, economics and original authenticated organization still identify the retry. Historical requests without routing evidence keep existing scope conflicts; incomplete requests retain their leases and backend routing fences. A required client-supplied `idempotencyKey` identifies the logical placement: the same key with the same resolved legs and constraint has no second economic effect in either scope, while reuse with a different payload returns 409. Fresh limit prices must be on the 0.005 tick between 0.005 and 0.995; `price: 1` for a buy and `price: 0` for a sell encode market orders, and off-tick values return 400 `VALIDATION_ERROR`. For an organization-bound key, each leg that omits `tournamentId` defaults to the organization's default tournament; unbound keys retain the public global default. All legs succeed or none are persisted — if any leg fails, the entire request rolls back and no orders are placed. Every leg must route to the same backend: a request mixing engine-routed and non-engine scopes returns 400 `VALIDATION_ERROR`. Engine-routed legs must all belong to the same organization; otherwise the request returns 400 `VALIDATION_ERROR`. Optional `relationshipConstraint` validates every leg against one active canonical ALL relationship using an engine preflight price snapshot taken immediately before dispatch. This validation is not held under the engine execution lock or re-evaluated atomically during execution, so a concurrent fill or graph change can create a later violation; observe subsequent violations through GET `/relationships/constraints` and violation broadcasts. When `relationshipConstraint` is supplied, duplicate legs for the same exchange in the same tournament scope return 400 `VALIDATION_ERROR` before engine state is read; without a constraint, duplicate legs are not rejected for that reason. Price validation evaluates every leg in YES terms: YES limit prices are unchanged, NO limit prices use their YES-complement price, and uncovered nodes or market orders use current engine prices. Exhaustive mutually exclusive relationships require sum(P) = 1; non-exhaustive mutually exclusive relationships require sum(P) ≤ 1. Unknown or inactive relationships, outsider exchanges, and violated price bounds return 422 `RELATIONSHIP_VIOLATION`; an unavailable engine graph or price read fails closed with 503. relationshipConstraint is part of the app-level idempotency request identity. An engine-routed retry with the same complete identity replays the recorded response before preflight is repeated; an incomplete claim after response loss resumes with the same engine key so the engine rehydrates the accepted command. Use /orders/batch instead if partial success is acceptable. Leg execution errors preserve their underlying v1 error status and include `details.leg` with the zero-based failed leg index. Each successful engine-routed leg includes per-leg `terminalReasonCode` when available. Each successful leg includes nullable authoritative `all` execution economics.

| Direction | Type |
| --- | --- |
| Request | [`OrderCreateMultiLegParams`](./src/super_market/types/order_create_multi_leg_params.py) |
| Response | [`OrderCreateMultiLegResponse`](./src/super_market/types/order_create_multi_leg_response.py) |

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

### Get order

Returns an order owned by the authenticated user. The order ID determines its trading context; organization-bound keys may only read orders in accessible tournaments belonging to their bound organization.

| Direction | Type |
| --- | --- |
| Response | [`Order`](./src/super_market/types/order.py) |

```python
order = client.orders.retrieve(
    id="1001",
)
```

### Cancel order

Cancels an open order. The order ID determines its trading context; organization-bound keys may only cancel orders in accessible tournaments belonging to their bound organization.

| Direction | Type |
| --- | --- |
| Response | [`OrderDeleteResponse`](./src/super_market/types/order_delete_response.py) |

```python
order = client.orders.delete(
    id="1001",
)
```

### Cancel all orders

Cancels open orders for the authenticated user in one trading context.

Scoping behavior:
- No body / empty body — an organization-bound key cancels its organization's default tournament orders; an unbound key cancels public global orders
- `{ exchangeId }` — narrows that default context to one exchange
- `{ marketId }` — narrows that default context to all exchanges in one market
- `{ tournamentId }` — uses that explicit accessible tournament; combine with `exchangeId` or `marketId` to narrow further
- `exchangeId` + `marketId` together — rejected with 400 (mutually exclusive)

An omitted or empty body cancels every open order in the resolved context. A supplied body must be valid JSON matching the schema, whatever its Content-Type; otherwise the request is rejected with 400 and nothing is cancelled.

Cancels the caller's open, unexpired orders in that context, in batches of up to 500. `cancelled` counts the orders this request removed; orders that were already filled or cancelled are not counted. Returns 200 once no targeted order remains open. Returns 503 if cancellation paused before it finished (the trading engine was briefly unavailable, or the request ran out of time); `error.details.cancelled` reports the progress so far. Retry the same request until it returns 200. A 503 without `error.details.cancelled` was refused before anything was cancelled and is safe to retry.

| Direction | Type |
| --- | --- |
| Request | [`OrderCreateCancelAllParams`](./src/super_market/types/order_create_cancel_all_params.py) |
| Response | [`OrderCreateCancelAllResponse`](./src/super_market/types/order_create_cancel_all_response.py) |

```python
order = client.orders.create_cancel_all(
    exchange_id="36",
)
```

### Get order fills

Returns one newest-first page of fills for a specific order. `totalQuantityFilled` and `avgFillPrice` are exact lifecycle totals for the whole order, independent of the current page. The order ID determines its trading context; organization-bound keys may only read fills for orders in accessible tournaments belonging to their bound organization.

| Direction | Type |
| --- | --- |
| Request | [`OrderListFillsParams`](./src/super_market/types/order_list_fills_params.py) |
| Response | [`OrderListFillsResponse`](./src/super_market/types/order_list_fills_response.py) |

```python
order = client.orders.list_fills(
    id="1001",
    limit=50,
)
```

## `Portfolio`

Read-only views of the authenticated user's portfolio, including scope-aware ALL collateral, open positions, trade and transaction history, and P&L analytics.

### Get ALL collateral

Returns the authenticated user's component-level ALL collateral advances and guaranteed payout floors. When `tournamentId` is omitted, an organization-bound key reads its organization's default tournament and an unbound key reads the public global context. An explicit `tournamentId` reads one accessible tournament; organization-bound keys are limited to tournaments in their bound organization.

| Direction | Type |
| --- | --- |
| Request | [`PortfolioListCollateralParams`](./src/super_market/types/portfolio_list_collateral_params.py) |
| Response | [`PortfolioListCollateralResponse`](./src/super_market/types/portfolio_list_collateral_response.py) |

```python
portfolio = client.portfolio.list_collateral()
```

### Get open positions

Returns open positions for the authenticated user with FIFO lot breakdown and unrealized P&L. An organization-bound key resolves this endpoint to its organization's default tournament and uses tournament valuation prices; an unbound key reads global positions. Use `/tournaments/{slug}/portfolio/positions` for an explicit tournament scope.

| Direction | Type |
| --- | --- |
| Response | [`PortfolioListPositionsResponse`](./src/super_market/types/portfolio_list_positions_response.py) |

```python
portfolio = client.portfolio.list_positions()
```

### Get P&L summary

Returns account value, unrealized P&L, period P&L (vs the applicable stored-history baseline), ROI, and annualized Sharpe ratio. An organization-bound key resolves this endpoint to its organization's default tournament and uses the tournament's virtual balance, valuation prices, snapshots, and initial virtual balance; an unbound key reads global portfolio state. Use `/tournaments/{slug}/portfolio/pnl` for an explicit tournament scope.

| Direction | Type |
| --- | --- |
| Request | [`PortfolioListPnlParams`](./src/super_market/types/portfolio_list_pnl_params.py) |
| Response | [`PortfolioListPnlResponse`](./src/super_market/types/portfolio_list_pnl_response.py) |

```python
portfolio = client.portfolio.list_pnl(
    period="quarter",
)
```

### Get portfolio value history

Returns continuous time-series portfolio value. An organization-bound key resolves this endpoint to its organization's default tournament and uses tournament snapshots, the member's joined-at seed when no snapshot exists, and a live tournament valuation; an unbound key reads global portfolio history. Use `/tournaments/{slug}/portfolio/history` for an explicit tournament scope. Under global engine authority, legacy daily snapshots strictly before the configured cutover are stitched to projection-backed points at and after the cutover, followed by a live engine-valued point. Before authority opens, the legacy daily-snapshot behavior is unchanged. The requested window is capped per interval — `1h` 31 days, `6h` 366 days, `1d` 1827 days, `1w` 1827 days, `all` 1827 days — and a longer range is rejected rather than truncated. Responses carry at most 2000 points; a series with more is thinned evenly, always keeping the first and last.

| Direction | Type |
| --- | --- |
| Request | [`PortfolioListHistoryParams`](./src/super_market/types/portfolio_list_history_params.py) |
| Response | [`PortfolioListHistoryResponse`](./src/super_market/types/portfolio_list_history_response.py) |

```python
portfolio = client.portfolio.list_history(
    interval="1d",
)
```

### Get transaction history

Returns a cursor-paginated audit trail of trades and transactions, newest first. An organization-bound key resolves this endpoint to its organization's default tournament; an unbound key reads global transactions. Use `/tournaments/{slug}/portfolio/transactions` for an explicit tournament scope.

| Direction | Type |
| --- | --- |
| Request | [`PortfolioListTransactionsParams`](./src/super_market/types/portfolio_list_transactions_params.py) |
| Response | [`PortfolioListTransactionsResponse`](./src/super_market/types/portfolio_list_transactions_response.py) |

```python
portfolio = client.portfolio.list_transactions(
    limit=50,
)
```

### List settlements

Returns settlement entries (win/loss/refund/correction) for the authenticated user. An organization-bound key resolves this endpoint to its organization's default tournament; an unbound key reads global settlements. Use `/tournaments/{slug}/portfolio/settlements` for an explicit tournament scope.

| Direction | Type |
| --- | --- |
| Request | [`PortfolioListSettlementsParams`](./src/super_market/types/portfolio_list_settlements_params.py) |
| Response | [`PortfolioListSettlementsResponse`](./src/super_market/types/portfolio_list_settlements_response.py) |

```python
portfolio = client.portfolio.list_settlements(
    limit=50,
)
```

### List fills

Returns all trade fills for the authenticated user across all orders, newest first. An organization-bound key resolves an omitted `tournamentId` to its organization's default tournament; an unbound key reads global fills. For per-order fills with aggregate stats, use `GET /orders/{id}/fills`. Every response includes projection `coverage` metadata.

| Direction | Type |
| --- | --- |
| Request | [`PortfolioListFillsParams`](./src/super_market/types/portfolio_list_fills_params.py) |
| Response | [`PortfolioListFillsResponse`](./src/super_market/types/portfolio_list_fills_response.py) |

```python
portfolio = client.portfolio.list_fills(
    limit=50,
)
```

## `Account`

View profile and balance for the authenticated API key holder.

### Get account

Returns the profile and balance of the authenticated API key holder. For an organization-bound key, `balance` comes from the organization's default tournament: enrolled members receive that tournament's balance (engine-authoritative when routed), while an organization member pending enrolment receives its initial virtual balance. An unbound key retains the public-global cash balance.

| Direction | Type |
| --- | --- |
| Response | [`AccountListResponse`](./src/super_market/types/account_list_response.py) |

```python
account = client.account.list()
```

## `Tournaments`

Private tournaments with isolated virtual-currency orderbooks.

### List my tournaments

Returns all tournaments the authenticated user can access, including open organization tournaments before first-action enrolment. Owners and admins of an organization also see every private tournament of that organization before they join.

| Direction | Type |
| --- | --- |
| Request | [`TournamentListParams`](./src/super_market/types/tournament_list_params.py) |
| Response | [`TournamentListResponse`](./src/super_market/types/tournament_list_response.py) |

```python
tournament = client.tournaments.list(
    status="any",
    limit=50,
    offset=0,
)
```

### Get tournament

Returns metadata and the authenticated member's current virtual balance for the tournament. The response `id` is the tournament UUID to pass as `tournamentId` on exchange price/orderbook and trading requests; the path itself uses the stable slug. Returns 403 if the caller is not a member, unless the tournament is open or the caller owns or administers the tournament's organization.

| Direction | Type |
| --- | --- |
| Response | [`TournamentRetrieveResponse`](./src/super_market/types/tournament_retrieve_response.py) |

```python
tournament = client.tournaments.retrieve(
    slug="alpha-tournament",
)
```

### Get tournament leaderboard

Returns members ranked within the tournament by the selected `sort` (P&L by default). `rank` and `myRank` follow the selected sort, and `myRank` is computed against the **same period** as the rankings list. `null` if the caller has not traded in the period (unranked). Ranks use standard competition ranking: tied entries share a rank and the positions that follow skip by the size of the tie (1-1-3).

**Period semantics (calendar-aligned, UTC):**
- `1d` — Today (since 00:00 UTC today)
- `7d` — This Week (since 00:00 UTC on the most recent Sunday)
- `30d` — This Month (since 00:00 UTC on the 1st of the current month)
- `all` — All-time

Baselines come from the daily tournament-portfolio snapshot taken at 00:00 UTC.

On **Ongoing Play** tournaments, rankings never cross a season reset: `all` covers the current season, and `1d`/`7d`/`30d` start no earlier than the last reset.

`groupId` filters to members of a user group bound to the tournament. Ongoing Play tournaments additionally support `season` (archived snapshots). An archived `season` key requires `period=all`; its entries use the archived shape (`finalTotalValue` / `finalBalance` instead of `pnl`), and the response omits `sort`.

| Direction | Type |
| --- | --- |
| Request | [`TournamentListLeaderboardParams`](./src/super_market/types/tournament_list_leaderboard_params.py) |
| Response | [`TournamentListLeaderboardResponse`](./src/super_market/types/tournament_list_leaderboard_response.py) |

```python
tournament = client.tournaments.list_leaderboard(
    slug="alpha-tournament",
    period="all",
    limit=50,
    offset=0,
    sort="pnl",
)
```

### List tournament seasons

Lists the current season + archived snapshots for an **Ongoing Play** tournament. Returns 404 for other tournaments, which have no seasons.

| Direction | Type |
| --- | --- |
| Response | [`TournamentListSeasonsResponse`](./src/super_market/types/tournament_list_seasons_response.py) |

```python
tournament = client.tournaments.list_seasons(
    slug="alpha-tournament",
)
```

### `Tournaments Markets`

Private tournaments with isolated virtual-currency orderbooks.

#### List tournament markets

Equivalent explicit tournament-scoped view of `GET /markets?tournamentId={id}`, addressed by slug. Returns exchange IDs and tournament-specific prices. Use the tournament UUID from `GET /tournaments/{slug}` as `tournamentId` on downstream exchange price/orderbook and trading requests so every call resolves the same isolated context. Only accessible to authorized organization/tournament members and to owners or admins of the tournament's organization.

| Direction | Type |
| --- | --- |
| Request | [`MarketListParams`](./src/super_market/types/tournaments/market_list_params.py) |
| Response | [`MarketListResponse`](./src/super_market/types/tournaments/market_list_response.py) |

```python
market = client.tournaments.markets.list(
    slug="alpha-tournament",
    limit=20,
    status="any",
)
```

#### Get tournament market

Returns a single market's detail with tournament-specific prices and the tournament-scoped orderbook embedded per exchange. Each exchange's embedded book carries `asOf`, the engine version it was read at, `{ sequence, at }`, the same version realtime `books` carry (compare by `sequence`, then `at`); it is null when the book is served without an engine version. `latestPrice` is null when no tournament trade has established a price, even when bids or asks are resting, and never falls back to the global exchange price. Returns 404 if the market is not assigned to this tournament.

| Direction | Type |
| --- | --- |
| Response | [`MarketRetrieveResponse`](./src/super_market/types/tournaments/market_retrieve_response.py) |

```python
market = client.tournaments.markets.retrieve(
    slug="alpha-tournament",
    id="26",
)
```

### `Tournaments Portfolio`

Private tournaments with isolated virtual-currency orderbooks.

#### Get tournament positions

Returns the caller's open positions within the tournament with FIFO lot breakdown and unrealized P&L. Prices use tournament valuation_price. If nonzero holdings exist without valuation_price, returns 409 instead of valuing them at a neutral default.

| Direction | Type |
| --- | --- |
| Response | [`PortfolioListPositionsResponse`](./src/super_market/types/tournaments/portfolio_list_positions_response.py) |

```python
portfolio = client.tournaments.portfolio.list_positions(
    slug="alpha-tournament",
)
```

#### Get tournament transactions

Returns a cursor-paginated audit trail of the caller's trades and transactions within the tournament, newest first.

| Direction | Type |
| --- | --- |
| Request | [`PortfolioListTransactionsParams`](./src/super_market/types/tournaments/portfolio_list_transactions_params.py) |
| Response | [`PortfolioListTransactionsResponse`](./src/super_market/types/tournaments/portfolio_list_transactions_response.py) |

```python
portfolio = client.tournaments.portfolio.list_transactions(
    slug="alpha-tournament",
    limit=50,
)
```

#### List tournament fills

Returns all trade fills for the caller within this tournament, newest first.

| Direction | Type |
| --- | --- |
| Request | [`PortfolioListFillsParams`](./src/super_market/types/tournaments/portfolio_list_fills_params.py) |
| Response | [`PortfolioListFillsResponse`](./src/super_market/types/tournaments/portfolio_list_fills_response.py) |

```python
portfolio = client.tournaments.portfolio.list_fills(
    slug="alpha-tournament",
    limit=50,
)
```

#### Get tournament portfolio value history

Returns the caller's tournament portfolio-value series from tournament snapshots plus a live tournament valuation. A member with no snapshots receives an initial-virtual-balance seed at their joined-at time. The requested window is capped per interval — `1h` 31 days, `6h` 366 days, `1d` 1827 days, `1w` 1827 days, `all` 1827 days — and responses carry at most 2000 points.

| Direction | Type |
| --- | --- |
| Request | [`PortfolioListHistoryParams`](./src/super_market/types/tournaments/portfolio_list_history_params.py) |
| Response | [`PortfolioListHistoryResponse`](./src/super_market/types/tournaments/portfolio_list_history_response.py) |

```python
portfolio = client.tournaments.portfolio.list_history(
    slug="alpha-tournament",
    interval="1d",
)
```

#### List tournament settlements

Returns settlement entries (win/loss/refund/correction) for the caller within this tournament. Payouts apply to the tournament virtual balance.

| Direction | Type |
| --- | --- |
| Request | [`PortfolioListSettlementsParams`](./src/super_market/types/tournaments/portfolio_list_settlements_params.py) |
| Response | [`PortfolioListSettlementsResponse`](./src/super_market/types/tournaments/portfolio_list_settlements_response.py) |

```python
portfolio = client.tournaments.portfolio.list_settlements(
    slug="alpha-tournament",
    limit=50,
)
```

#### Get tournament P&L

Returns the caller's tournament account value, unrealized P&L, period P&L, ROI, and Sharpe ratio. All figures are scoped to the tournament's virtual balance and tournament valuation prices. If nonzero holdings exist without valuation_price, returns 409 instead of valuing them at a neutral default. Bounded periods are rolling windows measured back from the request time (`day` 1, `week` 7, `month` 30, `quarter` 90, `year` 365 days), unlike the calendar-aligned leaderboard periods. Period P&L and ROI use the latest tournament snapshot at or before the period start, falling back to the initial virtual balance for members who joined inside the window; `periodPnl` is null for `all`. For `period=all`, ROI is computed relative to the tournament's initial virtual balance. Sharpe is the mean daily return over its standard deviation annualized by √252, and null when the daily returns have no usable variance.

| Direction | Type |
| --- | --- |
| Request | [`PortfolioListPnlParams`](./src/super_market/types/tournaments/portfolio_list_pnl_params.py) |
| Response | [`PortfolioListPnlResponse`](./src/super_market/types/tournaments/portfolio_list_pnl_response.py) |

```python
portfolio = client.tournaments.portfolio.list_pnl(
    slug="alpha-tournament",
    period="quarter",
)
```

### `Tournaments Me`

Private tournaments with isolated virtual-currency orderbooks.

#### Get my tournament smart score

Returns the caller's Smart Score entries for this tournament, one row per `marketType` the caller has been scored in. Smart Score is the time-decayed composite produced by the trader-scoring pipeline (combines PnL, ROI, win rate, and Sharpe-scaled volatility). `isElite=true` means the caller is in the latest elite cut for that marketType. Empty array when the caller has no metrics snapshot yet in this tournament.

| Direction | Type |
| --- | --- |
| Response | [`MeListSmartScoreResponse`](./src/super_market/types/tournaments/me_list_smart_score_response.py) |

```python
me = client.tournaments.me.list_smart_score(
    slug="alpha-tournament",
)
```

## `Leaderboards`

Rankings across global trading or a tournament, by P&L or another selected sort.

### Get a leaderboard (global or tournament-scoped)

Returns a leaderboard ranked by P&L. When `tournamentSlug` is omitted, an organization-bound API key defaults to its organization's default tournament; an unbound key ranks across global trading (`tournament_id IS NULL`). When supplied, `tournamentSlug` explicitly scopes the response to that tournament's members. Tournament-scoped requests, whether explicit or organization-defaulted, unlock the `groupId` and `sort` filters. Ranks use standard competition ranking: tied entries share a rank and the positions that follow skip by the size of the tie (1-1-3).

**Period semantics (calendar-aligned, UTC):**
- `1d` — Today (since 00:00 UTC today)
- `7d` — This Week (since 00:00 UTC on the most recent Sunday)
- `30d` — This Month (since 00:00 UTC on the 1st of the current month)
- `quarter` — Since 00:00 UTC on the first day of the current calendar quarter
- `all` — All-time

`groupId` and `sort` are rejected with 400 only when the request resolves to the global leaderboard (user groups are tournament-scoped; the global query path doesn't honor `sort` and always orders by P&L).

| Direction | Type |
| --- | --- |
| Request | [`LeaderboardListParams`](./src/super_market/types/leaderboard_list_params.py) |
| Response | [`LeaderboardListResponse`](./src/super_market/types/leaderboard_list_response.py) |

```python
leaderboard = client.leaderboards.list(
    period="all",
    limit=50,
    offset=0,
)
```

## `Dmm`

Designated-market-maker endpoints for platform administrators and organization owners/admins managing resources in their own organization.

### List failed autosettlements

<p class="api-access-notice"><span class="api-access-badge">Platform admin only</span><span class="api-access-detail">Unavailable to organization API keys.</span></p>

Queue of contracts the autosettlers couldn't resolve (`settlement_failed = true` and still unsettled). Use the existing market settle UI to manually resolve them — this endpoint is read-only.

For platform administrators only: the queue spans every organization, so organization owners and admins receive 403.

Sorted by `settlementRetryCount` descending, so abandoned contracts (retry count at the cap) come first, then by oldest `lastCheckAttempt`, then by contract ID. Abandoned contracts will not be retried by cron — manual resolution is the only path forward.

| Direction | Type |
| --- | --- |
| Request | [`DmmListFailedAutosettlementParams`](./src/super_market/types/dmm_list_failed_autosettlement_params.py) |
| Response | [`DesignatedMarketMakerFailedSettlementList`](./src/super_market/types/designated_market_maker_failed_settlement_list.py) |

```python
dmm = client.dmm.list_failed_autosettlement()
```

### Get org-wide user rankings

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Cross-tournament user rankings scoped to a single organization. An organization-bound API key reads its own organization; it may pass its own `organizationSlug`, but naming another organization's slug returns 403 and an unknown slug returns 404. Platform administrators must pass `organizationSlug` to choose the organization. Reads from the latest `organization_trader_metrics` snapshot for the requested `marketType` by default. Returns one row per org member with rank, Smart Score, ROI, Sharpe (scaled), win rate, realized/unrealized PnL, stake, trade counts, and elite flag.

In each member row, `hasSetUsername` indicates the handle is finalized and displayable — chosen by the participant or generated by the organization's automatic-username policy.

Pass `userGroupId` to restrict rows to members of a user group inside this organization; ranks are recomputed within the filtered set.

Pass `marketGroupId` and/or `period` to switch to an on-demand recompute that scopes trader metrics to trades inside that market group and/or within the calendar-aligned window. The response `computed` field indicates which path served the request. Ranks use standard competition ranking: tied entries share a rank and the positions that follow skip by the size of the tie (1-1-3).

| Direction | Type |
| --- | --- |
| Request | [`DmmListRankingsParams`](./src/super_market/types/dmm_list_rankings_params.py) |
| Response | [`DesignatedMarketMakerOrgRankings`](./src/super_market/types/designated_market_maker_org_rankings.py) |

```python
dmm = client.dmm.list_rankings()
```

### `Dmm Tournaments`

Designated-market-maker endpoints for platform administrators and organization owners/admins managing resources in their own organization.

#### List tournaments

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Admin-only endpoint that lists tournaments, optionally scoped to a single organization. Requires an API key with the `admin` scope.

| Direction | Type |
| --- | --- |
| Request | [`TournamentListParams`](./src/super_market/types/dmm/tournament_list_params.py) |
| Response | [`DesignatedMarketMakerTournamentList`](./src/super_market/types/dmm/designated_market_maker_tournament_list.py) |

```python
tournament = client.dmm.tournaments.list()
```

#### Create tournament

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Admin-only designated-market-maker endpoint for creating an organization-scoped tournament. Requires an API key with the `admin` scope and an admin role on the caller's account.

Optional `marketGroupIds` / `userGroupIds` bind existing groups of the tournament's organization in the same transaction as the tournament row; the response echoes the bound ids. The groups' markets and members are then materialized asynchronously, exactly as when a group is bound later.

| Direction | Type |
| --- | --- |
| Request | [`TournamentCreateParams`](./src/super_market/types/dmm/tournament_create_params.py) |
| Response | [`DesignatedMarketMakerTournamentCreate`](./src/super_market/types/dmm/designated_market_maker_tournament_create.py) |

```python
tournament = client.dmm.tournaments.create(
    name="Alpha Tournament",
    end_date="2026-07-01T00:00:00.000Z",
    organization_slug="acme-corp",
)
```

#### Update tournament

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Admin-only designated-market-maker endpoint for updating tournament settings. Requires an API key with the `admin` scope and an admin role on the caller's account. The body must contain at least one field, and unknown fields are rejected.

- Ended tournaments cannot be modified (409).
- `startDate` must not be more than 60 seconds in the past whenever it is supplied (400), even when it equals the stored start, so omit it unless you are changing it. Changing it is allowed only while the tournament is a draft (not yet started); otherwise 409.
- `initialVirtualBalance` can change only while the tournament is a draft; otherwise 409. Sending the current value is accepted. Changing it on a draft resets every existing member's balance to the new amount.
- `endDate` must be after the start date (400), and an active tournament cannot be given an `endDate` in the past (409).
- Currency name changes are rejected after the tournament's first trade (409); sending the current currency name remains valid. A name that diverges from a locked organization currency name returns 400.
- The organization's default tournament cannot be made `private` (409). The visibility of Ongoing Play cannot be changed (400), and a tournament without an organization cannot be made `open` (400).
- `autoEnrollOnSignup: true` requires an open, scheduled organization tournament (400 otherwise).
- While another tournament operation (such as a balance reset) is in progress, the update returns 409; retry after it completes.

| Direction | Type |
| --- | --- |
| Request | [`TournamentUpdateParams`](./src/super_market/types/dmm/tournament_update_params.py) |
| Response | [`DesignatedMarketMakerTournament`](./src/super_market/types/dmm/designated_market_maker_tournament.py) |

```python
tournament = client.dmm.tournaments.update(
    slug="alpha-tournament",
)
```

#### Delete draft tournament

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Admin-only designated-market-maker endpoint for deleting a draft tournament. Active and ended tournaments cannot be deleted, nor can the organization's default tournament or a tournament with an attached market already settled for its organization. The API key's owner must have an email address, which is recorded in the deletion audit.

```python
client.dmm.tournaments.delete(
    slug="alpha-tournament",
)
```

#### Reset tournament balances

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Admin-only endpoint that cancels open tournament orders, deletes tournament-scoped holdings, position lots, portfolio snapshots, and the tournament's super-signal data (market signals, signal elites, signal trader metrics, and cohort cuts), and resets every member balance to the tournament's initial virtual balance. Each affected member gets a `BALANCE_RESET` ledger transaction for the difference. Past trades and transactions remain for audit. Ended tournaments cannot be reset. The API key's owner must have an email address, which is recorded in the admin audit.

**Destructive.** Body must contain `{ "confirm": "<slug>", "resetKey": "<stable-key>" }`; `confirm` must match the path slug. The client-supplied `resetKey` is required so timeouts and lost responses can be retried safely. A committed attempt replays its stored response without repeating the destructive DB or engine phases; an interrupted attempt is resumed. Treat `503 TX_CONFLICT` as transient and retry with backoff using the same key.

| Direction | Type |
| --- | --- |
| Request | [`TournamentCreateResetBalancesParams`](./src/super_market/types/dmm/tournament_create_reset_balances_params.py) |
| Response | [`DesignatedMarketMakerResetBalances`](./src/super_market/types/dmm/designated_market_maker_reset_balances.py) |

```python
tournament = client.dmm.tournaments.create_reset_balances(
    slug="alpha-tournament",
    confirm="alpha-tournament",
    reset_key="quarterly-reset-2026-q3",
)
```

#### Get per-tournament user rankings

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Per-tournament user rankings. Requires owner/admin role in the tournament's organization. Reads from the latest `tournament_trader_metrics` snapshot for the requested `marketType` by default, joined with `tournament_members` so members without a snapshot still appear (with zeroed metric fields). Adds the current authoritative engine balance and exposes it as a sortable column.

Pass `userGroupId` to restrict rows to members of a user group bound to this tournament; ranks are recomputed within the filtered set.

Pass `marketGroupId` and/or `period` to switch to an on-demand recompute that scopes trader metrics to trades inside that market group and/or within the calendar-aligned window. The response `computed` field indicates which path served the request. Ranks use standard competition ranking: tied entries share a rank and the positions that follow skip by the size of the tie (1-1-3).

| Direction | Type |
| --- | --- |
| Request | [`TournamentListRankingsParams`](./src/super_market/types/dmm/tournament_list_rankings_params.py) |
| Response | [`DesignatedMarketMakerTournamentRankings`](./src/super_market/types/dmm/designated_market_maker_tournament_rankings.py) |

```python
tournament = client.dmm.tournaments.list_rankings(
    slug="alpha-tournament",
)
```

#### List tournament market assignments

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Returns administrative assignment metadata for markets attached directly or supplied by bound market groups, newest first, with opaque cursor pagination. This is not a market-data feed: use `/markets` with the appropriate API-key scope or `tournamentId` for exchange IDs and prices.

| Direction | Type |
| --- | --- |
| Request | [`TournamentListMarketAssignmentsParams`](./src/super_market/types/dmm/tournament_list_market_assignments_params.py) |
| Response | [`TournamentListMarketAssignmentsResponse`](./src/super_market/types/dmm/tournament_list_market_assignments_response.py) |

```python
tournament = client.dmm.tournaments.list_market_assignments(
    slug="alpha-tournament",
)
```

#### List executed trades

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Returns executed trades for the league, newest first, with both sides' identity fields. Org-scoped: an org API key may only read its own organization's tournaments. Supports `from`/`to` windowing and opaque cursor pagination.

| Direction | Type |
| --- | --- |
| Request | [`TournamentListTradesParams`](./src/super_market/types/dmm/tournament_list_trades_params.py) |
| Response | [`DesignatedMarketMakerTradeList`](./src/super_market/types/dmm/designated_market_maker_trade_list.py) |

```python
designated_market_maker_trades = client.dmm.tournaments.list_trades(
    slug="alpha-tournament",
)
```

#### List orders

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Returns orders placed in the league, newest first, with the placing trader's identity fields. Org-scoped. Supports `from`/`to` windowing and opaque cursor pagination.

| Direction | Type |
| --- | --- |
| Request | [`TournamentListOrdersParams`](./src/super_market/types/dmm/tournament_list_orders_params.py) |
| Response | [`DesignatedMarketMakerOrderList`](./src/super_market/types/dmm/designated_market_maker_order_list.py) |

```python
designated_market_maker_orders = client.dmm.tournaments.list_orders(
    slug="alpha-tournament",
)
```

#### List virtual-balance ledger

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Returns the league's virtual-balance ledger (opening balances, nominal trade cost/proceeds, separate ALL collateral advances/repayments/releases, settlement payouts/refunds/corrections, and balance resets), newest first, with the affected trader's identity fields. The nominal execution price is never rewritten: a collateral entry records the capital-efficiency adjustment atomically alongside its trade or lifecycle command. Tournaments run on virtual currency, so there are no real-money deposits, withdrawals, or fees. Org-scoped. Supports `from`/`to` windowing and opaque cursor pagination.

| Direction | Type |
| --- | --- |
| Request | [`TournamentListTransactionsParams`](./src/super_market/types/dmm/tournament_list_transactions_params.py) |
| Response | [`DesignatedMarketMakerTransactionList`](./src/super_market/types/dmm/designated_market_maker_transaction_list.py) |

```python
designated_market_maker_transactions = client.dmm.tournaments.list_transactions(
    slug="alpha-tournament",
)
```

#### Market-maker inventory and exposure

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Read-only snapshot of the managed `market_maker`'s inventory and risk across one P2P tournament. The maker's position is synthetic (it holds no `holdings` rows), so net inventory and net cash are reconstructed from its filled trades. Returns one row per outcome that the maker either holds inventory on or is quoting on (fully-closed, unquoted outcomes are omitted), grouped by market with a tournament-level rollup. Each row reports net inventory + net cash, mark-to-market value + unrealized PnL (via the tournament valuation price), resting bid/ask exposure, and worst-case settlement loss. Same admin / org-ownership gates as the liquidity endpoints.

| Direction | Type |
| --- | --- |
| Request | [`TournamentListInventoryParams`](./src/super_market/types/dmm/tournament_list_inventory_params.py) |
| Response | [`DmmInventory`](./src/super_market/types/dmm/dmm_inventory.py) |

```python
tournament = client.dmm.tournaments.list_inventory(
    slug="alpha-tournament",
)
```

#### `Dmm Tournaments EndSettlement`

Designated-market-maker endpoints for platform administrators and organization owners/admins managing resources in their own organization.

##### Preview end-settlement

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Preview prices for closing out tournament-scoped positions in markets that haven't yet resolved at tournament end. Review before calling POST. Available only once the tournament has ended.

Per exchange: `proposedPrice` (5h VWAP default), `proposedPriceSource` (`vwap` / `cfmm_pool` / `seed` / `backfilled` / `admin_override` / `dmm_submission` / `missing` — treat `seed`/`missing` with suspicion), `lastTradePrice` (for divergence-spotting), and `needsSubmittedPrice` (`true` when engine trading activity or nonzero app holdings exist without a valuation: POST must supply a `submittedPrices` row for that exchange). Untraded tournament scopes with no app holdings are reset automatically during closeout.

| Direction | Type |
| --- | --- |
| Response | [`DesignatedMarketMakerEndSettlementPreview`](./src/super_market/types/dmm/tournaments/designated_market_maker_end_settlement_preview.py) |

```python
end_settlement = client.dmm.tournaments.end_settlement.list(
    slug="alpha-tournament",
)
```

##### Queue end-settlement

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Queues the strict tournament end-settlement closeout. The worker writes submitted missing final prices, cancels open tournament orders, settles tournament-scoped engine positions and app holdings, deletes app holdings and position lots, enqueues untraded-scope resets in the transactional engine outbox, and refreshes the final snapshot in one all-or-failed transaction. The POST response is `202 Accepted` after the background event is dispatched; use the status endpoint to poll lifecycle progress.

Exchanges flagged `needsSubmittedPrice` in the preview must be supplied in `submittedPrices`; boundary prices 0 and 1 are accepted. A `resolved_outcomes` tournament with unresolved attached markets returns a 409 `awaiting_market_resolution` response with the unresolved market list. Submitting prices for exchanges that already have a proposed valuation returns 409. Already settled tournaments reject another initial end-settlement command; use retrospective settlement overrides after payout.

| Direction | Type |
| --- | --- |
| Request | [`EndSettlementCreateParams`](./src/super_market/types/dmm/tournaments/end_settlement_create_params.py) |
| Response | [`DesignatedMarketMakerEndSettlementQueue`](./src/super_market/types/dmm/tournaments/designated_market_maker_end_settlement_queue.py) |

```python
end_settlement = client.dmm.tournaments.end_settlement.create(
    slug="alpha-tournament",
)
```

##### Get end-settlement status

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Returns the current asynchronous final-settlement lifecycle and redacted attempt view for an ended tournament. DMM responses expose safe aggregate status, missing-price blockers, retry/action flags, and sanitized errors; they do not expose stack traces, member-level payout detail, or raw API-key identifiers.

| Direction | Type |
| --- | --- |
| Response | [`DesignatedMarketMakerSettlementStatus`](./src/super_market/types/dmm/tournaments/designated_market_maker_settlement_status.py) |

```python
end_settlement = client.dmm.tournaments.end_settlement.list_status(
    slug="alpha-tournament",
)
```

#### `Dmm Tournaments SettlementOverrides`

Designated-market-maker endpoints for platform administrators and organization owners/admins managing resources in their own organization.

##### Preview settlement corrections

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Non-mutating preview for retrospective settlement valuation corrections after tournament end-settlement has already paid out an exchange. The API key needs the admin scope, and its owner must be a platform administrator or an owner/admin of the tournament's organization. An explicitly organization-bound key is restricted to that organization. Only ended tournaments are eligible. Each target exchange must already be closed out with no open tournament holdings. Use this endpoint to review per-member deltas before calling the execute endpoint.

| Direction | Type |
| --- | --- |
| Request | [`SettlementOverrideCreatePreviewParams`](./src/super_market/types/dmm/tournaments/settlement_override_create_preview_params.py) |
| Response | [`DesignatedMarketMakerSettlementOverridePreview`](./src/super_market/types/dmm/tournaments/designated_market_maker_settlement_override_preview.py) |

```python
settlement_override = client.dmm.tournaments.settlement_overrides.create_preview(
    slug="alpha-tournament",
    reason="Corrected official final valuation from settlement desk review.",
    overrides=[{"exchange_id": "1234", "price": 0.75}],
)
```

##### Execute settlement corrections

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Atomically applies retrospective settlement valuation corrections after tournament end-settlement has already paid out an exchange. The API key needs the admin scope, and its owner must be a platform administrator or an owner/admin of the tournament's organization. An explicitly organization-bound key is restricted to that organization. Execution writes signed MARKET_SETTLEMENT_CORRECTION audit rows, increments affected tournament-member balances, updates exchange valuation state, and refreshes downstream tournament portfolio snapshots at the original tournament end date. Concurrent corrections for the same tournament/exchanges are serialized.

| Direction | Type |
| --- | --- |
| Request | [`SettlementOverrideCreateParams`](./src/super_market/types/dmm/tournaments/settlement_override_create_params.py) |
| Response | [`DesignatedMarketMakerSettlementOverrideExecution`](./src/super_market/types/dmm/tournaments/designated_market_maker_settlement_override_execution.py) |

```python
settlement_override = client.dmm.tournaments.settlement_overrides.create(
    slug="alpha-tournament",
    reason="Corrected official final valuation from settlement desk review.",
    overrides=[{"exchange_id": "1234", "price": 0.75}],
)
```

#### `Dmm Tournaments Markets`

Designated-market-maker endpoints for platform administrators and organization owners/admins managing resources in their own organization.

##### List tournament market assignments (deprecated)

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Deprecated compatibility alias for `GET /dmm/tournaments/{slug}/market-assignments`. It returns assignment metadata, not exchange IDs or tournament pricing. Every response carries `Deprecation: true` and a `Link` header naming the successor endpoint. New integrations should use the successor endpoint.

| Direction | Type |
| --- | --- |
| Request | [`MarketListParams`](./src/super_market/types/dmm/tournaments/market_list_params.py) |
| Response | [`MarketListResponse`](./src/super_market/types/dmm/tournaments/market_list_response.py) |

```python
market = client.dmm.tournaments.markets.list(
    slug="alpha-tournament",
)
```

##### Add market to tournament

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Attach a market to this tournament directly. Seeds tournament-scoped exchange state and CFMM orderbook (when applicable). Rejects ended and archived tournaments and markets attached to another organization.

If the market is already in the tournament only because a bound market group supplies it, the same request promotes it to a direct assignment and returns 200 with the same body; nothing is re-seeded, and unbinding the group no longer removes it.

| Direction | Type |
| --- | --- |
| Request | [`MarketCreateParams`](./src/super_market/types/dmm/tournaments/market_create_params.py) |
| Response | [`MarketCreateResponse`](./src/super_market/types/dmm/tournaments/market_create_response.py) |

```python
market = client.dmm.tournaments.markets.create(
    slug="alpha-tournament",
    market_id="26",
)
```

##### Remove market from tournament

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Removes a directly assigned market. When the market is assigned only directly, this cancels open orders, pays holders out at the tournament's `valuation_price`, and deletes tournament-scoped exchange state; the response reports `exchangesCleared` and `paidOutHoldings`.

When a bound market group also supplies the market, nothing is removed: the assignment is demoted to group-sourced and the response is `{ success: true, demoted: true }`. The market then leaves the tournament only when its last group source goes. A market supplied only by a group cannot be removed here (409); remove it from the group or unbind the group instead.

| Direction | Type |
| --- | --- |
| Response | [`MarketDeleteResponse`](./src/super_market/types/dmm/tournaments/market_delete_response.py) |

```python
market = client.dmm.tournaments.markets.delete(
    slug="slug",
    market_id="marketId",
)
```

#### `Dmm Tournaments Members`

Designated-market-maker endpoints for platform administrators and organization owners/admins managing resources in their own organization.

##### List tournament members

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

| Direction | Type |
| --- | --- |
| Response | [`MemberListResponse`](./src/super_market/types/dmm/tournaments/member_list_response.py) |

```python
member = client.dmm.tournaments.members.list(
    slug="alpha-tournament",
)
```

##### Add tournament member

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Add a member by username or email. The user must already belong to the tournament's organization. Idempotent: re-adding flags the row as `added_directly`.

| Direction | Type |
| --- | --- |
| Request | [`MemberCreateParams`](./src/super_market/types/dmm/tournaments/member_create_params.py) |
| Response | [`DmmTournamentMemberAdd`](./src/super_market/types/dmm/tournaments/dmm_tournament_member_add.py) |

```python
member = client.dmm.tournaments.members.create(
    slug="alpha-tournament",
)
```

##### Remove tournament member

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Removes a directly added member. The member's open tournament orders are cancelled and their tournament holdings, position lots, and membership are deleted with no payout; the forfeit is then applied in the trading engine asynchronously. Removing a member from an active tournament records an exit that blocks them from rejoining it (`rejoinBlocked: true`); removal from a tournament that has not started does not.

When a bound user group also supplies the member, nothing is removed: the membership is demoted to group-sourced and the response is `{ success: true, demoted: true }`. A member supplied only by a group cannot be removed here (409); remove them from the group or unbind the group instead.

| Direction | Type |
| --- | --- |
| Response | [`MemberDeleteResponse`](./src/super_market/types/dmm/tournaments/member_delete_response.py) |

```python
member = client.dmm.tournaments.members.delete(
    slug="slug",
    profile_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### `Dmm Tournaments MarketGroups`

Designated-market-maker endpoints for platform administrators and organization owners/admins managing resources in their own organization.

##### List org market groups (with binding status)

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Lists market groups in the tournament's organization, newest first, flagging which are bound to this tournament and when. Supports opaque cursor pagination.

| Direction | Type |
| --- | --- |
| Request | [`MarketGroupListParams`](./src/super_market/types/dmm/tournaments/market_group_list_params.py) |
| Response | [`MarketGroupListResponse`](./src/super_market/types/dmm/tournaments/market_group_list_response.py) |

```python
market_group = client.dmm.tournaments.market_groups.list(
    slug="alpha-tournament",
)
```

##### Bind market group

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Bind a market group to the tournament. Group must belong to the tournament's organization. Triggers an inngest reconcile that materializes the group's markets into `tournament_markets` asynchronously.

| Direction | Type |
| --- | --- |
| Request | [`MarketGroupCreateParams`](./src/super_market/types/dmm/tournaments/market_group_create_params.py) |
| Response | [`MarketGroupCreateResponse`](./src/super_market/types/dmm/tournaments/market_group_create_response.py) |

```python
market_group = client.dmm.tournaments.market_groups.create(
    slug="alpha-tournament",
    market_group_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

##### Unbind market group

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Unbind a market group from the tournament. An asynchronous reconciliation then removes every market that loses its last source: markets the group supplied that are not directly assigned and not supplied by another bound group. Each removed market has its open orders cancelled and its holders paid out at the tournament's valuation price, as with DELETE /dmm/tournaments/{slug}/markets/{marketId}.

Because removal settles held positions, the unbind is refused with 409 while any of the group's exchanges with holdings has no tournament valuation price (`details.missingValuations`).

| Direction | Type |
| --- | --- |
| Response | [`MarketGroupDeleteResponse`](./src/super_market/types/dmm/tournaments/market_group_delete_response.py) |

```python
market_group = client.dmm.tournaments.market_groups.delete(
    slug="slug",
    group_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### `Dmm Tournaments UserGroups`

Designated-market-maker endpoints for platform administrators and organization owners/admins managing resources in their own organization.

##### List org user groups (with binding status)

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Lists user groups in the tournament's organization, newest first, flagging which are bound to this tournament and when. Supports opaque cursor pagination.

| Direction | Type |
| --- | --- |
| Request | [`UserGroupListParams`](./src/super_market/types/dmm/tournaments/user_group_list_params.py) |
| Response | [`UserGroupListResponse`](./src/super_market/types/dmm/tournaments/user_group_list_response.py) |

```python
user_group = client.dmm.tournaments.user_groups.list(
    slug="alpha-tournament",
)
```

##### Bind user group

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Bind a user group to the tournament. Triggers an inngest reconcile that materializes the group's members into `tournament_members` asynchronously.

| Direction | Type |
| --- | --- |
| Request | [`UserGroupCreateParams`](./src/super_market/types/dmm/tournaments/user_group_create_params.py) |
| Response | [`UserGroupCreateResponse`](./src/super_market/types/dmm/tournaments/user_group_create_response.py) |

```python
user_group = client.dmm.tournaments.user_groups.create(
    slug="alpha-tournament",
    user_group_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

##### Unbind user group

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Unbind a user group from the tournament. An asynchronous reconciliation then removes every member who loses their last source: members the group supplied who were not added directly and are not supplied by another bound group. Each removed member forfeits as with DELETE /dmm/tournaments/{slug}/members/{profileId}: open orders are cancelled and holdings are deleted with no payout, and removal from an active tournament blocks them from rejoining it.

| Direction | Type |
| --- | --- |
| Response | [`UserGroupDeleteResponse`](./src/super_market/types/dmm/tournaments/user_group_delete_response.py) |

```python
user_group = client.dmm.tournaments.user_groups.delete(
    slug="slug",
    group_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### `Dmm Tournaments Exchanges`

Designated-market-maker endpoints for platform administrators and organization owners/admins managing resources in their own organization.

##### Seed tournament exchange liquidity

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Endpoint for appending or replacing managed market-maker liquidity on one P2P tournament exchange orderbook. The API key needs the admin scope, and its owner must be a platform administrator or an owner/admin of the organization that owns the tournament. An explicitly organization-bound key is restricted to that organization. Submitted levels can match executable user liquidity, but market-maker self-matching is rejected. `append` and `replace` each require a client-supplied `operationKey` on both engine and legacy paths; retry the same mode and payload with the same key for replay, and expect 409 if that mode's key is reused with a changed payload. A completed request replays its stored status and body, so a stored 400, 404, or 409 outcome (for example an engine rejection or a closed market) is returned again for the same key and payload; send a new key once the cause is fixed. Retryable 503 outcomes are not stored. The key namespace is per operation type, so `append:K` and `replace:K` are independent and may both execute. For `replace`, existing rungs with the same side, price, and remaining quantity are retained with their order IDs and queue priority. Only changed or removed rungs are cancelled, so an identical re-quote is a no-op. `replace` may submit an empty book to clear managed liquidity; `append` must include at least one level. Prices must be unique per side, and submitted bids and asks must not cross: a highest bid at or above the lowest ask returns 400.

| Direction | Type |
| --- | --- |
| Request | [`ExchangeCreateLiquidityParams`](./src/super_market/types/dmm/tournaments/exchange_create_liquidity_params.py) |
| Response | [`DesignatedMarketMakerLiquidity`](./src/super_market/types/dmm/tournaments/designated_market_maker_liquidity.py) |

```python
exchange = client.dmm.tournaments.exchanges.create_liquidity(
    slug="alpha-tournament",
    exchange_id="36",
    mode="append",
    operation_key="jerry-liquidity-2026-07-15-001",
)
```

##### Sweep tournament exchange liquidity

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Emergency risk-off for one tournament exchange orderbook. Cancels every `market_maker`-owned open order on `(tournamentSlug, exchangeId)`. No-op when nothing is resting. Same admin / org-ownership gates as the POST. The optional `Idempotency-Key` header identifies the sweep for safe retries; omission makes every request a new sweep.

| Direction | Type |
| --- | --- |
| Response | [`ExchangeDeleteLiquidityResponse`](./src/super_market/types/dmm/tournaments/exchange_delete_liquidity_response.py) |

```python
exchange = client.dmm.tournaments.exchanges.delete_liquidity(
    slug="alpha-tournament",
    exchange_id="36",
)
```

### `Dmm Relationships`

Designated-market-maker endpoints for platform administrators and organization owners/admins managing resources in their own organization.

#### Establish an ALL relationship

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Creates and immediately activates one manual canonical ALL relationship. Callers choose markets and outcomes; the API translates them to engine exchanges. Every selected market must belong exclusively to the API key's organization. The optional body `idempotencyKey` identifies the logical mutation for safe retries; omission gives each request a fresh operation identity. A transport-ambiguous outcome returns 202 with an operation ID to poll. Requires an API key with `admin` scope and an organization owner/admin or platform-admin principal.

The trading engine evaluates at most 12 free variables per connected relationship component: every distinct exchange across the relationships that share exchanges with this one, excluding exchanges a Boolean relationship produces as its output. The limit applies to the whole component the new relationship would join or merge, not to the inputs of this request; a relationship that would push its component past 12 free variables is rejected with 400.

| Direction | Type |
| --- | --- |
| Request | [`RelationshipCreateParams`](./src/super_market/types/dmm/relationship_create_params.py) |
| Response | [`RelationshipCreateResponse`](./src/super_market/types/dmm/relationship_create_response.py) |

```python
relationship = client.dmm.relationships.create(
    type="Implication",
    antecedent={"market_id": "26", "exchange_id": "36"},
    consequent={"market_id": "26", "exchange_id": "36"},
)
```

#### Deactivate an ALL relationship

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Disables a canonical ALL relationship through the trading engine and never hard-deletes it. The optional `Idempotency-Key` header identifies the logical mutation for safe retries; omission gives each request a fresh operation identity. A transport-ambiguous outcome returns 202 with an operation ID to poll. Organization-bound keys may deactivate a relationship only when every node exchange belongs exclusively to their organization; platform administrators are not organization-scoped. The engine may reject a status change that would make outstanding collateral unsafe. Requires an API key with `admin` scope and an organization owner/admin or platform-admin principal.

| Direction | Type |
| --- | --- |
| Response | [`RelationshipDeleteResponse`](./src/super_market/types/dmm/relationship_delete_response.py) |

```python
relationship = client.dmm.relationships.delete(
    relationship_id="550e8400-e29b-41d4-a716-446655440000",
)
```

#### Get an ALL relationship operation

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Returns durable status for a relationship create or disable operation after a 202 response. Poll until `status` is `succeeded` or `failed`. An organization key can poll only its organization's operations; an operation owned by another organization returns the same 404 as an unknown operation ID. A platform key can poll any organization-owned operation, including those it created on an organization's behalf, plus its own.

| Direction | Type |
| --- | --- |
| Response | [`DesignatedMarketMakerRelationshipOperationStatus`](./src/super_market/types/dmm/designated_market_maker_relationship_operation_status.py) |

```python
relationship = client.dmm.relationships.retrieve_operations(
    operation_id="550e8400-e29b-41d4-a716-446655440000",
)
```

#### Reconcile organization-derived ALL relationships

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Derives and reconciles only relationships whose exchanges belong exclusively to one organization. Relationships owned by another organization or spanning organization boundaries are never mutated. Requires an API key with `admin` scope.

Engine synchronization runs asynchronously and withholds any derived relationship whose connected component would exceed the engine's 12-free-variable limit (the superseded definition it would replace stays in place). Those skips are recorded in server diagnostics, not in this response.

| Direction | Type |
| --- | --- |
| Request | [`RelationshipCreateReconcileParams`](./src/super_market/types/dmm/relationship_create_reconcile_params.py) |
| Response | [`RelationshipCreateReconcileResponse`](./src/super_market/types/dmm/relationship_create_reconcile_response.py) |

```python
relationship = client.dmm.relationships.create_reconcile()
```

### `Dmm Icims`

Designated-market-maker endpoints for platform administrators and organization owners/admins managing resources in their own organization.

#### Export iCIMS-qualified candidates

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Manual trigger for the org's iCIMS data export. Evaluates the configured tag rules against every organization member and returns the qualifying candidates with the iCIMS tags and job requisitions they earned, ordered by org-aggregate Smart Score (strongest first). Read-only — it never calls the iCIMS API, so it works even when the push integration is disabled or has no credentials. An organization-bound API key exports its own organization; it may pass its own `organizationSlug`, but naming another organization's slug returns 403 and an unknown slug returns 404. Platform administrators must pass `organizationSlug` to choose the organization.

`contactOptIn` is true when the member opted in, false when the member registered without opting in, and null when no registration was collected for that organization.

The admin Web UI consumes the same export as a CSV download.

| Direction | Type |
| --- | --- |
| Request | [`IcimListExportParams`](./src/super_market/types/dmm/icim_list_export_params.py) |
| Response | [`DesignatedMarketMakerIcimsExport`](./src/super_market/types/dmm/designated_market_maker_icims_export.py) |

```python
icim = client.dmm.icims.list_export()
```

### `Dmm TraderAnalytics`

Designated-market-maker endpoints for platform administrators and organization owners/admins managing resources in their own organization.

#### Elite cohort summary

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Snapshot of the elite cohort for the caller's organization (or a specific tournament when `tournamentId` is supplied): latest cut timestamp, cohort size and smart-score band, the platform-wide thresholds used by the scoring pipeline, and the top 10 elites by decayed smart score.

When `tournamentId` is supplied the cohort and top performers are read from `tournament_elites` / `tournament_trader_metrics`; otherwise from `organization_elites` / `organization_trader_metrics`.

| Direction | Type |
| --- | --- |
| Request | [`TraderAnalyticListEliteSummaryParams`](./src/super_market/types/dmm/trader_analytic_list_elite_summary_params.py) |
| Response | [`DmmTraderAnalyticsEliteSummary`](./src/super_market/types/dmm/dmm_trader_analytics_elite_summary.py) |

```python
trader_analytic = client.dmm.trader_analytics.list_elite_summary()
```

#### `Dmm TraderAnalytics Users`

Designated-market-maker endpoints for platform administrators and organization owners/admins managing resources in their own organization.

##### List trader analytics

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Org-scoped trader analytics with optional tournament / user-group / market-group / period filters and elite / score / trade thresholds.

Pass `tournamentId` to scope to a single tournament (must belong to your organization); otherwise the request is org-wide.

Metrics are recomputed on-demand for each request from the trade fact tables — they reflect the current scope and window, not the persisted daily snapshot. `computedAsOf` reflects the recompute timestamp.

| Direction | Type |
| --- | --- |
| Request | [`UserListParams`](./src/super_market/types/dmm/trader_analytics/user_list_params.py) |
| Response | [`DmmTraderAnalyticsUsersList`](./src/super_market/types/dmm/trader_analytics/dmm_trader_analytics_users_list.py) |

```python
dmm_trader_analytics_users = client.dmm.trader_analytics.users.list()
```

##### Get trader analytics for a single user

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Returns the on-demand metrics row for a single trader in the requested scope, plus a per-market-type breakdown from the latest persisted snapshot and an optional daily smart-score history (up to 30 points).

The trader must be a member of the resolved org (or, when `tournamentId` is supplied, the tournament). The `categories` and `history` arrays are always read from `organization_trader_metrics` and therefore reflect organization-wide data even when the metrics row itself is tournament-scoped.

| Direction | Type |
| --- | --- |
| Request | [`UserRetrieveParams`](./src/super_market/types/dmm/trader_analytics/user_retrieve_params.py) |
| Response | [`DmmTraderAnalyticsUserDetail`](./src/super_market/types/dmm/trader_analytics/dmm_trader_analytics_user_detail.py) |

```python
user = client.dmm.trader_analytics.users.retrieve(
    profile_id="550e8400-e29b-41d4-a716-446655440000",
)
```

### `Dmm Groups`

Designated-market-maker endpoints for platform administrators and organization owners/admins managing resources in their own organization.

#### `Dmm Groups Markets`

Designated-market-maker endpoints for platform administrators and organization owners/admins managing resources in their own organization.

##### List market groups

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Lists market groups in the caller's organization. Admin-scoped. Cursor-paginated (offset).

| Direction | Type |
| --- | --- |
| Request | [`MarketListParams`](./src/super_market/types/dmm/groups/market_list_params.py) |
| Response | [`MarketListResponse`](./src/super_market/types/dmm/groups/market_list_response.py) |

```python
market = client.dmm.groups.markets.list(
    limit=25,
)
```

##### Create market group

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Creates a market group. Slug auto-generated from name when omitted. Platform-admin callers must include `organizationSlug`.

| Direction | Type |
| --- | --- |
| Request | [`MarketCreateParams`](./src/super_market/types/dmm/groups/market_create_params.py) |
| Response | [`Group`](./src/super_market/types/dmm/groups/group.py) |

```python
market = client.dmm.groups.markets.create(
    name="Earnings Markets",
)
```

##### Get market group

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Reads a single market group by ID.

| Direction | Type |
| --- | --- |
| Response | [`Group`](./src/super_market/types/dmm/groups/group.py) |

```python
market = client.dmm.groups.markets.retrieve(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

##### Update market group

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Updates a market group's name, slug, or description. Each field is optional, but the body must contain at least one of them.

| Direction | Type |
| --- | --- |
| Request | [`MarketUpdateParams`](./src/super_market/types/dmm/groups/market_update_params.py) |
| Response | [`Group`](./src/super_market/types/dmm/groups/group.py) |

```python
market = client.dmm.groups.markets.update(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

##### Delete market group

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Deletes a market group and its membership rows. In tournaments the group is bound to that have ended, the markets it supplied are kept as direct assignments so the historical record stays intact. In bound tournaments that have not ended (archived tournaments are left unchanged), the markets that lose their last source are removed by asynchronous reconciliation, which cancels their open orders and pays holders out at the tournament's valuation price. Because of that payout, the delete is refused with 409 while any of the group's exchanges with holdings in such a tournament has no tournament valuation price (`details.tournamentId`, `details.missingValuations`).

| Direction | Type |
| --- | --- |
| Response | [`MarketDeleteResponse`](./src/super_market/types/dmm/groups/market_delete_response.py) |

```python
market = client.dmm.groups.markets.delete(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

##### List market group members

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Lists the markets in a market group. Admin-scoped. Cursor-paginated (offset).

| Direction | Type |
| --- | --- |
| Request | [`MarketListMembersParams`](./src/super_market/types/dmm/groups/market_list_members_params.py) |
| Response | [`MarketListMembersResponse`](./src/super_market/types/dmm/groups/market_list_members_response.py) |

```python
market = client.dmm.groups.markets.list_members(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    limit=25,
)
```

##### Add market group members

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Bulk-adds markets to a market group (up to 500 per call). Ids that are malformed, unknown, or not visible to your organization are reported in `notFound` rather than failing the call. Additions propagate to every bound tournament that has not ended.

| Direction | Type |
| --- | --- |
| Request | [`MarketCreateMembersParams`](./src/super_market/types/dmm/groups/market_create_members_params.py) |
| Response | [`MarketGroupMemberAddResult`](./src/super_market/types/dmm/groups/market_group_member_add_result.py) |

```python
market = client.dmm.groups.markets.create_members(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    market_ids=["1042", "1043"],
)
```

##### Remove market group members

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Removes markets from a market group (up to 500 per call). Requires a request body; pass a one-element array to remove a single market. Removal settles positions held in bound tournaments, so any market whose exchanges still have holdings but no tournament valuation price is left in place and reported in `blocked`; the rest of the batch proceeds. Markets sourced into an *ended* tournament are pinned in place first.

| Direction | Type |
| --- | --- |
| Request | [`MarketDeleteMembersParams`](./src/super_market/types/dmm/groups/market_delete_members_params.py) |
| Response | [`MarketGroupMemberRemoveResult`](./src/super_market/types/dmm/groups/market_group_member_remove_result.py) |

```python
market = client.dmm.groups.markets.delete_members(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    market_ids=["1042", "1043"],
)
```

#### `Dmm Groups Users`

Designated-market-maker endpoints for platform administrators and organization owners/admins managing resources in their own organization.

##### List user groups

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Lists user groups in the caller's organization. Admin-scoped. Cursor-paginated (offset).

| Direction | Type |
| --- | --- |
| Request | [`UserListParams`](./src/super_market/types/dmm/groups/user_list_params.py) |
| Response | [`UserListResponse`](./src/super_market/types/dmm/groups/user_list_response.py) |

```python
user = client.dmm.groups.users.list(
    limit=25,
)
```

##### Create user group

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Creates a user group. Slug auto-generated from name when omitted. Platform-admin callers must include `organizationSlug`.

| Direction | Type |
| --- | --- |
| Request | [`UserCreateParams`](./src/super_market/types/dmm/groups/user_create_params.py) |
| Response | [`Group`](./src/super_market/types/dmm/groups/group.py) |

```python
user = client.dmm.groups.users.create(
    name="Earnings Markets",
)
```

##### Get user group

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Reads a single user group by ID.

| Direction | Type |
| --- | --- |
| Response | [`Group`](./src/super_market/types/dmm/groups/group.py) |

```python
user = client.dmm.groups.users.retrieve(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

##### Update user group

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Updates a user group's name, slug, or description. Each field is optional, but the body must contain at least one of them.

| Direction | Type |
| --- | --- |
| Request | [`UserUpdateParams`](./src/super_market/types/dmm/groups/user_update_params.py) |
| Response | [`Group`](./src/super_market/types/dmm/groups/group.py) |

```python
user = client.dmm.groups.users.update(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

##### Delete user group

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Deletes a user group and its membership rows. In tournaments the group is bound to that have ended, the members it supplied are kept as direct members so the historical record stays intact. In bound tournaments that have not ended (archived tournaments are left unchanged), the members who lose their last source are removed by asynchronous reconciliation: their open orders are cancelled and holdings deleted with no payout, and removal from an active tournament blocks them from rejoining it.

| Direction | Type |
| --- | --- |
| Response | [`UserDeleteResponse`](./src/super_market/types/dmm/groups/user_delete_response.py) |

```python
user = client.dmm.groups.users.delete(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

##### List user group members

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Lists the profiles in a user group. Admin-scoped. Cursor-paginated (offset).

| Direction | Type |
| --- | --- |
| Request | [`UserListMembersParams`](./src/super_market/types/dmm/groups/user_list_members_params.py) |
| Response | [`UserListMembersResponse`](./src/super_market/types/dmm/groups/user_list_members_response.py) |

```python
user = client.dmm.groups.users.list_members(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    limit=25,
)
```

##### Add user group members

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Bulk-adds profiles to a user group (up to 500 per call). Only profiles already in the group's organization are added directly. Anyone else is emailed an organization invitation (reported in `invited`) and joins the group when they sign in on the organization's site; an admin never enrols anyone in an organization. Profiles already in a different organization are reported in `rejected` and not added. Additions propagate to every bound tournament that has not ended.

| Direction | Type |
| --- | --- |
| Request | [`UserCreateMembersParams`](./src/super_market/types/dmm/groups/user_create_members_params.py) |
| Response | [`UserGroupMemberAddResult`](./src/super_market/types/dmm/groups/user_group_member_add_result.py) |

```python
user = client.dmm.groups.users.create_members(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

##### Remove user group members

<p class="api-access-notice"><span class="api-access-badge">Admin only</span><span class="api-access-detail">Unavailable to participant API keys.</span></p>

Removes profiles from a user group (up to 500 per call). Requires a request body; pass a one-element array to remove a single member. Ids holding no membership row are reported in `notFound`. Members this group sourced into an *ended* tournament are pinned in place first — ended tournaments are frozen historical records.

| Direction | Type |
| --- | --- |
| Request | [`UserDeleteMembersParams`](./src/super_market/types/dmm/groups/user_delete_members_params.py) |
| Response | [`UserGroupMemberRemoveResult`](./src/super_market/types/dmm/groups/user_group_member_remove_result.py) |

```python
user = client.dmm.groups.users.delete_members(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    profile_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
)
```

## `Realtime`

Mint short-lived JWTs for Realtime WebSocket channels (market price feed, user fills, order updates).

### Mint realtime token

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

| Direction | Type |
| --- | --- |
| Response | [`RealtimeCreateTokenResponse`](./src/super_market/types/realtime_create_token_response.py) |

```python
realtime = client.realtime.create_token()
```

## `RelationshipsAll`

Read the canonical Advanced Logic Linking graph, inspect engine-evaluated price constraints, and understand relationship-backed capital efficiency.

### List market relationships

Returns active canonical ALL relationships from the trading engine, enriched with market titles and outcome labels. Filter by a market to fetch every relationship touching any exchange in that market, or by one exchange. `marketId` and `exchangeId` are mutually exclusive.

| Direction | Type |
| --- | --- |
| Request | [`RelationshipsAllListRelationshipsParams`](./src/super_market/types/relationships_all_list_relationships_params.py) |
| Response | [`RelationshipsAllListRelationshipsResponse`](./src/super_market/types/relationships_all_list_relationships_response.py) |

```python
relationships_all = client.relationships_all.list_relationships(
    depth=1,
    limit=100,
)
```

### Get a market relationship graph

Traverses the canonical engine-owned ALL graph outward from every exchange in one accessible market and returns deduplicated relationships plus their labeled exchange nodes.

| Direction | Type |
| --- | --- |
| Request | [`RelationshipsAllListGraphParams`](./src/super_market/types/relationships_all_list_graph_params.py) |
| Response | [`RelationshipsAllListGraphResponse`](./src/super_market/types/relationships_all_list_graph_response.py) |

```python
relationships_all = client.relationships_all.list_graph(
    market_id="36",
    depth=2,
)
```

### Evaluate relationship price constraints

Returns engine-computed price-constraint evaluations. This endpoint reports satisfied, violated, and unevaluable states; Next.js does not recompute or reinterpret the engine's result.

| Direction | Type |
| --- | --- |
| Request | [`RelationshipsAllListConstraintsParams`](./src/super_market/types/relationships_all_list_constraints_params.py) |
| Response | [`RelationshipsAllListConstraintsResponse`](./src/super_market/types/relationships_all_list_constraints_response.py) |

```python
relationships_all = client.relationships_all.list_constraints(
    violations_only="false",
    min_violation=0.01,
)
```
