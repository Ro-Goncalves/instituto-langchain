from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import ClassVar
import logging

LOGGER = logging.getLogger("instituto_langchain")
LOGGER.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
LOGGER.addHandler(handler)
LOGGER.propagate = False  # Evita mensagens duplicadas no logger raiz


class Configuracoes(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore", env_file_encoding="utf-8"
    )
    
    GROQ_API_KEY: str
    
    TTQ_NOME_MODELO: str = "deepseek-r1-distill-llama-70b"
    
    CAMINHO_BANCO_AGENTE_SQL: str = ".db/AGENTE_SQL.db"

    # Configuração do logger
    LOGGER: ClassVar[logging.Logger] = LOGGER
    
configuracoes = Configuracoes()