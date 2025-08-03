from pydantic import BaseModel

from stripy import stripe_constants, stripe_fields
from stripy.stripe_models.products import Product


class Price(BaseModel):
    """
    https://docs.stripe.com/api/prices/object?lang=python
    """

    id: str
    active: bool
    product: 'Product'
    currency: str
    billing_scheme: stripe_constants.PriceBillingScheme

    nickname: str | None = None
    metadata: stripe_fields.Metadata | None = None
    unit_amount: stripe_fields.DecimalFromInt | None = None

    created: stripe_fields.DatetimeFromTimestamp
    updated: stripe_fields.DatetimeFromTimestamp
