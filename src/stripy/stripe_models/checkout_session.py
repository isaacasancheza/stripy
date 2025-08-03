from pydantic import BaseModel

from stripy import stripe_constants, stripe_fields
from stripy.stripe_models.customers import Customer
from stripy.stripe_models.discounts import Discount
from stripy.stripe_models.payment_intents import PaymentIntent


class CheckoutSession(BaseModel):
    """
    https://docs.stripe.com/api/checkout/sessions/object
    """

    id: str
    mode: stripe_constants.CheckoutSessionMode
    payment_status: stripe_constants.CheckoutSessionPaymentStatus

    currency: str | None = None
    customer: Customer | None = None
    discounts: list[Discount] | None = None
    payment_intent: PaymentIntent | None = None

    created: stripe_fields.DatetimeFromTimestamp
    metadata: stripe_fields.Metadata | None = None
    expires_at: stripe_fields.DatetimeFromTimestamp
