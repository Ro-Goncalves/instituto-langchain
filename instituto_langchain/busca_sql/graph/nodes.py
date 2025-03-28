from typing import Dict, Any

import time
from instituto_langchain.busca_sql.graph.state import InputState
from instituto_langchain.busca_sql.configuracoes import configuracoes
from instituto_langchain.busca_sql.graph.utils.gerenciador_banco import GerenciadorBanco
from instituto_langchain.busca_sql.graph.utils.gerenciador_llm import GerenciadorLLM
from instituto_langchain.busca_sql.core.prompts import ANALISAR_PERGUNTA_SYSTEM_PROMPT, ANALISAR_PERGUNTA_HUMAN_PROMPT

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

LOGGER = configuracoes.LOGGER
GERENCIADOR_BANCO = GerenciadorBanco()
GERENCIADOR_LLM = GerenciadorLLM()

async def node_analisar_pergunta(state: InputState) -> Dict[str, Any]:    
    """
    Analisa a pergunta do usuário e identifica as tabelas e colunas relevantes.
    
    Args:
        pergunta (str): Pergunta do usuário a ser analisada
        
    Returns:
        Dict[str, Any]: Dicionário contendo a análise da pergunta
    """    

    LOGGER.info(f"Iniciando análise da pergunta: '{state['pergunta']}'")
    
    try:        
        start_schema_time = time.time()
        esquema = GERENCIADOR_BANCO.get_schema()
        
        LOGGER.debug(f"Preparando prompt para o LLM")
        prompt = ChatPromptTemplate.from_messages([
            ("system", ANALISAR_PERGUNTA_SYSTEM_PROMPT),
            ("human", ANALISAR_PERGUNTA_HUMAN_PROMPT)
        ])        
       
        analisador_json = JsonOutputParser()
         
        resposta = GERENCIADOR_LLM.invoke(prompt, esquema=esquema, pergunta=state['pergunta'])          

        LOGGER.debug(f"Analisando resposta JSON")      
        try:
            resposta_analisada = analisador_json.parse(resposta) 
            
            is_relevante = resposta_analisada.get("is_relevante", False)
            num_tabelas = len(resposta_analisada.get("tabelas_relevantes", []))
            LOGGER.info(f"Análise concluída. Relevante: {is_relevante}, Tabelas identificadas: {num_tabelas}")
            
            if num_tabelas > 0:
                tabelas_nomes = [tabela.get("nome_tabela") for tabela in resposta_analisada.get("tabelas_relevantes", [])]
                LOGGER.debug(f"Tabelas relevantes: {', '.join(tabelas_nomes)}")
            
        except Exception as e:
            LOGGER.error(f"Erro ao analisar JSON da resposta: {str(e)}")
            LOGGER.error(f"Resposta que causou o erro: {resposta}\n")
            # Se houver erro no parsing, retornamos uma resposta de fallback
            resposta_analisada = {"is_relevante": False, "tabelas_relevantes": []}
        
        LOGGER.info(f"Resultado Final da Análise: {str(resposta_analisada)}")
        
        # Tempo total da operação
        total_time = time.time() - start_schema_time
        LOGGER.info(f"Análise completa em {total_time:.3f}s")
        
        # Retornar o resultado
        return {"pergunta_analisada": resposta_analisada}
        
    except Exception as e:
        LOGGER.error(f"Erro durante análise da pergunta: {str(e)}\n")
        
        return {"pergunta_analisada": {"is_relevante": False, "tabelas_relevantes": []}}