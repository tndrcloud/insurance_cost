from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8088
    # database_url: str = 'sqlite:///../db/database.db'


settings = Settings(
    _env_file='./.env',
    _env_file_encoding='utf-8'
)