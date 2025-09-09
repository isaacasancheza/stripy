from pydantic import BaseModel

from stripy import fields


class Customer(BaseModel):
    """
    https://docs.stripe.com/api/customers/object?lang=python
    """

    id: str

    name: str | None = None
    email: str | None = None
    phone: str | None = None
    metadata: fields.Metadata | None = None

    created: fields.DatetimeFromTimestamp
