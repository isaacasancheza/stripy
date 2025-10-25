from pydantic import BaseModel

from stripy import fields


class Refund(BaseModel):
    """
    https://docs.stripe.com/api/refunds/object
    """

    id: str
    amount: fields.DecimalFromInt

    created: fields.DatetimeFromTimestamp
    metadata: fields.Metadata | None = None
