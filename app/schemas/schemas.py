from enum import Enum
from tortoise.contrib.pydantic.base import PydanticModel
from pydantic import Field


class Category(str, Enum):
    glass = "Glass"
    electronics = "Electronics"
    other = "Other"


class CargoRateSchema(PydanticModel):
    id: int = Field(ge=0)
    date: str = Field(max_length=10)
    cargo_type: Category
    rate: float = Field(ge=0)


class CostInsuranceSchema(PydanticModel):
    date: str = Field(max_length=10)
    cargo_type: Category
    rate: float = Field(ge=0)
    price: float = Field(ge=0)
    cost: float = Field(ge=0)
