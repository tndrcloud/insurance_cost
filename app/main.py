import uvicorn
from settings import settings


app = FastAPI(
    title="Insurance Cost"
)


if __name__ == '__main__':
    uvicorn.run(
        "app.main:app",
        host=settings.server_host,
        port=settings.server_port,
    )
