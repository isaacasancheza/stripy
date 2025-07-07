from typing import TYPE_CHECKING

from stripy import stripe_constants, stripe_fields
from stripy.stripe_models.base import get_models_base_class

if TYPE_CHECKING:
    from stripy.stripe_models.customers import Customer
    from stripy.stripe_models.payment_methods import PaymentMethod


class PaymentIntent(get_models_base_class()):
    """
    https://docs.stripe.com/api/payment_intents/object
    """

    id: str
    status: stripe_constants.PaymentIntentStatus
    currency: str
    amount_received: stripe_fields.StripeDecimalFromInt

    metadata: stripe_fields.StripeMetadata | None = None
    customer: 'Customer | None' = None
    payment_method: 'PaymentMethod | None' = None

    created: stripe_fields.StripeDatetimeFromTimestamp
    canceled_at: stripe_fields.StripeDatetimeFromTimestamp | None = None
    cancellation_reason: stripe_constants.InvoiceCancellationReason | None = None
