from typing import Dict, Any

from state import BuscaSqlState
from instituto_langchain.busca_sql.configuracoes import configuracoes

LOGGER = configuracoes.LOGGER

async def node_analisar_pergunta(state: BuscaSqlState) -> Dict[str, Any]:    
    """
    Analisa a pergunta do usuário e identifica as tabelas e colunas relevantes.
    
    Args:
        pergunta (str): Pergunta do usuário a ser analisada
        
    Returns:
        Dict[str, Any]: Dicionário contendo a análise da pergunta
    """    

    LOGGER.info(f"Iniciando análise da pergunta: '{pergunta}'")
    
    try:        
        start_schema_time = time.time()
        esquema = db_manager.get_schema()
        
        LOGGER.debug(f"Preparando prompt para o LLM")
        prompt = ChatPromptTemplate.from_messages([
            ("system", '''Você é um analista de dados que pode ajudar a resumir tabelas SQL e interpretar perguntas de usuários sobre um banco de dados.  
Dada a pergunta e o esquema do banco de dados, identifique as tabelas e colunas relevantes.  
Se a pergunta não for relevante para o banco de dados ou se não houver informações suficientes para respondê-la, defina "is_relevante" como false.
Sua resposta deve estar no seguinte formato JSON:
{{
    "is_relevante": boolean,
    "tabelas_relevantes": [
        {{
            "nome_tabela": string,
            "colunas": [string],
            "colunas_substantivo": [string]
        }}
    ]
}}
O campo "colunas_substantivo" deve conter apenas as colunas que são relevantes para a pergunta e que contêm substantivos ou nomes.  
Por exemplo, a coluna "Nome do Artista" contém substantivos relevantes para a pergunta "Quais são os artistas mais vendidos?",  
mas a coluna "ID do Artista" não é relevante, pois não contém um substantivo. Não inclua colunas que contenham números.
'''),
            ("human", "===Esquema do banco de dados:\n{esquema}\n\n===Pergunta do usuário:\n{pergunta}\n\nIdentifique as tabelas e colunas relevantes:")
        ])        
       
        analisador_json = JsonOutputParser()
         
        resposta = llm_manager.invoke(prompt, esquema=esquema, pergunta=pergunta)          

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