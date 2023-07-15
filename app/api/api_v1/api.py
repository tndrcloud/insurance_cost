import json
from typing import List, Dict
from app.models import *



@app.exception_handler(ResponseValidationError)
async def validation_exception_handler(request: Request, exc: ResponseValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()})
    )


@app.get("/get_insurance_from_file", response_model=List[DataForCalculation])
async def get_cost(date: str, category: Category, price: float) -> List[CostInsurance]:
    with open("rate.json", "r", encoding="utf-8") as file:
        rates = json.load(file)

    return [tax["rate"] * price for tax in rates[date] if tax.get("cargo_type") == category]


@app.get("/get_cost_from_db/{category}", response_model=List[CostInsurance])
async def get_cost(date: str, category: Category) -> List[CostInsurance]:
    ...
    