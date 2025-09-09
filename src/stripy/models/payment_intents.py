from pydantic import BaseModel

from stripy import constants, fields
from stripy.models.customers import Customer
from stripy.models.payment_methods import PaymentMethod


class PaymentIntent(BaseModel):
    """
    https://docs.stripe.com/api/payment_intents/object
    """

    id: str
    status: constants.PaymentIntentStatus
    currency: str
    amount_received: fields.DecimalFromInt

    metadata: fields.Metadata | None = None
    customer: Customer | None = None
    payment_method: PaymentMethod | None = None

    created: fields.DatetimeFromTimestamp
    canceled_at: fields.DatetimeFromTimestamp | None = None
    cancellation_reason: constants.InvoiceCancellationReason | None = None
