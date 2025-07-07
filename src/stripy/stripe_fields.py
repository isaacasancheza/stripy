from datetime import datetime, timezone
from decimal import Decimal
from typing import Any

from pydantic import GetCoreSchemaHandler
from pydantic_core import core_schema

type StripeMetadata = dict[str, str]


class StripeDecimalFromInt(Decimal):
    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        source: type[Any],
        handler: GetCoreSchemaHandler,
    ) -> core_schema.CoreSchema:
        return core_schema.union_schema(
            [
                core_schema.chain_schema(
                    [
                        core_schema.int_schema(),
                        core_schema.no_info_plain_validator_function(
                            cls._int_to_decimal,
                        ),
                    ]
                ),
                core_schema.decimal_schema(decimal_places=2),
            ],
        )

    @classmethod
    def _int_to_decimal(cls, value: int) -> Decimal:
        return Decimal(str(value / 100))


class StripeDatetimeFromTimestamp(datetime):
    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        source: type[Any],
        handler: GetCoreSchemaHandler,
    ) -> core_schema.CoreSchema:
        return core_schema.union_schema(
            [
                core_schema.chain_schema(
                    [
                        core_schema.int_schema(),
                        core_schema.no_info_plain_validator_function(
                            cls._timestamp_to_aware_datetime,
                        ),
                    ],
                ),
                core_schema.datetime_schema(tz_constraint='aware'),
            ],
        )

    @classmethod
    def _timestamp_to_aware_datetime(cls, value: int) -> datetime:
        return datetime.fromtimestamp(value, tz=timezone.utc)
