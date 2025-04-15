

from langchain_core.messages import BaseMessage
from pydantic import BaseModel, Field
from typing import Optional

from langchain_groq import ChatGroq

from ....core.prompts import PROMPT_ANALISE_MEMORIA
from ..long_term.vector_store import get_vector_store
from ....settings import settings

class AnaliseMemoria(BaseModel):
    """Resultado da análise de uma mensagem para conteúdo digno de memória."""
    is_importante: bool = Field(
        ..., 
        description="Se a mensagem é importante o suficiente para ser armazenada como uma memória.")
    
    memoria_formatada: Optional[str] = Field(
        ..., 
        description="A memória formatada para ser armazenada.")

class GerenciadorMemoria:
    def __init__(self):
        self.vector_store = get_vector_store()
        self.llm = ChatGroq(
            model=settings.SMALL_TEXT_MODEL_NAME,
            api_key=settings.GROQ_API_KEY,
            temperature=0.1,
            max_retries=2,
        ).with_structured_output(AnaliseMemoria)
        
    async def _analise_memoria(self, mensagem: str) -> AnaliseMemoria:
        """Analisar uma mensagem para determinar importância e formatar se necessário."""
        prompt = PROMPT_ANALISE_MEMORIA.format(message=mensagem)
        return await self.llm.ainvoke(prompt)
        
    async def extrair_armazenar_memorias(self, mensagem: BaseMessage) -> None:
        """Extrai informações importantes de uma mensagem e armazena em um vector store."""
        if mensagem.type != "human":
            return
        
        # Analisar a mensagem para importância e formatação
        analise_memoria = await self._analise_memoria(mensagem.content)
        if analise_memoria.is_importante and analise_memoria.memoria_formatada:
            # Verificar se memória semelhante existe
            memoria_similar = self.vector_store.find_similar_memory(analise_memoria.memoria_formatada)
            return
        
        
        pass