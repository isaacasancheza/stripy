from stripy import stripe_fields
from stripy.stripe_models.base import get_models_base_class


class Customer(get_models_base_class()):
    """
    https://docs.stripe.com/api/customers/object?lang=python
    """

    id: str

    name: str | None = None
    email: str | None = None
    phone: str | None = None
    metadata: stripe_fields.StripeMetadata | None = None

    created: stripe_fields.StripeDatetimeFromTimestamp
