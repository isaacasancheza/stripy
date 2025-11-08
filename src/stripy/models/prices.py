from pydantic import BaseModel

from stripy import constants, fields


class Price(BaseModel):
    """
    https://docs.stripe.com/api/prices/object?lang=python
    """

    id: str
    currency: str
    billing_scheme: constants.PriceBillingScheme

    nickname: str | None = None
    metadata: fields.Metadata | None = None
    unit_amount: fields.DecimalFromInt | None = None

    created: fields.DatetimeFromTimestamp
    updated: fields.DatetimeFromTimestamp
