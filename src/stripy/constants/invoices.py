from enum import StrEnum


class InvoiceStatus(StrEnum):
    """
    https://docs.stripe.com/api/invoices/object?lang=python#invoice_object-status
    """

    VOID = 'void'
    OPEN = 'open'
    PAID = 'paid'
    DRAFT = 'draft'
    UNCOLLECTIBLE = 'uncollectible'


class InvoiceCancellationReason(StrEnum):
    """
    https://docs.stripe.com/api/payment_intents/object#payment_intent_object-cancellation_reason
    """

    ABANDONED = 'abandoned'
    AUTOMATIC = 'automatic'
    DUPLICATE = 'duplicate'
    EXPIRED = 'expired'
    FAILED_INVOICE = 'failed_invoice'
    FRAUDULENT = 'fraudulent'
    REQUESTED_BY_CUSTOMER = 'requested_by_customer'
    VOID_INVOICE = 'void_invoice'


class InvoiceCollectionMethod(StrEnum):
    """
    https://docs.stripe.com/api/invoices/object?lang=python#invoice_object-collection_method
    """

    SEND_INVOICE = 'send_invoice'
    CHARGE_AUTOMATICALLY = 'charge_automatically'
