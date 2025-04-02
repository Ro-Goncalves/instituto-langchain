import logging
import sqlite3
import os

from datetime import datetime
from typing import List, Dict, Any

from instituto_langchain.busca_sql.configuracoes import configuracoes

class GerenciadorBanco:
    VARIAVEIS_OBRIGATORIA = ['GROQ_API_KEY']
    
    def __init__(self):
        """Inicializa o gerenciador de banco de dados com SQLite."""
        self.logger = logging.getLogger(__name__)
        self.db_path = configuracoes.CAMINHO_BANCO_AGENTE_SQL

        self.logger.info(f"Inicializando DatabaseManager com banco de dados em {self.db_path}")

        self._validar_variaveis()

        try:
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row  # Permite acessar os resultados por nome de coluna
            self.logger.info("Conexão com o banco de dados estabelecida com sucesso\n")
        except sqlite3.Error as e:
            self.logger.error(f"Erro ao conectar ao banco de dados: {str(e)}\n")
            raise Exception(f"Falha na conexão com o banco de dados: {str(e)}")

    def _validar_variaveis(self) -> None:
        variaveis_faltantes = [var for var in self.VARIAVEIS_OBRIGATORIA if not os.getenv(var)]
        if variaveis_faltantes:
            raise ValueError(f"Variáveis obrigatórias ausentes: {', '.join(variaveis_faltantes)}")
        
    def get_schema(self) -> str:
        """Recupera o esquema do banco de dados SQLite."""
        self.logger.info("Obtendo esquema do banco de dados")
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT name, sql FROM sqlite_master WHERE type='table';")
            schema_info = cursor.fetchall()
            
            tables_count = len(schema_info)
            self.logger.debug(f"Encontradas {tables_count} tabelas no banco de dados")
            
            schema = "\n".join(f"Table: {row['name']}\n{row['sql']}" for row in schema_info if row['sql'])
            self.logger.debug(f"Esquema obtido: {schema}\n")
            return schema
        except sqlite3.DatabaseError as e:
            error_msg = f"Erro ao obter o esquema do banco de dados: {str(e)}\n"
            self.logger.error(error_msg)
            raise Exception(error_msg)

    def execute_query(self, query: str) -> List[Dict[str, Any]]:
        """Executa uma query SQL no banco SQLite e retorna os resultados."""
       
        self.logger.info(f"Executando query: {query}")
        
        try:
            is_select = query.strip().lower().startswith("select")
            
            if not is_select:
                operacao = query.strip().split("/")[0]
                self.logger.warning(f"Tentativa de execução de operação SQL '{operacao}' não permitida")
                raise Exception(f"Operação SQL '{operacao}' não permitida")
            
            cursor = self.connection.cursor()
            start_time = datetime.now()
            cursor.execute(query)
            
            results = [dict(row) for row in cursor.fetchall()]           
            
            execution_time = (datetime.now() - start_time).total_seconds()
            self.logger.info(f"Tempo de execução: {execution_time:.3f} segundos\n")

            return results
        except sqlite3.DatabaseError as e:
            error_msg = f"Erro ao executar a consulta: {str(e)}\n"
            self.logger.error(error_msg)            
            raise Exception(error_msg)

    def close(self):
        """Fecha a conexão com o banco de dados."""
        self.logger.info("Fechando conexão com o banco de dados")
        try:
            self.connection.close()
            self.logger.info("Conexão com o banco de dados fechada com sucesso\n")
        except sqlite3.Error as e:
            self.logger.error(f"Erro ao fechar a conexão com o banco de dados: {str(e)}\n")