from enum import StrEnum


class PaymentMethodCardFunding(StrEnum):
    """
    https://docs.stripe.com/api/payment_methods/object?lang=python#payment_method_object-card-funding
    """

    CREDIT = 'credit'
    DEBIT = 'debit'
    PREPAID = 'prepaid'
    UNKNOWN = 'unknown'


class PaymentMethodCardBrand(StrEnum):
    """
    https://docs.stripe.com/api/payment_methods/object?lang=python#payment_method_object-card-brand
    """

    AMEX = 'amex'
    CARTES_BANCAIRES = 'cartes_bancaires'
    DINERS = 'diners'
    DISCOVER = 'discover'
    EFTPOS_AU = 'eftpos_au'
    JCB = 'jcb'
    LINK = 'link'
    MASTERCARD = 'mastercard'
    UNIONPAY = 'unionpay'
    VISA = 'visa'
    UNKNOWN = 'unknown'
