from decouple import config


class Settings:
    LOG_DIR: str = config("LOG_DIR", default="logs")
    DB_DEBUG: bool = config("DB_DEBUG", default=False)
    DB_TYPE: str = config("DB_TYPE", default="postgresql+asyncpg")
    DB_HOST: str = config("DB_HOST", default="localhost")
    DB_USER: str = config("DB_USER", default="postgres")
    DB_PASS: str = config("DB_PASS", default="postgres")
    DB_BASE: str = config("DB_BASE", default="demo_db")
    DB_URL: str = f"{DB_TYPE}://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_BASE}"


settings = Settings()
