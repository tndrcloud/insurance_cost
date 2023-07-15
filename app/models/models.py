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
    rate: int = Field(ge=0)


class DataRate(BaseModel):
    date: List[CargoRate]
