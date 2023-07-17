import uvicorn
from envparse import Env
from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse
from settings import settings
from fastapi import FastAPI
from models.models import *
from tortoise.contrib.fastapi import register_tortoise
from api.api_v1.api import api_router


env = Env()
env.read_envfile("../.env")


app = FastAPI(
    title="Insurance Cost"
)

app.include_router(api_router)


@app.exception_handler(ResponseValidationError)
async def validation_exception_handler(request: Request, exc: ResponseValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()})
    )


register_tortoise(
    app,
    db_url=env.str("DB_PATH_TORTOISE"),
    modules={"models": ["models.models"]},
    generate_schemas=True,
    add_exception_handlers=True
    )


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host=settings.server_host,
        port=settings.server_port,
    )
