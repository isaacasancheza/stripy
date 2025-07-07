from enum import StrEnum


class CouponDuration(StrEnum):
    """
    https://docs.stripe.com/api/coupons/object?lang=python#coupon_object-duration
    """

    ONCE = 'once'
    FOREVER = 'forever'
    REPEATING = 'repeating'
