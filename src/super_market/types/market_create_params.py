# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, Required, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["MarketCreateParams", "MarketSubmission", "MarketSubmissionRootNode"]


class MarketCreateParams(TypedDict, total=False):
    market_submission: Required[Annotated[MarketSubmission, PropertyInfo(alias="marketSubmission")]]

    custom_thumbnail_url: Annotated[str, PropertyInfo(alias="customThumbnailUrl")]
    """Previously uploaded market-thumbnail URL owned by the API key's organization namespace, or by the platform namespace for an unbound platform key."""

    generate_video: Annotated[bool, PropertyInfo(alias="generateVideo")]
    """Opt-in AI video generation. Free for org-bound API keys; otherwise charges `video_upgrade_fee` from the caller's balance."""

    liquidity_amount: Annotated[float, PropertyInfo(alias="liquidityAmount")]
    """Initial paid liquidity. Values greater than 0 are rejected for org-bound API keys because organization market creation is free."""

    super_signal: Annotated[bool, PropertyInfo(alias="superSignal")]
    """Paid Super Signal promotion. `true` is rejected for org-bound API keys because organization market creation is free."""

    is_signal_anonymous: Annotated[bool, PropertyInfo(alias="isSignalAnonymous")]

    tournament_id: Annotated[str, PropertyInfo(alias="tournamentId")]
    """Attach the market to a private tournament at creation time. Admin-only."""

    tournament_initial_price: Annotated[float, PropertyInfo(alias="tournamentInitialPrice")]
    """Override the seed price for the tournament's isolated order book."""

    global_tournament_id: Annotated[str, PropertyInfo(alias="globalTournamentId")]
    """Enrol the market in a global tournament. Admin-only. Independent of `tournamentId`."""

    make_tournament_only: Annotated[bool, PropertyInfo(alias="makeTournamentOnly")]
    """Hide the market from the global real-money surface. Admin-only. Requires `tournamentId` or `globalTournamentId`."""

    preserve_submitted_title: Annotated[bool, PropertyInfo(alias="preserveSubmittedTitle")]
    """Store `marketSubmission.title` verbatim instead of the server-generated title. Organization-bound API keys only; single-contract markets only."""

    latest_price: Annotated[str, PropertyInfo(alias="latestPrice")]
    """Decimal in (0, 1). Seeds a single price across outcomes."""

    latest_prices: Annotated[str, PropertyInfo(alias="latestPrices")]
    """Comma-separated decimals in (0, 1) — one per settlement option. Multi-outcome custom seeding. Mutually exclusive with `latestPrice`."""


class MarketSubmissionRootNode(TypedDict, total=False):
    node_type: Required[Annotated[Literal["operator", "contract"], PropertyInfo(alias="nodeType")]]

    position: Required[int]

    operator: Literal["AND", "OR", "NOT", "IF"]
    """Required when `nodeType` is `operator`."""

    title: str

    settlement_date: Annotated[Union[str, datetime], PropertyInfo(alias="settlementDate", format="iso8601")]
    """Required for contract nodes except Imported Market. Corporate Earnings may omit it only while needsEarningsDateMonitoring is true and earningsDate is null. When present, must be in the future."""

    contract_type: Annotated[
        Literal[
            "Freeform",
            "Election Outcome",
            "Sports Outcome",
            "Economic Indicator",
            "Financial Product",
            "Corporate Earnings",
            "Imported Market",
            "Existing Market",
        ],
        PropertyInfo(alias="contractType"),
    ]

    contract_details: Annotated[Dict[str, object], PropertyInfo(alias="contractDetails")]
    """Per-`contractType` details. For `Existing Market`, send `contractType: "Existing Market"`, a positive numeric `marketId`, the referenced `marketTitle`, a positive numeric `exchangeId`, and the exchange's exact non-empty `settlementOption`. Selector-less legacy references are accepted only when the referenced market has exactly one exchange. Other contract types have their own server-validated fields."""

    settlement_options: Annotated[SequenceNotStr[str], PropertyInfo(alias="settlementOptions")]

    children: Iterable[MarketSubmissionRootNode]
    """Recursive — each element has the same shape as `MarketNode`. Required for operator nodes."""


class MarketSubmission(TypedDict, total=False):
    title: Required[str]

    is_anonymous: Annotated[bool, PropertyInfo(alias="isAnonymous")]

    root_node: Required[Annotated[MarketSubmissionRootNode, PropertyInfo(alias="rootNode")]]
