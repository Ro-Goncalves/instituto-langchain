from functools import lru_cache

from langgraph.graph import END, START, StateGraph

from .nodes import (
    node_analisar_pergunta
)

from .state import BuscaSqlState


@lru_cache(maxsize=1)
def criar_grafo_busca_sql() -> StateGraph:
    grafo_builder = StateGraph(BuscaSqlState)

    # NODES
    grafo_builder.add_node("node_analisar_pergunta", node_analisar_pergunta)