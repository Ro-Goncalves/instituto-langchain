from functools import lru_cache

from langgraph.graph import END, START, StateGraph

from instituto_langchain.busca_sql.graph.nodes import (
    node_analisar_pergunta,
    node_obter_substantivos_unicos,
    node_gerar_sql,
    node_validar_corrigir_sql,
    node_executar_sql
)

from instituto_langchain.busca_sql.graph.state import InputState, OutputState


@lru_cache(maxsize=1)
def criar_grafo_busca_sql() -> StateGraph:
    grafo_builder = StateGraph(input=InputState, output=OutputState)

    # NODES
    grafo_builder.add_node("node_analisar_pergunta", node_analisar_pergunta)
    grafo_builder.add_node("node_obter_substantivos_unicos", node_obter_substantivos_unicos)
    grafo_builder.add_node("node_gerar_sql", node_gerar_sql)
    grafo_builder.add_node("node_validar_corrigir_sql", node_validar_corrigir_sql)
    grafo_builder.add_node("node_executar_sql", node_executar_sql)

    # FLOW

    grafo_builder.add_edge(START, "node_analisar_pergunta")

    grafo_builder.add_edge("node_analisar_pergunta", "node_obter_substantivos_unicos")
    grafo_builder.add_edge("node_obter_substantivos_unicos", "node_gerar_sql")
    grafo_builder.add_edge("node_gerar_sql", "node_validar_corrigir_sql")
    grafo_builder.add_edge("node_validar_corrigir_sql", "node_executar_sql")

    grafo_builder.add_edge("node_executar_sql", END)

    return grafo_builder

grafo = criar_grafo_busca_sql().compile()