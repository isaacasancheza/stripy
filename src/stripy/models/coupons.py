from decimal import Decimal
from typing import Annotated

from pydantic import AfterValidator, BaseModel

from stripy import constants, fields

type PercentOff = Annotated[Decimal, AfterValidator(lambda v: v / 100)]


class Coupon(BaseModel):
    """
    https://docs.stripe.com/api/coupons/object?lang=python
    """

    id: str
    valid: bool
    duration: constants.CouponDuration

    name: str | None = None
    currency: str | None = None
    amount_off: fields.DecimalFromInt | None = None
    percent_off: PercentOff | None = None

    created: fields.DatetimeFromTimestamp
