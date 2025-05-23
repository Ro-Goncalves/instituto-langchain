from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import ClassVar
import logging

LOGGER = logging.getLogger("instituto_langchain")
LOGGER.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
LOGGER.addHandler(handler)
LOGGER.propagate = False  # Prevents duplicate messages in the root logger


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore", env_file_encoding="utf-8"
    )

    GROQ_API_KEY: str

    TTQ_MODEL_NAME: str = "deepseek-r1-distill-llama-70b"

    AGENT_SQL_DB_PATH: str = ".db/AGENT_SQL.db"

    # Logger configuration
    LOGGER: ClassVar[logging.Logger] = LOGGER


settings = Settings()