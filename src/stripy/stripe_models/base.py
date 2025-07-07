from pydantic import BaseModel

_models_base_class = None


def set_models_base_class(
    cls: type,
    /,
) -> None:
    global _models_base_class
    _models_base_class = cls


def get_models_base_class() -> type:
    return _models_base_class or BaseModel
