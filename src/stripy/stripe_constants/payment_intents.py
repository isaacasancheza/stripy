from enum import StrEnum


class PaymentIntentStatus(StrEnum):
    """
    https://docs.stripe.com/api/payment_intents/object#payment_intent_object-status
    """

    CANCELED = 'canceled'
    SUCCEEDED = 'succeeded'
    PROCESSING = 'processing'
    REQUIRES_ACTION = 'requires_action'
    REQUIRES_CAPTURE = 'requires_capture'
    REQUIRES_CONFIRMATION = 'requires_confirmation'
    REQUIRES_PAYMENT_METHOD = 'requires_payment_method'


class PaymentIntentCaptureMethod(StrEnum):
    """
    https://docs.stripe.com/api/payment_intents/object#payment_intent_object-capture_method
    """

    AUTOMATIC = 'automatic'
    AUTOMATIC_ASYNC = 'automatic_async'
    MANUAL = 'manual'


class PaymentIntentConfirmationMethod(StrEnum):
    """
    https://docs.stripe.com/api/payment_intents/object#payment_intent_object-confirmation_method
    """

    AUTOMATIC = 'automatic'
    MANUAL = 'manual'
