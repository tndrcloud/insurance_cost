import json
from fastapi import APIRouter
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.schemas import Category
from tortoise.exceptions import ValidationError
from models.models import CargoRate, CargoRateListPydantic, Cost, CostListPydantic


router = APIRouter()

    
@router.get("/load_rates_in_database", response_model=CargoRateListPydantic)
async def load_rates() -> CargoRateListPydantic:
    with open("../rate.json", "r", encoding="utf-8") as file:
        rates = json.load(file)

    for date, tax in rates.items():
        for element in tax:
            await CargoRate.get_or_create(
                date = date, 
                cargo_type = element["cargo_type"], 
                rate = element["rate"]
                )

    return await CargoRateListPydantic.from_queryset(CargoRate.all())


@router.get("/get_insurance_cost", response_model=CostListPydantic) 
async def get_insurance_cost(date: str, cargo_type: Category, price: float) -> CostListPydantic:
    try:
        cargorate = await CargoRate.filter(date=date).filter(cargo_type=cargo_type).first()

        await Cost.get_or_create(
            date = date,
            cargo_type = cargo_type,
            rate = cargorate.rate,
            price = price,
            cost = cargorate.rate * price
        )
    
    except AttributeError:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder({"error": "date not found in database."})
    )
    except ValidationError:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder({"error": "date must be format YYYY-MM-DD."})
    )

    return await CostListPydantic.from_queryset(
        Cost.filter(date=date).filter(cargo_type=cargo_type).filter(price=price)
        )

