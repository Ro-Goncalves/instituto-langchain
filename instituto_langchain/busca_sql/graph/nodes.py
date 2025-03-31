from typing import Dict, Any

import time
from instituto_langchain.busca_sql.graph.state import InputState
from instituto_langchain.busca_sql.configuracoes import configuracoes
from instituto_langchain.busca_sql.graph.utils.gerenciador_banco import GerenciadorBanco
from instituto_langchain.busca_sql.graph.utils.gerenciador_llm import GerenciadorLLM
from instituto_langchain.busca_sql.core.prompts import (
    ANALISAR_PERGUNTA_SYSTEM_PROMPT, 
    ANALISAR_PERGUNTA_HUMAN_PROMPT,
    GERAR_SQL_SYSTEM_PROMPT,
    GERAR_SQL_HUMAN_PROMPT,
    VALIDAR_SQL_SYSTEM_PROMPT,
    VALIDAR_SQL_HUMAN_PROMPT
)

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
    
async def node_obter_substantivos_unicos(state: InputState) -> Dict[str, Any]:
    """Identifica substantivos únicos nas tabelas e colunas relevantes."""
    pergunta_analisada = state['pergunta_analisada']
    LOGGER.info("Iniciando a busca por substantivos únicos.")
    LOGGER.debug(f"Análise da pergunta: {pergunta_analisada}")
    
    if not pergunta_analisada['is_relevante']:
        LOGGER.info("A pergunta não é relevante. Retornando lista vazia.\n")
        return {"substantivos_unicos": []}

    substantivos_unicos = set()

    for info_tabela in pergunta_analisada['tabelas_relevantes']:
        nome_tabela = info_tabela['nome_tabela']
        colunas_substantivos = info_tabela['colunas_substantivo']

        if not colunas_substantivos:
            LOGGER.debug(f"A tabela '{nome_tabela}' não possui colunas relevantes.")
            continue

        nomes_colunas = ', '.join(f"`{col}`" for col in colunas_substantivos)
        consulta = f"SELECT DISTINCT {nomes_colunas} FROM `{nome_tabela}`"
        LOGGER.debug(f"Executando consulta SQL na tabela '{nome_tabela}': {consulta}")

        try:
            resultados = GERENCIADOR_BANCO.execute_query(consulta)
            LOGGER.debug(f"Consulta retornou {len(resultados)} registros.")

            for linha in resultados:
                valores = [str(valor) for valor in linha if valor]
                substantivos_unicos.update(valores)
                LOGGER.debug(f"Valores extraídos: {valores}")

        except Exception as e:
            LOGGER.error(f"Erro ao executar consulta na tabela '{nome_tabela}': {e}\n")

    LOGGER.info(f"Processo concluído. {len(substantivos_unicos)} substantivos únicos encontrados.")
    LOGGER.info(f"Substantivos Únicos: {str(substantivos_unicos)}\n")
    return {"substantivos_unicos": list(substantivos_unicos)}

async def node_gerar_sql(state: InputState) -> Dict[str, Any]:
    """Gera uma consulta SQL com base na pergunta analisada e nos substantivos únicos."""
    pergunta = state['pergunta']
    pergunta_analisada = state['pergunta_analisada']
    substantivos_unicos = state['substantivos_unicos']

    LOGGER.info(f"Iniciando geração da consulta SQL para a pergunta: '{pergunta}'")
    start_time = time.time()

    if not pergunta_analisada['is_relevante']:
        LOGGER.warning("Pergunta não é relevante.")
        return {"consulta_sql": "NAO_RELEVANTE", "is_relevante": False}
    
    try:
        esquema = GERENCIADOR_BANCO.get_schema()
        
        LOGGER.debug("Preparando prompt para o LLM")
        prompt = ChatPromptTemplate.from_messages([
            ("system", GERAR_SQL_SYSTEM_PROMPT),
            ("human", GERAR_SQL_HUMAN_PROMPT),
        ])
       
        consulta = GERENCIADOR_LLM.invoke(
            prompt, 
            esquema=esquema, 
            pergunta=pergunta, 
            pergunta_analisada=pergunta_analisada, 
            substantivos_unicos=substantivos_unicos
        )

        if consulta.strip() == "INFORMACAO_INSUFICIENTE":
            return {"consulta_sql": "NAO_RELEVANTE"}
        
        total_time = time.time() - start_time
        LOGGER.info(f"Consulta SQL gerada com sucesso em {total_time:.3f}s")
        LOGGER.info(f"Consulta SQL: {consulta}\n")
        
        return {"consulta_sql": consulta}
        
    except Exception as e:
        LOGGER.error(f"Erro durante a geração da consulta SQL: {str(e)}\n")
        return {"consulta_sql": "ERRO_EXECUCAO", "is_relevante": False}
    
async def node_validar_corrigir_sql(state: InputState) -> Dict[str, Any]:
    """Valida e corrige a consulta SQL gerada."""
    consulta_sql = state['consulta_sql']
           
    LOGGER.info(f"Iniciando validação da consulta SQL: '{consulta_sql}'")
    start_time = time.time()
    
    if consulta_sql == "NAO_RELEVANTE":
        LOGGER.warning("A consulta não é relevante.")
        return {"consulta_sql": "NAO_RELEVANTE", "consulta_valida": False}
    
    try:
        
        esquema = GERENCIADOR_BANCO.get_schema()

        prompt = ChatPromptTemplate.from_messages([
            ("system", VALIDAR_SQL_SYSTEM_PROMPT),
            ("human", VALIDAR_SQL_HUMAN_PROMPT),
        ])

        analisador_saida = JsonOutputParser()
        
        resposta = GERENCIADOR_LLM.invoke(prompt, esquema=esquema, consulta_sql=consulta_sql)
        resultado = analisador_saida.parse(resposta)

        if resultado["valido"] and resultado["problemas"] is None:
            total_time = time.time() - start_time
            LOGGER.info(f"Consulta SQL validade em {total_time:.3f}s")
            LOGGER.info(f"Consulta SQL: {resultado['consulta_corrigida']}\n")
            
            return {"consulta_corrigida": consulta_sql, "consulta_valida": True, "consulta_problemas": None}
        
        total_time = time.time() - start_time
        LOGGER.info(f"Consulta SQL validade em {total_time:.3f}s")
        LOGGER.info(f"Consulta SQL: {resultado['consulta_corrigida']}\n")
        
        
        return {
            "consulta_corrigida": resultado["consulta_corrigida"],
            "consulta_valida": resultado["valido"],
            "consulta_problemas": resultado["problemas"]
        }
    except Exception as e:
        LOGGER.error(f"Erro ao validar a consulta SQL: {e}\n", exc_info=True)
        return {"consulta_sql": "ERRO_EXECUCAO", "consulta_valida": False, "consulta_problemas": str(e)}
    
async def node_executar_sql(state: InputState) -> Dict[str, Any]:
    """Executa a consulta SQL e retorna os resultados."""
    consulta_sql = state['consulta_sql']
    consulta_corrigida = state['consulta_corrigida']
    
    LOGGER.info(f"Iniciando a execução da consulta SQL: '{consulta_sql}'")
    start_time = time.time()
    
    if consulta_sql == "NAO_RELEVANTE":
        LOGGER.warning("A consulta não é relevante.")
        return {"resultados": "NAO_RELEVANTE"}
    
    consulta = ""
    if consulta_corrigida == "None":
        consulta = consulta_sql
    else:
        consulta = consulta_corrigida

    try:
        resultados = GERENCIADOR_BANCO.execute_query(consulta)
        
        total_time = time.time() - start_time
        LOGGER.info(f"Consulta SQL exedcutada em {total_time:.3f}s")
        LOGGER.info(f"Resultado: {str(resultados)}\n")
        
        return {"resultados": resultados}
    except Exception as e:
        LOGGER.error(f"Erro ao executar a consulta SQL: {e}\n", exc_info=True)
        return {"erro": str(e)}
