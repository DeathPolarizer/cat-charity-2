from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_title: str = "Благотворительный фонд поддержки котиков QRKot"
    description: str = (
        "Сервис для управления пожертвованиями реализованный на FastAPI"
    )
    database_url: str | None = "sqlite+aiosqlite:///./cat_charity.db"
    secret: str = "SECRET"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
