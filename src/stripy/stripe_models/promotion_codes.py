from datetime import datetime, timezone
from typing import TYPE_CHECKING

from stripy import stripe_fields
from stripy.stripe_models.base import get_models_base_class

if TYPE_CHECKING:
    from stripy.stripe_models.coupons import Coupon
    from stripy.stripe_models.customers import Customer


class PromotionCode(get_models_base_class()):
    """
    https://docs.stripe.com/api/promotion_codes/object?lang=python
    """

    id: str
    code: str
    active: bool
    coupon: 'Coupon'
    expires_at: stripe_fields.StripeDatetimeFromTimestamp | None = None
    times_redeemed: int
    max_redemptions: int | None = None

    metadata: stripe_fields.StripeMetadata | None = None
    customer: 'Customer | None' = None

    created: stripe_fields.StripeDatetimeFromTimestamp

    @property
    def expired(self):
        if self.expires_at:
            return datetime.now(timezone.utc) > self.expires_at
        return False

    @property
    def redeemable(self):
        if self.max_redemptions is not None:
            if self.times_redeemed >= self.max_redemptions:
                return False
        return True

    @property
    def duration(self):
        return self.coupon.duration

    @property
    def duration_in_months(self):
        return self.coupon.duration_in_months

    @property
    def amount_off(self):
        return self.coupon.amount_off

    @property
    def percent_off(self):
        return self.coupon.percent_off
