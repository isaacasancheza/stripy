from pydantic import BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):
    model_config = {
        'from_attributes': True,
    }
