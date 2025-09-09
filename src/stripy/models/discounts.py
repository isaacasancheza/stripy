from pydantic import BaseModel

from stripy import fields
from stripy.models.coupons import Coupon
from stripy.models.customers import Customer
from stripy.models.promotion_codes import PromotionCode


class Discount(BaseModel):
    """
    https://docs.stripe.com/api/discounts/object?lang=python
    """

    id: str
    start: fields.DatetimeFromTimestamp
    coupon: Coupon
    customer: Customer | None = None
    promotion_code: PromotionCode | None = None
