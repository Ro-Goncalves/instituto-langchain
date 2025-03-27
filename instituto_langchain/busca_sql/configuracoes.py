from pydantic_settings import BaseSettings, SettingsConfigDict

import logging


class Configuracoes(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore", env_file_encoding="utf-8"
    )
    
    GROQ_API_KEY: str
    
    TTQ_NOME_MODELO: str = "deepseek-r1-distill-llama-70b"
    
    CAMINHO_BANCO_AGENTE_SQL: str = "../.db/AGENTE_SQL.db"

    LOGGER: logging = logging.basicConfig(
        level=logging.INFO,   
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[        
            logging.StreamHandler()
        ]
)
    
configuracoes = Configuracoes()