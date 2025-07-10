from enum import StrEnum


class CheckoutSessionMode(StrEnum):
    """
    https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-mode
    """

    SETUP = 'setup'
    PAYMENT = 'payment'
    SUBSCRIPTION = 'subscription'


class CheckoutSessionStatus(StrEnum):
    """
    https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-status
    """

    OPEN = 'open'
    EXPIRED = 'expired'
    COMPLETE = 'complete'


class CheckoutSessionUIMode(StrEnum):
    CUSTOM = 'custom'
    HOSTED = 'hosted'
    EMBEDDED = 'embedded'


class CheckoutSessionPaymentStatus(StrEnum):
    """
    https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-payment_status
    """

    PAID = 'paid'
    UNPAID = 'unpaid'
    NO_PAYMENT_REQUIRED = 'no_payment_required'
