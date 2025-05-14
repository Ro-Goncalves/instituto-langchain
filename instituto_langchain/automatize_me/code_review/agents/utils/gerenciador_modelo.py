import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.language_models.chat_models import BaseChatModel

from instituto_langchain.automatize_me.configuracoes import configuracoes

class GerenciadorModelo:
        
    VARIAVEIS_OBRIGATORIA = ['GROQ_API_KEY', 'GEMINI_API_KEY']
    
    def __init__(self):        
        self.logger = configuracoes.LOGGER
        
        self.logger.info("Inicializando GerenciadorModelo")
        
        self._validar_variaveis()
        
        try:
            self.llm_deepseek = ChatGroq(
                model=configuracoes.MODELO_DEEPSEEK,
                api_key=configuracoes.GROQ_API_KEY,
                temperature=0.5,
                max_retries=2,
            )
            self.logger.info(f"LLM DEEPSEEK inicializado (modelo: {configuracoes.MODELO_DEEPSEEK}, temperatura: 0.5)")

            self.llm_gemini = ChatGoogleGenerativeAI(
                model=configuracoes.MODELO_GEMINI,
                api_key=configuracoes.GEMINI_API_KEY,
                temperature=0.5,
                max_retries=2,
            )
            self.logger.info(f"LLM GEMINI inicializado (modelo: {configuracoes.MODELO_GEMINI}, temperatura: 0.5)")
        except Exception as e:
            self.logger.error(f"Erro ao inicializar o LLM: {str(e)}\n")
            raise Exception(f"Falha na inicialização do LLM: {str(e)}")

    def _validar_variaveis(self) -> None:

        variaveis_faltantes = [var for var in self.VARIAVEIS_OBRIGATORIA if not os.getenv(var)]

        if variaveis_faltantes:
            raise ValueError(f"Variáveis obrigatórias ausentes: {', '.join(variaveis_faltantes)}")
        
    def obter_llm_deepseek(self) -> BaseChatModel:
        return self.llm_deepseek
    
    def obter_llm_gemini(self) -> BaseChatModel:
        return self.llm_gemini