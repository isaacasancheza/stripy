from stripy import fields
from stripy.models.base import BaseModel


class Customer(BaseModel):
    """
    https://docs.stripe.com/api/customers/object?lang=python
    """

    id: str

    name: str | None = None
    email: str | None = None
    phone: str | None = None
    metadata: fields.StripeObject | None = None

    created: fields.DatetimeFromTimestamp
