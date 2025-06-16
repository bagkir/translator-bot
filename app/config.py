from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
import os


class Settings(BaseSettings):
    BOT_TOKEN: SecretStr
    DB_PORT: str
    DB_NAME: str
    DB_PASSWORD: SecretStr
    DB_HOST: str
    DB_USER: str
    AUTH_KEY: SecretStr

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    )

    def get_db_url(self):
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD.get_secret_value()}@"
            f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


settings = Settings()
