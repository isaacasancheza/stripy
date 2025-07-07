from pydantic import BaseModel

from stripy import stripe_fields


class Customer(BaseModel):
    """
    https://docs.stripe.com/api/customers/object?lang=python
    """

    id: str

    name: str | None = None
    email: str | None = None
    phone: str | None = None
    metadata: stripe_fields.Metadata | None = None

    created: stripe_fields.DatetimeFromTimestamp
