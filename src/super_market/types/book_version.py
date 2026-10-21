# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["BookVersion"]


class BookVersion(BaseModel):
    """The engine version an exchange's book was captured at, the same `asOf` the realtime book push carries. Versions compare by `sequence`, then `at`. Null when the book was read from the database, which has no version."""

    sequence: int
    """The last engine event applied to the book."""

    at: str
    """The engine clock when the book was read."""
