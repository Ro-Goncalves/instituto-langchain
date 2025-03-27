

# class LLMManager:
#     def __init__(self):
#         """Inicializa o gerenciador de LLM com o modelo Groq."""
#         LOGGER.info("Inicializando LLMManager com o modelo deepseek-r1-distill-llama-70b")
        
#         api_key = os.getenv("GROQ_API_KEY")
#         if not api_key:
#             LOGGER.error("GROQ_API_KEY não encontrada nas variáveis de ambiente\n")
#             raise ValueError("GROQ_API_KEY não configurada. Configure a variável de ambiente GROQ_API_KEY.")
        
#         try:
#             self.llm = ChatGroq(
#                 model="deepseek-r1-distill-llama-70b",
#                 api_key=api_key,
#                 temperature=0.1,
#                 max_retries=2,
#             )
#             LOGGER.info("LLM inicializado com sucesso (modelo: deepseek-r1-distill-llama-70b, temperatura: 0.1)\n")
#         except Exception as e:
#             LOGGER.error(f"Erro ao inicializar o LLM: {str(e)}\n")
#             raise Exception(f"Falha na inicialização do LLM: {str(e)}")

#     def invoke(self, prompt: ChatPromptTemplate, **kwargs) -> str:
#         """
#         Invoca o LLM com o prompt fornecido e parâmetros adicionais.
        
#         Args:
#             prompt: O template de prompt do chat
#             **kwargs: Variáveis para formatação do prompt
            
#         Returns:
#             str: A resposta do modelo
#         """       
        
#         try:           
#             start_format_time = time.time()
#             messages = prompt.format_messages(**kwargs)
#             format_time = time.time() - start_format_time
            
#             LOGGER.info("Enviando requisição ao modelo...")
#             start_invoke_time = time.time()
#             response = self.llm.invoke(messages)
#             invoke_time = time.time() - start_invoke_time
           
#             response_content = response.content
#             LOGGER.debug(f"Resposta recebida em {invoke_time:.3f}s ({len(response_content)} caracteres)")
#             LOGGER.info(f"Resposta do LLM: {response_content}")
            
#             # Log de métricas
#             total_time = format_time + invoke_time
#             LOGGER.debug(f"Invocação completa. Tempo total: {total_time:.3f}s")
            
#             return re.sub(r'<think>.*?</think>\s*', '', response_content, flags=re.DOTALL)
            
#         except Exception as e:
#             LOGGER.error(f"Erro ao invocar o LLM: {str(e)}")
#             raise Exception(f"Falha na invocação do LLM: {str(e)}")