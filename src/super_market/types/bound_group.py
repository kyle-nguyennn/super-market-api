# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["BoundGroup"]


class BoundGroup(BaseModel):
    id: str

    name: str

    slug: str

    member_count: int
    """Members of the user group who are also members of this tournament."""
