from typing import TYPE_CHECKING

from pydantic import HttpUrl

from stripy import stripe_fields
from stripy.stripe_models.base import get_models_base_class

if TYPE_CHECKING:
    from stripy.stripe_models.prices import Price


class Product(get_models_base_class()):
    """
    https://docs.stripe.com/api/prices/object?lang=python
    """

    id: str
    name: str
    active: bool
    currency: str
    livemode: bool

    images: list[HttpUrl] = []
    metadata: stripe_fields.StripeMetadata | None = None
    description: str | None = None
    default_price: 'Price | None' = None

    created: stripe_fields.StripeDatetimeFromTimestamp
    updated: stripe_fields.StripeDatetimeFromTimestamp
