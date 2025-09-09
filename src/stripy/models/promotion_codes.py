from datetime import datetime, timezone

from pydantic import BaseModel

from stripy import fields
from stripy.models.coupons import Coupon
from stripy.models.customers import Customer


class PromotionCode(BaseModel):
    """
    https://docs.stripe.com/api/promotion_codes/object?lang=python
    """

    id: str
    code: str
    active: bool
    coupon: Coupon
    expires_at: fields.DatetimeFromTimestamp | None = None
    times_redeemed: int
    max_redemptions: int | None = None

    metadata: fields.Metadata | None = None
    customer: Customer | None = None

    created: fields.DatetimeFromTimestamp

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
    def amount_off(self):
        return self.coupon.amount_off

    @property
    def percent_off(self):
        return self.coupon.percent_off
