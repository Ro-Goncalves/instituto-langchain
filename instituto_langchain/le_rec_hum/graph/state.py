from typing import Dict, Any, List
from typing_extensions import TypedDict

class InputState(TypedDict):
    question: str
    analyzed_question: Dict[str, Any]
    unique_nouns: List[str]
    sql_query: str
    corrected_query: str
    query_results: List[Any]

class OutputState(TypedDict):
    analyzed_question: Dict[str, Any]
    unique_nouns: List[str]
    sql_query: str
    corrected_query: str
    query_valid: bool
    query_issues: str
    query_results: List[Any]
