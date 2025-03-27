from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

import logging

from instituto_langchain.busca_sql.configuracoes import configuracoes

import os, time, re


class GerenciadorLLM:
        
    VARIAVEIS_OBRIGATORIA = ['GROQ_API_KEY']
    
    def __init__(self):
        """Inicializa o gerenciador de LLM com o modelo Groq."""
        self.logger = logging.getLogger(__name__)
        
        self.logger.info("Inicializando GerenciadorLLM com o modelo deepseek-r1-distill-llama-70b")
        
        self._validar_variaveis()
        
        try:
            self.llm = ChatGroq(
                model=configuracoes.TTQ_NOME_MODELO,
                api_key=configuracoes.GROQ_API_KEY,
                temperature=0.1,
                max_retries=2,
            )
            self.logger.info("LLM inicializado com sucesso (modelo: deepseek-r1-distill-llama-70b, temperatura: 0.1)\n")
        except Exception as e:
            self.logger.error(f"Erro ao inicializar o LLM: {str(e)}\n")
            raise Exception(f"Falha na inicialização do LLM: {str(e)}")

    def _validar_variaveis(self) -> None:

        variaveis_faltantes = [var for var in self.VARIAVEIS_OBRIGATORIA if not os.getenv(var)]

        if variaveis_faltantes:
            raise ValueError(f"Variáveis obrigatórias ausentes: {', '.join(variaveis_faltantes)}")
        
    def invoke(self, prompt: ChatPromptTemplate, **kwargs) -> str:
        """
        Invoca o LLM com o prompt fornecido e parâmetros adicionais.
        
        Args:
            prompt: O template de prompt do chat
            **kwargs: Variáveis para formatação do prompt
            
        Returns:
            str: A resposta do modelo
        """       
        
        try:           
            start_format_time = time.time()
            messages = prompt.format_messages(**kwargs)
            format_time = time.time() - start_format_time
            
            self.logger.info("Enviando requisição ao modelo...")
            start_invoke_time = time.time()
            response = self.llm.invoke(messages)
            invoke_time = time.time() - start_invoke_time
           
            response_content = response.content
            self.logger.debug(f"Resposta recebida em {invoke_time:.3f}s ({len(response_content)} caracteres)")
            self.logger.info(f"Resposta do LLM: {response_content}")
            
            # Log de métricas
            total_time = format_time + invoke_time
            self.logger.debug(f"Invocação completa. Tempo total: {total_time:.3f}s")
            
            return re.sub(r'<think>.*?</think>\s*', '', response_content, flags=re.DOTALL)
            
        except Exception as e:
            self.logger.error(f"Erro ao invocar o LLM: {str(e)}")
            raise Exception(f"Falha na invocação do LLM: {str(e)}")