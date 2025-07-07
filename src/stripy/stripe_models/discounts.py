from typing import TYPE_CHECKING

from pydantic import BaseModel

from stripy import stripe_fields

if TYPE_CHECKING:
    from stripy.stripe_models.coupons import Coupon
    from stripy.stripe_models.customers import Customer
    from stripy.stripe_models.promotion_codes import PromotionCode


class Discount(BaseModel):
    """
    https://docs.stripe.com/api/discounts/object?lang=python
    """

    id: str
    start: stripe_fields.DatetimeFromTimestamp
    coupon: 'Coupon'
    customer: 'Customer | None' = None
    promotion_code: 'PromotionCode | None' = None
