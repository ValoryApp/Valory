from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[1]
ENV_FILE = BASE_DIR / ".env"
LOG_FILE_PATH = BASE_DIR / "log.txt"


class Settings(BaseSettings):
    PROJECT_NAME: str = "My Project"
    PROJECT_DESCRIPTION: str = "API"
    VERSION: str = "1.0.0"
    DEBUG: bool = False

    FRONTEND_URL: str
    BACKEND_URL: str

    TWITCH_CLIENT_ID: str
    TWITCH_CLIENT_SECRET: str

    DATABASE_LOGIN: str = "user"
    DATABASE_PASSWORD: str = "password"
    DATABASE_NAME: str = "database"
    DATABASE_IP: str = "localhost"
    DATABASE_PORT: int = 5432

    model_config = SettingsConfigDict(env_file=ENV_FILE)

    @property
    def REDIRECT_URI(self) -> str:
        return f"{self.BACKEND_URL}/api/auth/callback"

    @property
    def DB_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DATABASE_LOGIN}:{self.DATABASE_PASSWORD}@{self.DATABASE_IP}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"


settings = Settings()
database_url = settings.DB_URL
