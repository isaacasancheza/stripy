from stripy import fields
from stripy.models.base import BaseModel


class Refund(BaseModel):
    """
    https://docs.stripe.com/api/refunds/object
    """

    id: str
    amount: fields.DecimalFromInt

    created: fields.DatetimeFromTimestamp
