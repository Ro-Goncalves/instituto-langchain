from functools import lru_cache

from langgraph.graph import END, START, StateGraph

from instituto_langchain.le_rec_hum.graph.nodes import (
    node_analyze_question,
    node_extract_unique_nouns,
    node_generate_sql,
    node_validate_and_correct_sql,
    node_execute_sql
)

from instituto_langchain.le_rec_hum.graph.state import InputState, OutputState


@lru_cache(maxsize=1)
def create_sql_search_graph() -> StateGraph:
    graph_builder = StateGraph(input=InputState, output=OutputState)

    # NODES
    graph_builder.add_node("node_analyze_question", node_analyze_question)
    graph_builder.add_node("node_extract_unique_nouns", node_extract_unique_nouns)
    graph_builder.add_node("node_generate_sql", node_generate_sql)
    graph_builder.add_node("node_validate_and_correct_sql", node_validate_and_correct_sql)
    graph_builder.add_node("node_execute_sql", node_execute_sql)

    # FLOW

    graph_builder.add_edge(START, "node_analyze_question")

    graph_builder.add_edge("node_analyze_question", "node_extract_unique_nouns")
    graph_builder.add_edge("node_extract_unique_nouns", "node_generate_sql")
    graph_builder.add_edge("node_generate_sql", "node_validate_and_correct_sql")
    graph_builder.add_edge("node_validate_and_correct_sql", "node_execute_sql")

    graph_builder.add_edge("node_execute_sql", END)

    return graph_builder


graph = create_sql_search_graph().compile()
