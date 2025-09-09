from pydantic import BaseModel

from stripy import constants, fields


class PaymentMethodCard(BaseModel):
    """
    https://docs.stripe.com/api/payment_methods/object?lang=python#payment_method_object-card
    """

    brand: constants.PaymentMethodCardBrand
    exp_month: int
    exp_year: int
    funding: constants.PaymentMethodCardFunding
    last4: str


class PaymentMethod(BaseModel):
    """
    https://docs.stripe.com/api/payment_methods/object?lang=python
    """

    id: str
    type: str
    card: PaymentMethodCard | None = None

    created: fields.DatetimeFromTimestamp
