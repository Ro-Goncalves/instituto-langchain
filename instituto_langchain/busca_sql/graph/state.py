from typing import Dict, Any
from typing_extensions import TypedDict

class InputState(TypedDict):
    pergunta: str

class OutputState(TypedDict):
    pergunta_analisada: Dict[str, Any]