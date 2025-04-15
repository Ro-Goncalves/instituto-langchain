import os
from typing import Optional, List
from functools import lru_cache
from dataclasses import dataclass
from datetime import datetime

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer

from ....settings import settings

@dataclass
class Memoria:
    """Representa uma entrada de memória no vector store."""
    
    texto: str
    metadata: dict
    score: Optional[float] = None
    
    @property
    def id(self) -> Optional[str]:
        return self.metadata.get("id")
    
    @property
    def timestamp(self) -> Optional[datetime]:
        ts = self.metadata.get("timestamp")
        return datetime.fromtimestamp(ts) if ts else None
    
class VectorStore:
    """classe para manipular operações de vector store usando Qdrant."""
    
    VARIAVEIS_AMBIENTE_OBRIGATORIAS = ["QDRANT_URL"]
    MODELO_EMBEDDING = "all-MiniLM-L6-v2"
    NOME_COLLECTION = "long_term_memory"
    LIMIAR_SEMELHANCA = 0.9  # Limiar para considerar duas memórias como semelhantes

    _instancia: Optional["VectorStore"] = None
    _inicializada: bool = False
    
    def __new__(cls) -> "VectorStore":
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def __init__(self) -> None:
        if not self._inicializada:
            self._validar_variaveis_ambiente()
            self.model = SentenceTransformer(self.MODELO_EMBEDDING)
            self.client = QdrantClient(
                url=settings.QDRANT_URL
            )
            self._inicializada = True
            
    def _validar_variaveis_ambiente(self) -> None:
        """Validar que todas as variáveis de ambiente obrigatórias estão definidas."""
        ausentes = [var for var in self.VARIAVEIS_AMBIENTE_OBRIGATORIAS if not os.getenv(var)]
        if ausentes:
            raise ValueError(
                f"Variáveis de ambiente obrigatórias ausentes: {', '.join(ausentes)}"
            )
            
    def _colecao_existe(self) -> bool:
        """Verificar se a coleção de memória existe."""
        colecoes = self.client.get_collections().collections
        return any(col.name == self.NOME_COLLECTION for col in colecoes)
    
    def _criar_colecao(self) -> None:
        """Criar uma nova coleção para armazernar memórias."""
        embedding_exemplo = self.model.encode("sample text")
        self.client.create_collection(
            collection_name=self.NOME_COLLECTION,
            vectors_config=VectorParams(
                size=len(embedding_exemplo),
                distance=Distance.COSINE,
            ),
        )
        
    def localizar_memoria_similar(self, texto: str) -> Optional[Memoria]:
        """Localiza se uma memória similar já existe.

        Args:
            texto: O texto a ser procurado

        Returns:
            Optional Memoria se uma similar for encontrada
        """
        resultados = self.procurar_memorias(texto, k=1)
        if resultados and resultados[0].score >= self.LIMIAR_SEMELHANCA:
            return resultados[0]
        return None
    
    def armazenar_memoria(self, texto: str, metadata: dict) -> None:
        """Armazenar uma nova memória no Vector Store ou atualizar se uma similar existir.

        Args:
            texto: O texto com o conteúdo da memória
            metadata: Informações adicionais sobre a memória (timestamp, type, etc.)
        """
        if not self._colecao_existe():
            self._criar_colecao()
        
        # Verificar se memória semelhante existe
        memoria_similar = self.localizar_memoria_similar(texto)
        if memoria_similar and memoria_similar.id:
            metadata["id"] = memoria_similar.id  # Mantem o mesmo id para atualização

        embedding = self.model.encode(texto)
        point = PointStruct(
            id=metadata.get("id", abs(hash(texto))),
            vector=embedding.tolist(),
            payload={
                "texto": texto,
                **metadata,
            },
        )

        self.client.upsert(
            collection_name=self.NOME_COLLECTION,
            points=[point],
        )
    
    def procurar_memorias(self, query: str, k: int = 5) -> List[Memoria]:
        """Procura por memórias similares no vector store.

        Args:
            query: Texto a ser procurado
            k: Número de memórias a serem retornadas

        Returns:
            List de objetos Memoria
        """
        if not self._colecao_existe():
            return []

        query_embedding = self.model.encode(query)
        resultados = self.client.search(
            collection_name=self.NOME_COLLECTION,
            query_vector=query_embedding.tolist(),
            limit=k,
        )

        return [
            Memoria(
                texto=hit.payload["texto"],
                metadata={k: v for k, v in hit.payload.items() if k != "texto"},
                score=hit.score,
            )
            for hit in resultados
        ]
    
@lru_cache
def get_vector_store() -> VectorStore:
    """Obter ou Criar a instância singleton do VectorStore."""
    return VectorStore()
