from typing import TYPE_CHECKING

from pydantic import BaseModel, HttpUrl

from stripy import stripe_fields

if TYPE_CHECKING:
    from stripy.stripe_models.prices import Price


class Product(BaseModel):
    """
    https://docs.stripe.com/api/prices/object?lang=python
    """

    id: str
    name: str
    active: bool
    currency: str
    livemode: bool

    images: list[HttpUrl] = []
    metadata: stripe_fields.Metadata | None = None
    description: str | None = None
    default_price: 'Price | None' = None

    created: stripe_fields.DatetimeFromTimestamp
    updated: stripe_fields.DatetimeFromTimestamp
