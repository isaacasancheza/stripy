from typing import TYPE_CHECKING

from stripy import stripe_constants, stripe_fields
from stripy.stripe_models.base import get_models_base_class

if TYPE_CHECKING:
    from stripy.stripe_models.products import Product


class Price(get_models_base_class()):
    """
    https://docs.stripe.com/api/prices/object?lang=python
    """

    id: str
    active: bool
    product: 'Product'
    currency: str
    billing_scheme: stripe_constants.PriceBillingScheme

    nickname: str | None = None
    metadata: stripe_fields.StripeMetadata | None = None
    unit_amount: stripe_fields.StripeDecimalFromInt | None = None

    created: stripe_fields.StripeDatetimeFromTimestamp
    updated: stripe_fields.StripeDatetimeFromTimestamp
