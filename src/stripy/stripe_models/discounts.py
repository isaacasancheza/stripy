from typing import TYPE_CHECKING

from stripy import stripe_fields
from stripy.stripe_models.base import get_models_base_class

if TYPE_CHECKING:
    from stripy.stripe_models.coupons import Coupon
    from stripy.stripe_models.customers import Customer
    from stripy.stripe_models.promotion_codes import PromotionCode


class Discount(get_models_base_class()):
    """
    https://docs.stripe.com/api/discounts/object?lang=python
    """

    id: str
    start: stripe_fields.StripeDatetimeFromTimestamp
    coupon: 'Coupon'
    customer: 'Customer | None' = None
    promotion_code: 'PromotionCode | None' = None
