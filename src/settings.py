from pydantic_settings import BaseSettings
from pydantic import SecretStr


class Settings(BaseSettings):
    openai_api_key: SecretStr
    model: str
    db_user: str
    db_pass: str
    db_host: str
    db_port: int
    db_name: str
