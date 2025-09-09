from pydantic import BaseModel

from stripy import constants, fields
from stripy.models.customers import Customer
from stripy.models.discounts import Discount
from stripy.models.payment_intents import PaymentIntent


class CheckoutSession(BaseModel):
    """
    https://docs.stripe.com/api/checkout/sessions/object
    """

    id: str
    mode: constants.CheckoutSessionMode
    payment_status: constants.CheckoutSessionPaymentStatus

    currency: str | None = None
    customer: Customer | None = None
    discounts: list[Discount] | None = None
    payment_intent: PaymentIntent | None = None

    created: fields.DatetimeFromTimestamp
    metadata: fields.Metadata | None = None
    expires_at: fields.DatetimeFromTimestamp
