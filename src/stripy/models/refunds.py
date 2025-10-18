from pydantic import BaseModel

from stripy import fields
from stripy.models.payment_intents import PaymentIntent


class Refund(BaseModel):
    """
    https://docs.stripe.com/api/refunds/object
    """

    id: str
    amount: fields.DecimalFromInt
    payment_intent: PaymentIntent

    created: fields.DatetimeFromTimestamp
    metadata: fields.Metadata | None = None
