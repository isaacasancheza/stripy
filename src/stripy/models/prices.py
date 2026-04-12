from stripy import constants, fields
from stripy.models.base import BaseModel


class Price(BaseModel):
    """
    https://docs.stripe.com/api/prices/object?lang=python
    """

    id: str
    currency: str
    billing_scheme: constants.PriceBillingScheme

    nickname: str | None = None
    metadata: fields.StripeObject | None = None
    unit_amount: fields.DecimalFromInt | None = None

    created: fields.DatetimeFromTimestamp
    updated: fields.DatetimeFromTimestamp
