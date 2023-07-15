from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Union


class Category(Enum):
    glass = "Glass"
    electronics = "Electronics"
    other = "Other"


class CargoRate(BaseModel):
    cargo_type: Category
    rate: float = Field(ge=0)


class DataRate(BaseModel):
    date: List[CargoRate]


class DataForCalculation(BaseModel):
    date: str
    cargo_type: Category
    price: float = Field(ge=0)


class CostInsurance(BaseModel):
    cost_insurance: float = Field(ge=0)
