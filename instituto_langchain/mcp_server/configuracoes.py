from pydantic_settings import BaseSettings, SettingsConfigDict


class Configuracoes(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore", env_file_encoding="utf-8"
    )

    GROQ_API_KEY: str   

    MODELO_LLAMA: str = "llama-3.3-70b-versatile"
    MODELO_GEMMA: str = "gemma2-9b-it"
    MODELO_DEEPSEEK: str = "deepseek-r1-distill-llama-70b"
    
    CAMINHO_ARQUIVOS: str = ".arquivos/"
    CAMINHO_SERVERS: str = "instituto_langchain/mcp_server/server/"
    
    CLICKUP_API_KEY: str
    CLICKUP_TEAM_ID: str

configuracoes = Configuracoes()
