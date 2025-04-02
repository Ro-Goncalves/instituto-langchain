from typing import Dict, Any, List
from typing_extensions import TypedDict

class InputState(TypedDict):
    pergunta: str
    pergunta_analisada: Dict[str, Any]
    substantivos_unicos: List[str]
    consulta_sql: str
    consulta_corrigida: str
    resultados: List[Any]

class OutputState(TypedDict):
    pergunta_analisada: Dict[str, Any]
    substantivos_unicos: List[str]
    consulta_sql: str
    consulta_corrigida: str
    consulta_valida: bool
    consulta_problemas: str
    resultados: List[Any]
