from pydantic import BaseModel, HttpUrl

from stripy import fields


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
    metadata: fields.Metadata | None = None
    description: str | None = None

    created: fields.DatetimeFromTimestamp
    updated: fields.DatetimeFromTimestamp
