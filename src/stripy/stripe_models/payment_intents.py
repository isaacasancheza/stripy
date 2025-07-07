from typing import TYPE_CHECKING

from pydantic import BaseModel

from stripy import stripe_constants, stripe_fields

if TYPE_CHECKING:
    from stripy.stripe_models.customers import Customer
    from stripy.stripe_models.payment_methods import PaymentMethod


class PaymentIntent(BaseModel):
    """
    https://docs.stripe.com/api/payment_intents/object
    """

    id: str
    status: stripe_constants.PaymentIntentStatus
    currency: str
    amount_received: stripe_fields.StripeDecimalFromInt

    metadata: stripe_fields.Metadata | None = None
    customer: 'Customer | None' = None
    payment_method: 'PaymentMethod | None' = None

    created: stripe_fields.DatetimeFromTimestamp
    canceled_at: stripe_fields.DatetimeFromTimestamp | None = None
    cancellation_reason: stripe_constants.InvoiceCancellationReason | None = None
