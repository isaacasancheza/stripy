from pydantic import BaseModel

from stripy import constants, fields
from stripy.models.products import Product


class Price(BaseModel):
    """
    https://docs.stripe.com/api/prices/object?lang=python
    """

    id: str
    active: bool
    product: 'Product'
    currency: str
    billing_scheme: constants.PriceBillingScheme

    nickname: str | None = None
    metadata: fields.Metadata | None = None
    unit_amount: fields.DecimalFromInt | None = None

    created: fields.DatetimeFromTimestamp
    updated: fields.DatetimeFromTimestamp
