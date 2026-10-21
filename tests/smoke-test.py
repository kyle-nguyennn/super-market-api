# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke test: calls every generated operation once to confirm the SDK can reach each endpoint.
# Run it from this repo with `python tests/smoke-test.py`. The generator also runs this file
# against a mock server and reads the JSON report produced via SCALAR_SMOKE_REPORT.
from __future__ import annotations

import json
import os
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Callable, TypedDict

from super_market import SuperMarketAPI

# The shared smoke-test runner injects base URL and credentials through the same
# environment variables the generated client reads in normal use.
client = SuperMarketAPI(max_retries=2, timeout=10)


class SmokeResult(TypedDict, total=False):
    operation: str
    method: str
    path: str
    label: str
    status: str
    durationMs: int
    error: str


class _SmokeCaseBase(TypedDict):
    operation: str
    method: str
    path: str
    run: Callable[[], Any]


# `label` says which of an operation's two calls this is — "required params" or "all params".
# It sits in a total=False extension because it is absent when the operation contributed a
# single case, while the fields above are always present.
class SmokeCase(_SmokeCaseBase, total=False):
    label: str


def _smoke_case_0() -> None:
    market = client.markets.list(
        limit=20,
        sort="recent",
        status="any",
    )


def _smoke_case_1() -> None:
    market = client.markets.list(
        limit=20,
        cursor="cursor",
        tournament_id="550e8400-e29b-41d4-a716-446655440000",
        search="unemployment",
        sort="recent",
        status="any",
        category="economic-indicator",
        ids="1,2,3",
        is_composite="true",
        is_multi_outcome="true",
    )


def _smoke_case_2() -> None:
    market = client.markets.create(
        market_submission={
            "title": "Will it rain tomorrow in NYC?",
            "root_node": {"node_type": "contract", "position": 0},
        },
    )


def _smoke_case_3() -> None:
    market = client.markets.create(
        market_submission={
            "title": "Will it rain tomorrow in NYC?",
            "is_anonymous": False,
            "root_node": {"node_type": "contract", "position": 0},
        },
        custom_thumbnail_url="https://example.com",
        generate_video=False,
        liquidity_amount=0,
        super_signal=False,
        is_signal_anonymous=False,
        tournament_id="",
        tournament_initial_price=0.65,
        global_tournament_id="",
        make_tournament_only=False,
        preserve_submitted_title=False,
        latest_price="0.65",
        latest_prices="0.45,0.35,0.20",
    )


def _smoke_case_4() -> None:
    market = client.markets.retrieve(
        id="26",
    )


def _smoke_case_5() -> None:
    market = client.markets.retrieve(
        id="26",
        tournament_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_6() -> None:
    market = client.markets.update(
        id="26",
        thumbnail_url="https://r2.thesuper.market/market-thumbnails/platform/123e4567-e89b-12d3-a456-426614174000.webp",
    )


def _smoke_case_7() -> None:
    market = client.markets.list_orderbook(
        id="26",
    )


def _smoke_case_8() -> None:
    market = client.markets.list_orderbook(
        id="26",
        tournament_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        depth=20,
    )


def _smoke_case_9() -> None:
    market = client.markets.list_nodes(
        id="26",
    )


def _smoke_case_10() -> None:
    market = client.markets.list_nodes(
        id="26",
        tournament_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_11() -> None:
    exchange = client.exchanges.list(
        limit=50,
    )


def _smoke_case_12() -> None:
    exchange = client.exchanges.list(
        market_id="26",
        ids="36,37,42",
        limit=50,
        cursor="cursor",
        tournament_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_13() -> None:
    exchange = client.exchanges.list_price(
        id="36",
    )


def _smoke_case_14() -> None:
    exchange = client.exchanges.list_price(
        id="36",
        tournament_id="550e8400-e29b-41d4-a716-446655440000",
    )


def _smoke_case_15() -> None:
    exchange = client.exchanges.list_orderbook(
        id="36",
        depth=20,
    )


def _smoke_case_16() -> None:
    exchange = client.exchanges.list_orderbook(
        id="36",
        depth=20,
        tournament_id="550e8400-e29b-41d4-a716-446655440000",
    )


def _smoke_case_17() -> None:
    exchange = client.exchanges.list_price_history(
        id="36",
        resolution="1h",
        limit=200,
    )


def _smoke_case_18() -> None:
    exchange = client.exchanges.list_price_history(
        id="36",
        tournament_id="550e8400-e29b-41d4-a716-446655440000",
        resolution="1h",
        from_="2025-01-01T00:00:00.000Z",
        to="2026-01-01T00:00:00.000Z",
        limit=200,
    )


def _smoke_case_19() -> None:
    exchange = client.exchanges.list_trades(
        id="36",
        limit=50,
    )


def _smoke_case_20() -> None:
    exchange = client.exchanges.list_trades(
        id="36",
        tournament_id="550e8400-e29b-41d4-a716-446655440000",
        from_="2026-01-01T00:00:00.000Z",
        to="2026-04-04T00:00:00.000Z",
        limit=50,
        cursor="cursor",
    )


def _smoke_case_21() -> None:
    exchange = client.exchanges.list_prices(
        ids="36,37,42",
    )


def _smoke_case_22() -> None:
    exchange = client.exchanges.list_prices(
        ids="36,37,42",
        tournament_id="550e8400-e29b-41d4-a716-446655440000",
    )


def _smoke_case_23() -> None:
    order = client.orders.create(
        exchange_id="36",
        side="yes",
        action="buy",
        quantity=100,
        idempotency_key="order-placement-2026-07-23-001",
    )


def _smoke_case_24() -> None:
    order = client.orders.create(
        exchange_id="36",
        side="yes",
        action="buy",
        quantity=100,
        price=0.42,
        expiration_date="2026-07-13T12:00:00.000Z",
        tournament_id="550e8400-e29b-41d4-a716-446655440000",
        idempotency_key="order-placement-2026-07-23-001",
    )


def _smoke_case_25() -> None:
    order = client.orders.list(
        status="open",
        limit=50,
    )


def _smoke_case_26() -> None:
    order = client.orders.list(
        status="open",
        exchange_id="36",
        market_id="26",
        limit=50,
        cursor="cursor",
        tournament_id="550e8400-e29b-41d4-a716-446655440000",
    )


def _smoke_case_27() -> None:
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


def _smoke_case_28() -> None:
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


def _smoke_case_29() -> None:
    order = client.orders.retrieve(
        id="1001",
    )


def _smoke_case_30() -> None:
    order = client.orders.delete(
        id="1001",
    )


def _smoke_case_31() -> None:
    order = client.orders.create_cancel_all(
        exchange_id="36",
    )


def _smoke_case_32() -> None:
    order = client.orders.create_cancel_all(
        exchange_id="36",
        market_id="",
        tournament_id="550e8400-e29b-41d4-a716-446655440000",
    )


def _smoke_case_33() -> None:
    order = client.orders.list_fills(
        id="1001",
        limit=50,
    )


def _smoke_case_34() -> None:
    order = client.orders.list_fills(
        id="1001",
        limit=50,
        cursor="cursor",
    )


def _smoke_case_35() -> None:
    portfolio = client.portfolio.list_collateral()


def _smoke_case_36() -> None:
    portfolio = client.portfolio.list_collateral(
        tournament_id="550e8400-e29b-41d4-a716-446655440000",
    )


def _smoke_case_37() -> None:
    portfolio = client.portfolio.list_positions()


def _smoke_case_38() -> None:
    portfolio = client.portfolio.list_pnl(
        period="quarter",
    )


def _smoke_case_39() -> None:
    portfolio = client.portfolio.list_history(
        interval="1d",
    )


def _smoke_case_40() -> None:
    portfolio = client.portfolio.list_history(
        interval="1d",
        from_="2025-01-01T00:00:00.000Z",
        to="2026-04-04T00:00:00.000Z",
    )


def _smoke_case_41() -> None:
    portfolio = client.portfolio.list_transactions(
        limit=50,
    )


def _smoke_case_42() -> None:
    portfolio = client.portfolio.list_transactions(
        limit=50,
        cursor="cursor",
        type="trade,settlement",
    )


def _smoke_case_43() -> None:
    portfolio = client.portfolio.list_settlements(
        limit=50,
    )


def _smoke_case_44() -> None:
    portfolio = client.portfolio.list_settlements(
        limit=50,
        cursor="cursor",
        type="win,loss",
        market_id="26",
    )


def _smoke_case_45() -> None:
    portfolio = client.portfolio.list_fills(
        limit=50,
    )


def _smoke_case_46() -> None:
    portfolio = client.portfolio.list_fills(
        exchange_id="36",
        market_id="26",
        limit=50,
        cursor="cursor",
        tournament_id="550e8400-e29b-41d4-a716-446655440000",
    )


def _smoke_case_47() -> None:
    account = client.account.list()


def _smoke_case_48() -> None:
    tournament = client.tournaments.list(
        status="any",
        limit=50,
        offset=0,
    )


def _smoke_case_49() -> None:
    tournament = client.tournaments.list(
        status="any",
        limit=50,
        offset=0,
        market_id=26,
    )


def _smoke_case_50() -> None:
    tournament = client.tournaments.retrieve(
        slug="alpha-tournament",
    )


def _smoke_case_51() -> None:
    tournament = client.tournaments.list_leaderboard(
        slug="alpha-tournament",
        period="all",
        limit=50,
        offset=0,
        sort="pnl",
    )


def _smoke_case_52() -> None:
    tournament = client.tournaments.list_leaderboard(
        slug="alpha-tournament",
        period="all",
        limit=50,
        offset=0,
        group_id="00000000-0000-0000-0000-000000000010",
        season="2026-Q1",
        sort="pnl",
    )


def _smoke_case_53() -> None:
    tournament = client.tournaments.list_seasons(
        slug="alpha-tournament",
    )


def _smoke_case_54() -> None:
    market = client.tournaments.markets.list(
        slug="alpha-tournament",
        limit=20,
        status="any",
    )


def _smoke_case_55() -> None:
    market = client.tournaments.markets.list(
        slug="alpha-tournament",
        limit=20,
        cursor="cursor",
        search="unemployment",
        status="any",
        market_group_id="00000000-0000-0000-0000-000000000010",
    )


def _smoke_case_56() -> None:
    market = client.tournaments.markets.retrieve(
        slug="alpha-tournament",
        id="26",
    )


def _smoke_case_57() -> None:
    portfolio = client.tournaments.portfolio.list_positions(
        slug="alpha-tournament",
    )


def _smoke_case_58() -> None:
    portfolio = client.tournaments.portfolio.list_transactions(
        slug="alpha-tournament",
        limit=50,
    )


def _smoke_case_59() -> None:
    portfolio = client.tournaments.portfolio.list_transactions(
        slug="alpha-tournament",
        limit=50,
        cursor="cursor",
        type="trade,settlement",
    )


def _smoke_case_60() -> None:
    portfolio = client.tournaments.portfolio.list_fills(
        slug="alpha-tournament",
        limit=50,
    )


def _smoke_case_61() -> None:
    portfolio = client.tournaments.portfolio.list_fills(
        slug="alpha-tournament",
        exchange_id="36",
        market_id="26",
        limit=50,
        cursor="cursor",
    )


def _smoke_case_62() -> None:
    portfolio = client.tournaments.portfolio.list_history(
        slug="alpha-tournament",
        interval="1d",
    )


def _smoke_case_63() -> None:
    portfolio = client.tournaments.portfolio.list_history(
        slug="alpha-tournament",
        interval="1d",
        from_="2025-01-01T00:00:00.000Z",
        to="2026-04-04T00:00:00.000Z",
    )


def _smoke_case_64() -> None:
    portfolio = client.tournaments.portfolio.list_settlements(
        slug="alpha-tournament",
        limit=50,
    )


def _smoke_case_65() -> None:
    portfolio = client.tournaments.portfolio.list_settlements(
        slug="alpha-tournament",
        limit=50,
        cursor="cursor",
        type="win,loss",
        market_id="26",
    )


def _smoke_case_66() -> None:
    portfolio = client.tournaments.portfolio.list_pnl(
        slug="alpha-tournament",
        period="quarter",
    )


def _smoke_case_67() -> None:
    me = client.tournaments.me.list_smart_score(
        slug="alpha-tournament",
    )


def _smoke_case_68() -> None:
    leaderboard = client.leaderboards.list(
        period="all",
        limit=50,
        offset=0,
    )


def _smoke_case_69() -> None:
    leaderboard = client.leaderboards.list(
        tournament_slug="alpha-tournament",
        group_id="00000000-0000-0000-0000-000000000010",
        period="all",
        sort="pnl",
        limit=50,
        offset=0,
    )


def _smoke_case_70() -> None:
    dmm = client.dmm.list_failed_autosettlement()


def _smoke_case_71() -> None:
    dmm = client.dmm.list_failed_autosettlement(
        limit=50,
        offset=0,
    )


def _smoke_case_72() -> None:
    dmm = client.dmm.list_rankings()


def _smoke_case_73() -> None:
    dmm = client.dmm.list_rankings(
        organization_slug="acme-corp",
        market_type="global",
        sort_by="smartScore",
        order="desc",
        limit=50,
        offset=0,
        user_group_id="550e8400-e29b-41d4-a716-446655440000",
        market_group_id="550e8400-e29b-41d4-a716-446655440000",
        period="all",
    )


def _smoke_case_74() -> None:
    tournament = client.dmm.tournaments.list()


def _smoke_case_75() -> None:
    tournament = client.dmm.tournaments.list(
        organization_slug="acme-corp",
        archived="active",
        limit=50,
        cursor="cursor",
    )


def _smoke_case_76() -> None:
    tournament = client.dmm.tournaments.create(
        name="Alpha Tournament",
        end_date="2026-07-01T00:00:00.000Z",
        organization_slug="acme-corp",
    )


def _smoke_case_77() -> None:
    tournament = client.dmm.tournaments.create(
        name="Alpha Tournament",
        description="Internal trading competition.",
        start_date="2026-06-01T00:00:00.000Z",
        end_date="2026-07-01T00:00:00.000Z",
        initial_virtual_balance=1000,
        auto_enroll_on_signup=False,
        currency_name="Coins",
        organization_slug="acme-corp",
        mode="p2p",
        visibility="private",
        logo_url="https://cdn.example.com/logo.png",
        banner_url="https://cdn.example.com/banner.png",
        market_group_ids=["550e8400-e29b-41d4-a716-446655440000"],
        user_group_ids=["550e8400-e29b-41d4-a716-446655440000"],
    )


def _smoke_case_78() -> None:
    tournament = client.dmm.tournaments.update(
        slug="alpha-tournament",
    )


def _smoke_case_79() -> None:
    tournament = client.dmm.tournaments.update(
        slug="alpha-tournament",
        name="Alpha Tournament",
        description="Internal trading competition.",
        start_date="2026-06-01T00:00:00.000Z",
        initial_virtual_balance=1000,
        auto_enroll_on_signup=False,
        currency_name="Coins",
        visibility="private",
        logo_url="https://cdn.example.com/logo.png",
        banner_url="https://cdn.example.com/banner.png",
        end_date="2026-07-15T00:00:00.000Z",
    )


def _smoke_case_80() -> None:
    client.dmm.tournaments.delete(
        slug="alpha-tournament",
    )


def _smoke_case_81() -> None:
    tournament = client.dmm.tournaments.create_reset_balances(
        slug="alpha-tournament",
        confirm="alpha-tournament",
        reset_key="quarterly-reset-2026-q3",
    )


def _smoke_case_82() -> None:
    tournament = client.dmm.tournaments.list_rankings(
        slug="alpha-tournament",
    )


def _smoke_case_83() -> None:
    tournament = client.dmm.tournaments.list_rankings(
        slug="alpha-tournament",
        market_type="global",
        sort_by="smartScore",
        order="desc",
        limit=50,
        offset=0,
        user_group_id="550e8400-e29b-41d4-a716-446655440000",
        market_group_id="550e8400-e29b-41d4-a716-446655440000",
        period="all",
    )


def _smoke_case_84() -> None:
    tournament = client.dmm.tournaments.list_market_assignments(
        slug="alpha-tournament",
    )


def _smoke_case_85() -> None:
    tournament = client.dmm.tournaments.list_market_assignments(
        slug="alpha-tournament",
        limit=50,
        cursor="cursor",
    )


def _smoke_case_86() -> None:
    designated_market_maker_trades = client.dmm.tournaments.list_trades(
        slug="alpha-tournament",
    )


def _smoke_case_87() -> None:
    designated_market_maker_trades = client.dmm.tournaments.list_trades(
        slug="alpha-tournament",
        from_="2026-06-01T00:00:00.000Z",
        to="2026-07-01T00:00:00.000Z",
        limit=50,
        cursor="cursor",
    )


def _smoke_case_88() -> None:
    designated_market_maker_orders = client.dmm.tournaments.list_orders(
        slug="alpha-tournament",
    )


def _smoke_case_89() -> None:
    designated_market_maker_orders = client.dmm.tournaments.list_orders(
        slug="alpha-tournament",
        from_="2026-06-01T00:00:00.000Z",
        to="2026-07-01T00:00:00.000Z",
        limit=50,
        cursor="cursor",
    )


def _smoke_case_90() -> None:
    designated_market_maker_transactions = client.dmm.tournaments.list_transactions(
        slug="alpha-tournament",
    )


def _smoke_case_91() -> None:
    designated_market_maker_transactions = client.dmm.tournaments.list_transactions(
        slug="alpha-tournament",
        from_="2026-06-01T00:00:00.000Z",
        to="2026-07-01T00:00:00.000Z",
        limit=50,
        cursor="cursor",
    )


def _smoke_case_92() -> None:
    tournament = client.dmm.tournaments.list_inventory(
        slug="alpha-tournament",
    )


def _smoke_case_93() -> None:
    tournament = client.dmm.tournaments.list_inventory(
        slug="alpha-tournament",
        market="3",
    )


def _smoke_case_94() -> None:
    end_settlement = client.dmm.tournaments.end_settlement.list(
        slug="alpha-tournament",
    )


def _smoke_case_95() -> None:
    end_settlement = client.dmm.tournaments.end_settlement.create(
        slug="alpha-tournament",
    )


def _smoke_case_96() -> None:
    end_settlement = client.dmm.tournaments.end_settlement.create(
        slug="alpha-tournament",
        submitted_prices=[{"exchangeId": "1234", "price": 0}, {"exchangeId": "1235", "price": 1}],
    )


def _smoke_case_97() -> None:
    end_settlement = client.dmm.tournaments.end_settlement.list_status(
        slug="alpha-tournament",
    )


def _smoke_case_98() -> None:
    settlement_override = client.dmm.tournaments.settlement_overrides.create_preview(
        slug="alpha-tournament",
        reason="Corrected official final valuation from settlement desk review.",
        overrides=[{"exchange_id": "1234", "price": 0.75}],
    )


def _smoke_case_99() -> None:
    settlement_override = client.dmm.tournaments.settlement_overrides.create(
        slug="alpha-tournament",
        reason="Corrected official final valuation from settlement desk review.",
        overrides=[{"exchange_id": "1234", "price": 0.75}],
    )


def _smoke_case_100() -> None:
    market = client.dmm.tournaments.markets.list(
        slug="alpha-tournament",
    )


def _smoke_case_101() -> None:
    market = client.dmm.tournaments.markets.list(
        slug="alpha-tournament",
        limit=50,
        cursor="cursor",
    )


def _smoke_case_102() -> None:
    market = client.dmm.tournaments.markets.create(
        slug="alpha-tournament",
        market_id="26",
    )


def _smoke_case_103() -> None:
    market = client.dmm.tournaments.markets.delete(
        slug="slug",
        market_id="marketId",
    )


def _smoke_case_104() -> None:
    member = client.dmm.tournaments.members.list(
        slug="alpha-tournament",
    )


def _smoke_case_105() -> None:
    member = client.dmm.tournaments.members.create(
        slug="alpha-tournament",
    )


def _smoke_case_106() -> None:
    member = client.dmm.tournaments.members.create(
        slug="alpha-tournament",
        username="",
        email="user@example.com",
    )


def _smoke_case_107() -> None:
    member = client.dmm.tournaments.members.delete(
        slug="slug",
        profile_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_108() -> None:
    market_group = client.dmm.tournaments.market_groups.list(
        slug="alpha-tournament",
    )


def _smoke_case_109() -> None:
    market_group = client.dmm.tournaments.market_groups.list(
        slug="alpha-tournament",
        limit=50,
        cursor="cursor",
    )


def _smoke_case_110() -> None:
    market_group = client.dmm.tournaments.market_groups.create(
        slug="alpha-tournament",
        market_group_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_111() -> None:
    market_group = client.dmm.tournaments.market_groups.delete(
        slug="slug",
        group_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_112() -> None:
    user_group = client.dmm.tournaments.user_groups.list(
        slug="alpha-tournament",
    )


def _smoke_case_113() -> None:
    user_group = client.dmm.tournaments.user_groups.list(
        slug="alpha-tournament",
        limit=50,
        cursor="cursor",
    )


def _smoke_case_114() -> None:
    user_group = client.dmm.tournaments.user_groups.create(
        slug="alpha-tournament",
        user_group_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_115() -> None:
    user_group = client.dmm.tournaments.user_groups.delete(
        slug="slug",
        group_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_116() -> None:
    exchange = client.dmm.tournaments.exchanges.create_liquidity(
        slug="alpha-tournament",
        exchange_id="36",
        mode="append",
        operation_key="jerry-liquidity-2026-07-15-001",
    )


def _smoke_case_117() -> None:
    exchange = client.dmm.tournaments.exchanges.create_liquidity(
        slug="alpha-tournament",
        exchange_id="36",
        mode="append",
        operation_key="jerry-liquidity-2026-07-15-001",
        bids=[{"price": 0.48, "quantity": 100}],
        asks=[{"price": 0.48, "quantity": 100}],
    )


def _smoke_case_118() -> None:
    exchange = client.dmm.tournaments.exchanges.delete_liquidity(
        slug="alpha-tournament",
        exchange_id="36",
    )


def _smoke_case_119() -> None:
    exchange = client.dmm.tournaments.exchanges.delete_liquidity(
        slug="alpha-tournament",
        exchange_id="36",
        idempotency_key="jerry-sweep-2026-09-23-001",
    )


def _smoke_case_120() -> None:
    relationship = client.dmm.relationships.create(
        type="Implication",
        antecedent={"market_id": "26", "exchange_id": "36"},
        consequent={"market_id": "26", "exchange_id": "36"},
    )


def _smoke_case_121() -> None:
    relationship = client.dmm.relationships.create(
        organization_slug="sig",
        label="",
        reason="",
        idempotency_key="relationship-create-2026-08-04-001",
        type="Implication",
        antecedent={"market_id": "26", "exchange_id": "36"},
        consequent={"market_id": "26", "exchange_id": "36"},
    )


def _smoke_case_122() -> None:
    relationship = client.dmm.relationships.delete(
        relationship_id="550e8400-e29b-41d4-a716-446655440000",
    )


def _smoke_case_123() -> None:
    relationship = client.dmm.relationships.delete(
        relationship_id="550e8400-e29b-41d4-a716-446655440000",
        idempotency_key="relationship-disable-2026-08-04-001",
    )


def _smoke_case_124() -> None:
    relationship = client.dmm.relationships.retrieve_operations(
        operation_id="550e8400-e29b-41d4-a716-446655440000",
    )


def _smoke_case_125() -> None:
    relationship = client.dmm.relationships.create_reconcile()


def _smoke_case_126() -> None:
    relationship = client.dmm.relationships.create_reconcile(
        organization_slug="x",
    )


def _smoke_case_127() -> None:
    icim = client.dmm.icims.list_export()


def _smoke_case_128() -> None:
    icim = client.dmm.icims.list_export(
        organization_slug="acme-corp",
    )


def _smoke_case_129() -> None:
    trader_analytic = client.dmm.trader_analytics.list_elite_summary()


def _smoke_case_130() -> None:
    trader_analytic = client.dmm.trader_analytics.list_elite_summary(
        tournament_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        market_type="global",
        organization_slug="organization_slug",
    )


def _smoke_case_131() -> None:
    dmm_trader_analytics_users = client.dmm.trader_analytics.users.list()


def _smoke_case_132() -> None:
    dmm_trader_analytics_users = client.dmm.trader_analytics.users.list(
        tournament_id="550e8400-e29b-41d4-a716-446655440000",
        group_id="550e8400-e29b-41d4-a716-446655440000",
        market_group_id="550e8400-e29b-41d4-a716-446655440000",
        market_type="global",
        period="month",
        period_start="2026-04-01T00:00:00.000Z",
        period_end="2026-05-01T00:00:00.000Z",
        min_smart_score=70,
        min_trades=50,
        elite_only="false",
        sort="smart_score_desc",
        limit=50,
        cursor="cursor",
        organization_slug="organization_slug",
    )


def _smoke_case_133() -> None:
    user = client.dmm.trader_analytics.users.retrieve(
        profile_id="550e8400-e29b-41d4-a716-446655440000",
    )


def _smoke_case_134() -> None:
    user = client.dmm.trader_analytics.users.retrieve(
        profile_id="550e8400-e29b-41d4-a716-446655440000",
        tournament_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        market_group_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        market_type="market_type",
        period="month",
        period_start="2026-04-01T00:00:00.000Z",
        period_end="2026-05-01T00:00:00.000Z",
        include_history="true",
        organization_slug="organization_slug",
    )


def _smoke_case_135() -> None:
    market = client.dmm.groups.markets.list(
        limit=25,
    )


def _smoke_case_136() -> None:
    market = client.dmm.groups.markets.list(
        limit=25,
        cursor="cursor",
        search="search",
        organization_slug="organization_slug",
    )


def _smoke_case_137() -> None:
    market = client.dmm.groups.markets.create(
        name="Earnings Markets",
    )


def _smoke_case_138() -> None:
    market = client.dmm.groups.markets.create(
        name="Earnings Markets",
        slug="earnings-markets",
        description="",
        organization_slug="x",
    )


def _smoke_case_139() -> None:
    market = client.dmm.groups.markets.retrieve(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_140() -> None:
    market = client.dmm.groups.markets.update(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_141() -> None:
    market = client.dmm.groups.markets.update(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
        slug="",
        description="",
    )


def _smoke_case_142() -> None:
    market = client.dmm.groups.markets.delete(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_143() -> None:
    market = client.dmm.groups.markets.list_members(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=25,
    )


def _smoke_case_144() -> None:
    market = client.dmm.groups.markets.list_members(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=25,
        cursor="cursor",
    )


def _smoke_case_145() -> None:
    market = client.dmm.groups.markets.create_members(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        market_ids=["1042", "1043"],
    )


def _smoke_case_146() -> None:
    market = client.dmm.groups.markets.delete_members(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        market_ids=["1042", "1043"],
    )


def _smoke_case_147() -> None:
    user = client.dmm.groups.users.list(
        limit=25,
    )


def _smoke_case_148() -> None:
    user = client.dmm.groups.users.list(
        limit=25,
        cursor="cursor",
        search="search",
        organization_slug="organization_slug",
    )


def _smoke_case_149() -> None:
    user = client.dmm.groups.users.create(
        name="Earnings Markets",
    )


def _smoke_case_150() -> None:
    user = client.dmm.groups.users.create(
        name="Earnings Markets",
        slug="earnings-markets",
        description="",
        organization_slug="x",
    )


def _smoke_case_151() -> None:
    user = client.dmm.groups.users.retrieve(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_152() -> None:
    user = client.dmm.groups.users.update(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_153() -> None:
    user = client.dmm.groups.users.update(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
        slug="",
        description="",
    )


def _smoke_case_154() -> None:
    user = client.dmm.groups.users.delete(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_155() -> None:
    user = client.dmm.groups.users.list_members(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=25,
    )


def _smoke_case_156() -> None:
    user = client.dmm.groups.users.list_members(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=25,
        cursor="cursor",
    )


def _smoke_case_157() -> None:
    user = client.dmm.groups.users.create_members(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_158() -> None:
    user = client.dmm.groups.users.create_members(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        profile_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
        identifiers=["jsmith@example.com", "adoe"],
    )


def _smoke_case_159() -> None:
    user = client.dmm.groups.users.delete_members(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        profile_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
    )


def _smoke_case_160() -> None:
    realtime = client.realtime.create_token()


def _smoke_case_161() -> None:
    relationships_all = client.relationships_all.list_relationships(
        depth=1,
        limit=100,
    )


def _smoke_case_162() -> None:
    relationships_all = client.relationships_all.list_relationships(
        market_id="36",
        exchange_id="36",
        type="monotonic",
        depth=1,
        limit=100,
        cursor="cursor",
        tournament_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_163() -> None:
    relationships_all = client.relationships_all.list_graph(
        market_id="36",
        depth=2,
    )


def _smoke_case_164() -> None:
    relationships_all = client.relationships_all.list_graph(
        market_id="36",
        depth=2,
        tournament_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_165() -> None:
    relationships_all = client.relationships_all.list_constraints(
        violations_only="false",
        min_violation=0.01,
    )


def _smoke_case_166() -> None:
    relationships_all = client.relationships_all.list_constraints(
        market_id="36",
        relationship_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        violations_only="false",
        min_violation=0.01,
        tournament_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


cases: list[SmokeCase] = [
    {
        "operation": "list",
        "method": "GET",
        "path": "/markets",
        "label": "required params",
        "run": _smoke_case_0,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/markets",
        "label": "all params",
        "run": _smoke_case_1,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/markets",
        "label": "required params",
        "run": _smoke_case_2,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/markets",
        "label": "all params",
        "run": _smoke_case_3,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/markets/{id}",
        "label": "required params",
        "run": _smoke_case_4,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/markets/{id}",
        "label": "all params",
        "run": _smoke_case_5,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/markets/{id}",
        "run": _smoke_case_6,
    },
    {
        "operation": "listOrderbook",
        "method": "GET",
        "path": "/markets/{id}/orderbook",
        "label": "required params",
        "run": _smoke_case_7,
    },
    {
        "operation": "listOrderbook",
        "method": "GET",
        "path": "/markets/{id}/orderbook",
        "label": "all params",
        "run": _smoke_case_8,
    },
    {
        "operation": "listNodes",
        "method": "GET",
        "path": "/markets/{id}/nodes",
        "label": "required params",
        "run": _smoke_case_9,
    },
    {
        "operation": "listNodes",
        "method": "GET",
        "path": "/markets/{id}/nodes",
        "label": "all params",
        "run": _smoke_case_10,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/exchanges",
        "label": "required params",
        "run": _smoke_case_11,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/exchanges",
        "label": "all params",
        "run": _smoke_case_12,
    },
    {
        "operation": "listPrice",
        "method": "GET",
        "path": "/exchanges/{id}/price",
        "label": "required params",
        "run": _smoke_case_13,
    },
    {
        "operation": "listPrice",
        "method": "GET",
        "path": "/exchanges/{id}/price",
        "label": "all params",
        "run": _smoke_case_14,
    },
    {
        "operation": "listOrderbook",
        "method": "GET",
        "path": "/exchanges/{id}/orderbook",
        "label": "required params",
        "run": _smoke_case_15,
    },
    {
        "operation": "listOrderbook",
        "method": "GET",
        "path": "/exchanges/{id}/orderbook",
        "label": "all params",
        "run": _smoke_case_16,
    },
    {
        "operation": "listPriceHistory",
        "method": "GET",
        "path": "/exchanges/{id}/price-history",
        "label": "required params",
        "run": _smoke_case_17,
    },
    {
        "operation": "listPriceHistory",
        "method": "GET",
        "path": "/exchanges/{id}/price-history",
        "label": "all params",
        "run": _smoke_case_18,
    },
    {
        "operation": "listTrades",
        "method": "GET",
        "path": "/exchanges/{id}/trades",
        "label": "required params",
        "run": _smoke_case_19,
    },
    {
        "operation": "listTrades",
        "method": "GET",
        "path": "/exchanges/{id}/trades",
        "label": "all params",
        "run": _smoke_case_20,
    },
    {
        "operation": "listPrices",
        "method": "GET",
        "path": "/exchanges/prices",
        "label": "required params",
        "run": _smoke_case_21,
    },
    {
        "operation": "listPrices",
        "method": "GET",
        "path": "/exchanges/prices",
        "label": "all params",
        "run": _smoke_case_22,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/orders",
        "label": "required params",
        "run": _smoke_case_23,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/orders",
        "label": "all params",
        "run": _smoke_case_24,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/orders",
        "label": "required params",
        "run": _smoke_case_25,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/orders",
        "label": "all params",
        "run": _smoke_case_26,
    },
    {
        "operation": "createBatch",
        "method": "POST",
        "path": "/orders/batch",
        "run": _smoke_case_27,
    },
    {
        "operation": "createMultiLeg",
        "method": "POST",
        "path": "/orders/multi-leg",
        "run": _smoke_case_28,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/orders/{id}",
        "run": _smoke_case_29,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/orders/{id}",
        "run": _smoke_case_30,
    },
    {
        "operation": "createCancelAll",
        "method": "POST",
        "path": "/orders/cancel-all",
        "label": "required params",
        "run": _smoke_case_31,
    },
    {
        "operation": "createCancelAll",
        "method": "POST",
        "path": "/orders/cancel-all",
        "label": "all params",
        "run": _smoke_case_32,
    },
    {
        "operation": "listFills",
        "method": "GET",
        "path": "/orders/{id}/fills",
        "label": "required params",
        "run": _smoke_case_33,
    },
    {
        "operation": "listFills",
        "method": "GET",
        "path": "/orders/{id}/fills",
        "label": "all params",
        "run": _smoke_case_34,
    },
    {
        "operation": "listCollateral",
        "method": "GET",
        "path": "/portfolio/collateral",
        "label": "required params",
        "run": _smoke_case_35,
    },
    {
        "operation": "listCollateral",
        "method": "GET",
        "path": "/portfolio/collateral",
        "label": "all params",
        "run": _smoke_case_36,
    },
    {
        "operation": "listPositions",
        "method": "GET",
        "path": "/portfolio/positions",
        "run": _smoke_case_37,
    },
    {
        "operation": "listPnl",
        "method": "GET",
        "path": "/portfolio/pnl",
        "run": _smoke_case_38,
    },
    {
        "operation": "listHistory",
        "method": "GET",
        "path": "/portfolio/history",
        "label": "required params",
        "run": _smoke_case_39,
    },
    {
        "operation": "listHistory",
        "method": "GET",
        "path": "/portfolio/history",
        "label": "all params",
        "run": _smoke_case_40,
    },
    {
        "operation": "listTransactions",
        "method": "GET",
        "path": "/portfolio/transactions",
        "label": "required params",
        "run": _smoke_case_41,
    },
    {
        "operation": "listTransactions",
        "method": "GET",
        "path": "/portfolio/transactions",
        "label": "all params",
        "run": _smoke_case_42,
    },
    {
        "operation": "listSettlements",
        "method": "GET",
        "path": "/portfolio/settlements",
        "label": "required params",
        "run": _smoke_case_43,
    },
    {
        "operation": "listSettlements",
        "method": "GET",
        "path": "/portfolio/settlements",
        "label": "all params",
        "run": _smoke_case_44,
    },
    {
        "operation": "listFills",
        "method": "GET",
        "path": "/portfolio/fills",
        "label": "required params",
        "run": _smoke_case_45,
    },
    {
        "operation": "listFills",
        "method": "GET",
        "path": "/portfolio/fills",
        "label": "all params",
        "run": _smoke_case_46,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/account",
        "run": _smoke_case_47,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/tournaments",
        "label": "required params",
        "run": _smoke_case_48,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/tournaments",
        "label": "all params",
        "run": _smoke_case_49,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/tournaments/{slug}",
        "run": _smoke_case_50,
    },
    {
        "operation": "listLeaderboard",
        "method": "GET",
        "path": "/tournaments/{slug}/leaderboard",
        "label": "required params",
        "run": _smoke_case_51,
    },
    {
        "operation": "listLeaderboard",
        "method": "GET",
        "path": "/tournaments/{slug}/leaderboard",
        "label": "all params",
        "run": _smoke_case_52,
    },
    {
        "operation": "listSeasons",
        "method": "GET",
        "path": "/tournaments/{slug}/seasons",
        "run": _smoke_case_53,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/tournaments/{slug}/markets",
        "label": "required params",
        "run": _smoke_case_54,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/tournaments/{slug}/markets",
        "label": "all params",
        "run": _smoke_case_55,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/tournaments/{slug}/markets/{id}",
        "run": _smoke_case_56,
    },
    {
        "operation": "listPositions",
        "method": "GET",
        "path": "/tournaments/{slug}/portfolio/positions",
        "run": _smoke_case_57,
    },
    {
        "operation": "listTransactions",
        "method": "GET",
        "path": "/tournaments/{slug}/portfolio/transactions",
        "label": "required params",
        "run": _smoke_case_58,
    },
    {
        "operation": "listTransactions",
        "method": "GET",
        "path": "/tournaments/{slug}/portfolio/transactions",
        "label": "all params",
        "run": _smoke_case_59,
    },
    {
        "operation": "listFills",
        "method": "GET",
        "path": "/tournaments/{slug}/portfolio/fills",
        "label": "required params",
        "run": _smoke_case_60,
    },
    {
        "operation": "listFills",
        "method": "GET",
        "path": "/tournaments/{slug}/portfolio/fills",
        "label": "all params",
        "run": _smoke_case_61,
    },
    {
        "operation": "listHistory",
        "method": "GET",
        "path": "/tournaments/{slug}/portfolio/history",
        "label": "required params",
        "run": _smoke_case_62,
    },
    {
        "operation": "listHistory",
        "method": "GET",
        "path": "/tournaments/{slug}/portfolio/history",
        "label": "all params",
        "run": _smoke_case_63,
    },
    {
        "operation": "listSettlements",
        "method": "GET",
        "path": "/tournaments/{slug}/portfolio/settlements",
        "label": "required params",
        "run": _smoke_case_64,
    },
    {
        "operation": "listSettlements",
        "method": "GET",
        "path": "/tournaments/{slug}/portfolio/settlements",
        "label": "all params",
        "run": _smoke_case_65,
    },
    {
        "operation": "listPnl",
        "method": "GET",
        "path": "/tournaments/{slug}/portfolio/pnl",
        "run": _smoke_case_66,
    },
    {
        "operation": "listSmartScore",
        "method": "GET",
        "path": "/tournaments/{slug}/me/smart-score",
        "run": _smoke_case_67,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/leaderboards",
        "label": "required params",
        "run": _smoke_case_68,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/leaderboards",
        "label": "all params",
        "run": _smoke_case_69,
    },
    {
        "operation": "listFailedAutosettlement",
        "method": "GET",
        "path": "/dmm/failed-autosettlement",
        "label": "required params",
        "run": _smoke_case_70,
    },
    {
        "operation": "listFailedAutosettlement",
        "method": "GET",
        "path": "/dmm/failed-autosettlement",
        "label": "all params",
        "run": _smoke_case_71,
    },
    {
        "operation": "listRankings",
        "method": "GET",
        "path": "/dmm/rankings",
        "label": "required params",
        "run": _smoke_case_72,
    },
    {
        "operation": "listRankings",
        "method": "GET",
        "path": "/dmm/rankings",
        "label": "all params",
        "run": _smoke_case_73,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/dmm/tournaments",
        "label": "required params",
        "run": _smoke_case_74,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/dmm/tournaments",
        "label": "all params",
        "run": _smoke_case_75,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/dmm/tournaments",
        "label": "required params",
        "run": _smoke_case_76,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/dmm/tournaments",
        "label": "all params",
        "run": _smoke_case_77,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/dmm/tournaments/{slug}",
        "label": "required params",
        "run": _smoke_case_78,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/dmm/tournaments/{slug}",
        "label": "all params",
        "run": _smoke_case_79,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/dmm/tournaments/{slug}",
        "run": _smoke_case_80,
    },
    {
        "operation": "createResetBalances",
        "method": "POST",
        "path": "/dmm/tournaments/{slug}/reset-balances",
        "run": _smoke_case_81,
    },
    {
        "operation": "listRankings",
        "method": "GET",
        "path": "/dmm/tournaments/{slug}/rankings",
        "label": "required params",
        "run": _smoke_case_82,
    },
    {
        "operation": "listRankings",
        "method": "GET",
        "path": "/dmm/tournaments/{slug}/rankings",
        "label": "all params",
        "run": _smoke_case_83,
    },
    {
        "operation": "listMarketAssignments",
        "method": "GET",
        "path": "/dmm/tournaments/{slug}/market-assignments",
        "label": "required params",
        "run": _smoke_case_84,
    },
    {
        "operation": "listMarketAssignments",
        "method": "GET",
        "path": "/dmm/tournaments/{slug}/market-assignments",
        "label": "all params",
        "run": _smoke_case_85,
    },
    {
        "operation": "listTrades",
        "method": "GET",
        "path": "/dmm/tournaments/{slug}/trades",
        "label": "required params",
        "run": _smoke_case_86,
    },
    {
        "operation": "listTrades",
        "method": "GET",
        "path": "/dmm/tournaments/{slug}/trades",
        "label": "all params",
        "run": _smoke_case_87,
    },
    {
        "operation": "listOrders",
        "method": "GET",
        "path": "/dmm/tournaments/{slug}/orders",
        "label": "required params",
        "run": _smoke_case_88,
    },
    {
        "operation": "listOrders",
        "method": "GET",
        "path": "/dmm/tournaments/{slug}/orders",
        "label": "all params",
        "run": _smoke_case_89,
    },
    {
        "operation": "listTransactions",
        "method": "GET",
        "path": "/dmm/tournaments/{slug}/transactions",
        "label": "required params",
        "run": _smoke_case_90,
    },
    {
        "operation": "listTransactions",
        "method": "GET",
        "path": "/dmm/tournaments/{slug}/transactions",
        "label": "all params",
        "run": _smoke_case_91,
    },
    {
        "operation": "listInventory",
        "method": "GET",
        "path": "/dmm/tournaments/{slug}/inventory",
        "label": "required params",
        "run": _smoke_case_92,
    },
    {
        "operation": "listInventory",
        "method": "GET",
        "path": "/dmm/tournaments/{slug}/inventory",
        "label": "all params",
        "run": _smoke_case_93,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/dmm/tournaments/{slug}/end-settlement",
        "run": _smoke_case_94,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/dmm/tournaments/{slug}/end-settlement",
        "label": "required params",
        "run": _smoke_case_95,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/dmm/tournaments/{slug}/end-settlement",
        "label": "all params",
        "run": _smoke_case_96,
    },
    {
        "operation": "listStatus",
        "method": "GET",
        "path": "/dmm/tournaments/{slug}/end-settlement/status",
        "run": _smoke_case_97,
    },
    {
        "operation": "createPreview",
        "method": "POST",
        "path": "/dmm/tournaments/{slug}/settlement-overrides/preview",
        "run": _smoke_case_98,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/dmm/tournaments/{slug}/settlement-overrides",
        "run": _smoke_case_99,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/dmm/tournaments/{slug}/markets",
        "label": "required params",
        "run": _smoke_case_100,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/dmm/tournaments/{slug}/markets",
        "label": "all params",
        "run": _smoke_case_101,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/dmm/tournaments/{slug}/markets",
        "run": _smoke_case_102,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/dmm/tournaments/{slug}/markets/{marketId}",
        "run": _smoke_case_103,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/dmm/tournaments/{slug}/members",
        "run": _smoke_case_104,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/dmm/tournaments/{slug}/members",
        "label": "required params",
        "run": _smoke_case_105,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/dmm/tournaments/{slug}/members",
        "label": "all params",
        "run": _smoke_case_106,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/dmm/tournaments/{slug}/members/{profileId}",
        "run": _smoke_case_107,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/dmm/tournaments/{slug}/market-groups",
        "label": "required params",
        "run": _smoke_case_108,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/dmm/tournaments/{slug}/market-groups",
        "label": "all params",
        "run": _smoke_case_109,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/dmm/tournaments/{slug}/market-groups",
        "run": _smoke_case_110,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/dmm/tournaments/{slug}/market-groups/{groupId}",
        "run": _smoke_case_111,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/dmm/tournaments/{slug}/user-groups",
        "label": "required params",
        "run": _smoke_case_112,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/dmm/tournaments/{slug}/user-groups",
        "label": "all params",
        "run": _smoke_case_113,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/dmm/tournaments/{slug}/user-groups",
        "run": _smoke_case_114,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/dmm/tournaments/{slug}/user-groups/{groupId}",
        "run": _smoke_case_115,
    },
    {
        "operation": "createLiquidity",
        "method": "POST",
        "path": "/dmm/tournaments/{slug}/exchanges/{exchangeId}/liquidity",
        "label": "required params",
        "run": _smoke_case_116,
    },
    {
        "operation": "createLiquidity",
        "method": "POST",
        "path": "/dmm/tournaments/{slug}/exchanges/{exchangeId}/liquidity",
        "label": "all params",
        "run": _smoke_case_117,
    },
    {
        "operation": "deleteLiquidity",
        "method": "DELETE",
        "path": "/dmm/tournaments/{slug}/exchanges/{exchangeId}/liquidity",
        "label": "required params",
        "run": _smoke_case_118,
    },
    {
        "operation": "deleteLiquidity",
        "method": "DELETE",
        "path": "/dmm/tournaments/{slug}/exchanges/{exchangeId}/liquidity",
        "label": "all params",
        "run": _smoke_case_119,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/dmm/relationships",
        "label": "required params",
        "run": _smoke_case_120,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/dmm/relationships",
        "label": "all params",
        "run": _smoke_case_121,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/dmm/relationships/{relationshipId}",
        "label": "required params",
        "run": _smoke_case_122,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/dmm/relationships/{relationshipId}",
        "label": "all params",
        "run": _smoke_case_123,
    },
    {
        "operation": "retrieveOperations",
        "method": "GET",
        "path": "/dmm/relationships/operations/{operationId}",
        "run": _smoke_case_124,
    },
    {
        "operation": "createReconcile",
        "method": "POST",
        "path": "/dmm/relationships/reconcile",
        "label": "required params",
        "run": _smoke_case_125,
    },
    {
        "operation": "createReconcile",
        "method": "POST",
        "path": "/dmm/relationships/reconcile",
        "label": "all params",
        "run": _smoke_case_126,
    },
    {
        "operation": "listExport",
        "method": "GET",
        "path": "/dmm/icims/export",
        "label": "required params",
        "run": _smoke_case_127,
    },
    {
        "operation": "listExport",
        "method": "GET",
        "path": "/dmm/icims/export",
        "label": "all params",
        "run": _smoke_case_128,
    },
    {
        "operation": "listEliteSummary",
        "method": "GET",
        "path": "/dmm/trader-analytics/elite-summary",
        "label": "required params",
        "run": _smoke_case_129,
    },
    {
        "operation": "listEliteSummary",
        "method": "GET",
        "path": "/dmm/trader-analytics/elite-summary",
        "label": "all params",
        "run": _smoke_case_130,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/dmm/trader-analytics/users",
        "label": "required params",
        "run": _smoke_case_131,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/dmm/trader-analytics/users",
        "label": "all params",
        "run": _smoke_case_132,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/dmm/trader-analytics/users/{profileId}",
        "label": "required params",
        "run": _smoke_case_133,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/dmm/trader-analytics/users/{profileId}",
        "label": "all params",
        "run": _smoke_case_134,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/dmm/groups/markets",
        "label": "required params",
        "run": _smoke_case_135,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/dmm/groups/markets",
        "label": "all params",
        "run": _smoke_case_136,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/dmm/groups/markets",
        "label": "required params",
        "run": _smoke_case_137,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/dmm/groups/markets",
        "label": "all params",
        "run": _smoke_case_138,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/dmm/groups/markets/{id}",
        "run": _smoke_case_139,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/dmm/groups/markets/{id}",
        "label": "required params",
        "run": _smoke_case_140,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/dmm/groups/markets/{id}",
        "label": "all params",
        "run": _smoke_case_141,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/dmm/groups/markets/{id}",
        "run": _smoke_case_142,
    },
    {
        "operation": "listMembers",
        "method": "GET",
        "path": "/dmm/groups/markets/{id}/members",
        "label": "required params",
        "run": _smoke_case_143,
    },
    {
        "operation": "listMembers",
        "method": "GET",
        "path": "/dmm/groups/markets/{id}/members",
        "label": "all params",
        "run": _smoke_case_144,
    },
    {
        "operation": "createMembers",
        "method": "POST",
        "path": "/dmm/groups/markets/{id}/members",
        "run": _smoke_case_145,
    },
    {
        "operation": "deleteMembers",
        "method": "DELETE",
        "path": "/dmm/groups/markets/{id}/members",
        "run": _smoke_case_146,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/dmm/groups/users",
        "label": "required params",
        "run": _smoke_case_147,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/dmm/groups/users",
        "label": "all params",
        "run": _smoke_case_148,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/dmm/groups/users",
        "label": "required params",
        "run": _smoke_case_149,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/dmm/groups/users",
        "label": "all params",
        "run": _smoke_case_150,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/dmm/groups/users/{id}",
        "run": _smoke_case_151,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/dmm/groups/users/{id}",
        "label": "required params",
        "run": _smoke_case_152,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/dmm/groups/users/{id}",
        "label": "all params",
        "run": _smoke_case_153,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/dmm/groups/users/{id}",
        "run": _smoke_case_154,
    },
    {
        "operation": "listMembers",
        "method": "GET",
        "path": "/dmm/groups/users/{id}/members",
        "label": "required params",
        "run": _smoke_case_155,
    },
    {
        "operation": "listMembers",
        "method": "GET",
        "path": "/dmm/groups/users/{id}/members",
        "label": "all params",
        "run": _smoke_case_156,
    },
    {
        "operation": "createMembers",
        "method": "POST",
        "path": "/dmm/groups/users/{id}/members",
        "label": "required params",
        "run": _smoke_case_157,
    },
    {
        "operation": "createMembers",
        "method": "POST",
        "path": "/dmm/groups/users/{id}/members",
        "label": "all params",
        "run": _smoke_case_158,
    },
    {
        "operation": "deleteMembers",
        "method": "DELETE",
        "path": "/dmm/groups/users/{id}/members",
        "run": _smoke_case_159,
    },
    {
        "operation": "createToken",
        "method": "POST",
        "path": "/realtime/token",
        "run": _smoke_case_160,
    },
    {
        "operation": "listRelationships",
        "method": "GET",
        "path": "/relationships",
        "label": "required params",
        "run": _smoke_case_161,
    },
    {
        "operation": "listRelationships",
        "method": "GET",
        "path": "/relationships",
        "label": "all params",
        "run": _smoke_case_162,
    },
    {
        "operation": "listGraph",
        "method": "GET",
        "path": "/relationships/graph",
        "label": "required params",
        "run": _smoke_case_163,
    },
    {
        "operation": "listGraph",
        "method": "GET",
        "path": "/relationships/graph",
        "label": "all params",
        "run": _smoke_case_164,
    },
    {
        "operation": "listConstraints",
        "method": "GET",
        "path": "/relationships/constraints",
        "label": "required params",
        "run": _smoke_case_165,
    },
    {
        "operation": "listConstraints",
        "method": "GET",
        "path": "/relationships/constraints",
        "label": "all params",
        "run": _smoke_case_166,
    },
]

DEFAULT_SMOKE_CONCURRENCY = 32


def _selected_cases() -> list[SmokeCase]:
    filter_value = os.environ.get("SCALAR_SMOKE_FILTER")
    needles = [needle.strip() for needle in filter_value.split(",") if needle.strip()] if filter_value else []
    if not needles:
        return cases
    return [case for case in cases if any(needle in case["operation"] or needle in case["path"] for needle in needles)]


def _smoke_concurrency(case_count: int) -> int:
    override = os.environ.get("SCALAR_SMOKE_CONCURRENCY")
    if override:
        try:
            parsed = int(override)
            if parsed > 0:
                return min(parsed, case_count)
        except ValueError:
            pass
    return min(DEFAULT_SMOKE_CONCURRENCY, case_count)


def _case_identity(case: SmokeCase) -> SmokeResult:
    # `label` is carried through only when the operation contributed both of its calls, so a
    # single-case operation reports exactly as it did before there were two.
    identity: SmokeResult = {
        "operation": case["operation"],
        "method": case["method"],
        "path": case["path"],
    }
    label = case.get("label")
    if label:
        identity["label"] = label
    return identity


def _run_case(case: SmokeCase) -> SmokeResult:
    started_at = time.monotonic()
    identity = _case_identity(case)
    try:
        case["run"]()
        return {
            **identity,
            "status": "passed",
            "durationMs": int((time.monotonic() - started_at) * 1000),
        }
    except Exception:
        return {
            **identity,
            "status": "failed",
            "durationMs": int((time.monotonic() - started_at) * 1000),
            "error": traceback.format_exc(),
        }


def main() -> None:
    selected = _selected_cases()
    if selected:
        # Keep enough parallelism to catch generated SDK concurrency bugs without overwhelming
        # CI runners or the in-process mock server for large SDKs.
        with ThreadPoolExecutor(max_workers=_smoke_concurrency(len(selected))) as executor:
            results = list(executor.map(_run_case, selected))
    else:
        results = []
    failed = [result for result in results if result["status"] == "failed"]

    report_path = os.environ.get("SCALAR_SMOKE_REPORT")
    if report_path:
        Path(report_path).write_text(
            json.dumps({"total": len(results), "failed": len(failed), "results": results}), encoding="utf-8"
        )
    else:
        for result in results:
            suffix = f" [{result['label']}]" if result.get("label") else ""
            if result["status"] == "passed":
                print(
                    f"PASS {result['operation']}{suffix} ({result['method']} {result['path']}) {result['durationMs']}ms"
                )
            else:
                print(
                    f"FAIL {result['operation']}{suffix} ({result['method']} {result['path']})\n{result.get('error', '')}",
                    file=sys.stderr,
                )
        if not results:
            print("No code samples ran (empty SDK or a SCALAR_SMOKE_FILTER that matched nothing).", file=sys.stderr)
        else:
            print(f"\n{len(results) - len(failed)}/{len(results)} samples passed")

    if failed or not results:
        sys.exit(1)


if __name__ == "__main__":
    main()
