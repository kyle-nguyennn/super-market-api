# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from typing_extensions import TypeAlias

from .tournament_smart_score_entry import TournamentSmartScoreEntry

__all__ = ["MeListSmartScoreResponse"]

MeListSmartScoreResponse: TypeAlias = List[TournamentSmartScoreEntry]
