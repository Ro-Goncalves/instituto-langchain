from typing import Dict, Any

import time
from instituto_langchain.le_rec_hum.graph.state import InputState
from instituto_langchain.le_rec_hum.settings import settings
from instituto_langchain.le_rec_hum.graph.utils.data_base_manager import DatabaseManager
from instituto_langchain.le_rec_hum.graph.utils.llm_manager import LLMManager
from instituto_langchain.le_rec_hum.core.prompts import (
    ANALYZE_QUESTION_SYSTEM_PROMPT,
    ANALYZE_QUESTION_HUMAN_PROMPT,
    GENERATE_SQL_SYSTEM_PROMPT,
    GENERATE_SQL_HUMAN_PROMPT,
    VALIDATE_SQL_SYSTEM_PROMPT,
    VALIDATE_SQL_HUMAN_PROMPT
)

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

LOGGER = settings.LOGGER
DB_MANAGER = DatabaseManager()
LLM_MANAGER = LLMManager()

async def node_analyze_question(state: InputState) -> Dict[str, Any]:
    """
    Analyzes the user's question to identify relevant tables and columns.
    
    Args:
        state (InputState): Contains the user's question
    
    Returns:
        Dict[str, Any]: Dictionary containing the analysis result
    """    
    LOGGER.info(f"Starting question analysis: '{state['pergunta']}'")

    try:
        start_schema_time = time.time()
        schema = DB_MANAGER.get_schema()

        LOGGER.debug("Preparing prompt for the LLM")
        prompt = ChatPromptTemplate.from_messages([
            ("system", ANALYZE_QUESTION_SYSTEM_PROMPT),
            ("human", ANALYZE_QUESTION_HUMAN_PROMPT)
        ])
        
        json_parser = JsonOutputParser()
        response = LLM_MANAGER.invoke(prompt, esquema=schema, pergunta=state['pergunta'])

        LOGGER.debug("Parsing JSON response")
        try:
            parsed_response = json_parser.parse(response)

            is_relevant = parsed_response.get("is_relevante", False)
            table_count = len(parsed_response.get("tabelas_relevantes", []))
            LOGGER.info(f"Analysis complete. Relevant: {is_relevant}, Tables identified: {table_count}")

            if table_count > 0:
                table_names = [tbl.get("nome_tabela") for tbl in parsed_response.get("tabelas_relevantes", [])]
                LOGGER.debug(f"Relevant tables: {', '.join(table_names)}")
                
        except Exception as e:
            LOGGER.error(f"Error parsing JSON response: {str(e)}")
            LOGGER.error(f"Faulty response: {response}\n")
            parsed_response = {"is_relevante": False, "tabelas_relevantes": []}

        total_time = time.time() - start_schema_time
        LOGGER.info(f"Final analysis result: {str(parsed_response)}")
        LOGGER.info(f"Analysis completed in {total_time:.3f}s")

        return {"pergunta_analisada": parsed_response}

    except Exception as e:
        LOGGER.error(f"Error during question analysis: {str(e)}\n")
        return {"pergunta_analisada": {"is_relevante": False, "tabelas_relevantes": []}}


async def node_extract_unique_nouns(state: InputState) -> Dict[str, Any]:
    """Extracts unique nouns from the relevant tables and columns."""
    analyzed_question = state['pergunta_analisada']
    LOGGER.info("Starting unique noun extraction.")
    LOGGER.debug(f"Question analysis: {analyzed_question}")
    
    if not analyzed_question['is_relevante']:
        LOGGER.info("The question is not relevant. Returning empty list.\n")
        return {"substantivos_unicos": []}

    unique_nouns = set()

    for table_info in analyzed_question['tabelas_relevantes']:
        table_name = table_info['nome_tabela']
        noun_columns = table_info['colunas_substantivo']

        if not noun_columns:
            LOGGER.debug(f"Table '{table_name}' has no relevant columns.")
            continue

        column_names = ', '.join(f"`{col}`" for col in noun_columns)
        query = f"SELECT DISTINCT {column_names} FROM `{table_name}`"
        LOGGER.debug(f"Executing SQL query on table '{table_name}': {query}")

        try:
            results = DB_MANAGER.execute_query(query)
            LOGGER.debug(f"Query returned {len(results)} records.")

            for row in results:
                values = [str(value) for value in row if value]
                unique_nouns.update(values)
                LOGGER.debug(f"Extracted values: {values}")

        except Exception as e:
            LOGGER.error(f"Error executing query on table '{table_name}': {e}\n")

    LOGGER.info(f"Process completed. {len(unique_nouns)} unique nouns found.")
    LOGGER.info(f"Unique Nouns: {str(unique_nouns)}\n")
    return {"substantivos_unicos": list(unique_nouns)}


async def node_generate_sql(state: InputState) -> Dict[str, Any]:
    """Generates an SQL query based on the analyzed question and extracted nouns."""
    question = state['pergunta']
    analyzed_question = state['pergunta_analisada']
    unique_nouns = state['substantivos_unicos']

    LOGGER.info(f"Starting SQL generation for question: '{question}'")
    start_time = time.time()

    if not analyzed_question['is_relevante']:
        LOGGER.warning("Question is not relevant.")
        return {"consulta_sql": "NAO_RELEVANTE", "is_relevante": False}

    try:
        schema = DB_MANAGER.get_schema()

        LOGGER.debug("Preparing prompt for LLM")
        prompt = ChatPromptTemplate.from_messages([
            ("system", GENERATE_SQL_SYSTEM_PROMPT),
            ("human", GENERATE_SQL_HUMAN_PROMPT),
        ])

        query = LLM_MANAGER.invoke(
            prompt,
            esquema=schema,
            pergunta=question,
            pergunta_analisada=analyzed_question,
            substantivos_unicos=unique_nouns
        )

        if query.strip() == "INFORMACAO_INSUFICIENTE":
            return {"consulta_sql": "NAO_RELEVANTE"}

        total_time = time.time() - start_time
        LOGGER.info(f"SQL query generated in {total_time:.3f}s")
        LOGGER.info(f"Generated SQL: {query}\n")

        return {"consulta_sql": query}

    except Exception as e:
        LOGGER.error(f"Error generating SQL query: {str(e)}\n")
        return {"consulta_sql": "ERRO_EXECUCAO", "is_relevante": False}


async def node_validate_and_correct_sql(state: InputState) -> Dict[str, Any]:
    """Validates and corrects the generated SQL query."""
    sql_query = state['consulta_sql']

    LOGGER.info(f"Starting SQL validation: '{sql_query}'")
    start_time = time.time()

    if sql_query == "NAO_RELEVANTE":
        LOGGER.warning("The query is not relevant.")
        return {"consulta_sql": "NAO_RELEVANTE", "consulta_valida": False}

    try:
        schema = DB_MANAGER.get_schema()

        prompt = ChatPromptTemplate.from_messages([
            ("system", VALIDATE_SQL_SYSTEM_PROMPT),
            ("human", VALIDATE_SQL_HUMAN_PROMPT),
        ])

        json_parser = JsonOutputParser()
        response = LLM_MANAGER.invoke(prompt, esquema=schema, consulta_sql=sql_query)
        result = json_parser.parse(response)

        total_time = time.time() - start_time
        LOGGER.info(f"SQL validated in {total_time:.3f}s")
        LOGGER.info(f"Corrected SQL: {result['consulta_corrigida']}\n")

        return {
            "consulta_corrigida": result["consulta_corrigida"],
            "consulta_valida": result["valido"],
            "consulta_problemas": result["problemas"]
        }

    except Exception as e:
        LOGGER.error(f"Error validating SQL query: {e}\n", exc_info=True)
        return {"consulta_sql": "ERRO_EXECUCAO", "consulta_valida": False, "consulta_problemas": str(e)}


async def node_execute_sql(state: InputState) -> Dict[str, Any]:
    """Executes the SQL query and returns the results."""
    sql_query = state['consulta_sql']
    corrected_query = state['consulta_corrigida']

    LOGGER.info(f"Starting SQL execution: '{sql_query}'")
    start_time = time.time()

    if sql_query == "NAO_RELEVANTE":
        LOGGER.warning("The query is not relevant.")
        return {"resultados": "NAO_RELEVANTE"}

    query = sql_query if corrected_query == "None" else corrected_query

    try:
        results = DB_MANAGER.execute_query(query)

        total_time = time.time() - start_time
        LOGGER.info(f"SQL executed in {total_time:.3f}s")
        LOGGER.info(f"Results: {str(results)}\n")

        return {"resultados": results}
    except Exception as e:
        LOGGER.error(f"Error executing SQL query: {e}\n", exc_info=True)
        return {"erro": str(e)}
