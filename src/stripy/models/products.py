from pydantic import HttpUrl

from stripy import fields
from stripy.models.base import BaseModel


class Product(BaseModel):
    """
    https://docs.stripe.com/api/prices/object?lang=python
    """

    id: str
    name: str
    currency: str

    images: list[HttpUrl] = []
    metadata: fields.StripeObject | None = None
    description: str | None = None

    created: fields.DatetimeFromTimestamp
    updated: fields.DatetimeFromTimestamp
