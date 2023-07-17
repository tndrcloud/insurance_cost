from schemas.schemas import Category
from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator


class CargoRate(Model):
    """Модель тип груза-тариф"""

    id = fields.IntField(pk=True)
    date = fields.CharField(max_length=10)
    cargo_type = fields.CharEnumField(Category)
    rate = fields.FloatField()


class Cost(Model):
    """Модель стоимость страхования"""

    id = fields.IntField(pk=True)
    date = fields.CharField(max_length=10)
    cargo_type = fields.CharEnumField(Category)
    rate = fields.FloatField()
    price = fields.FloatField()
    cost = fields.FloatField()


CargoRatePydantic = pydantic_model_creator(CargoRate, name="Cargo")
CostPydantic = pydantic_model_creator(Cost, name="Cost")

CargoRateListPydantic = pydantic_queryset_creator(CargoRate)
CostListPydantic = pydantic_queryset_creator(Cost)
