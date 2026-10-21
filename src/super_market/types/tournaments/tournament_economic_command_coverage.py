# File generated from our OpenAPI spec by Scalar. See README.md for details.

from ..._models import BaseModel

__all__ = ["TournamentEconomicCommandCoverage"]


class TournamentEconomicCommandCoverage(BaseModel):
    complete: bool
    """False when the economic-command history walk reached its hard 20-page budget before it found enough matching events or exhausted the log."""
