from decimal import Decimal
from typing import Annotated

from pydantic import AfterValidator, BaseModel

from stripy import stripe_constants, stripe_fields

type PercentOff = Annotated[Decimal, AfterValidator(lambda v: v / 100)]


class Coupon(BaseModel):
    """
    https://docs.stripe.com/api/coupons/object?lang=python
    """

    id: str
    valid: bool
    duration: stripe_constants.CouponDuration

    name: str | None = None
    currency: str | None = None
    amount_off: stripe_fields.DecimalFromInt | None = None
    percent_off: PercentOff | None = None

    created: stripe_fields.DatetimeFromTimestamp
