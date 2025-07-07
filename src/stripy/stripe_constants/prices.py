from enum import StrEnum


class PriceType(StrEnum):
    """
    https://docs.stripe.com/api/prices/object?lang=python#price_object-type
    """

    ONE_TIME = 'one_time'
    RECURRING = 'recurring'


class PriceBillingScheme(StrEnum):
    """
    https://docs.stripe.com/api/prices/object?lang=python#price_object-billing_scheme
    """

    TIERED = 'tiered'
    PER_UNIT = 'per_unit'
