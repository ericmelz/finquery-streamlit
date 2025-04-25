from pydantic_settings import BaseSettings
from pydantic import SecretStr


class Settings(BaseSettings):
    openai_api_key: SecretStr
    openai_llm_model: str
    db_user: SecretStr
    db_pass: SecretStr
    db_host: SecretStr
    db_port: SecretStr
    db_name: SecretStr
