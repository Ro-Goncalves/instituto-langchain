import logging
import sqlite3
import os

from datetime import datetime
from typing import List, Dict, Any

from instituto_langchain.le_rec_hum.settings import settings

class DatabaseManager:
    REQUIRED_ENV_VARS = ['GROQ_API_KEY']

    def __init__(self):
        """Initializes the database manager using SQLite."""
        self.logger = logging.getLogger(__name__)
        self.db_path = settings.AGENT_SQL_DB_PATH

        self.logger.info(f"Initializing DatabaseManager with database at {self.db_path}")

        self._validate_environment_variables()

        try:
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row  # Enables column name access for results
            self.logger.info("Database connection established successfully\n")
        except sqlite3.Error as e:
            self.logger.error(f"Error connecting to the database: {str(e)}\n")
            raise Exception(f"Database connection failed: {str(e)}")

    def _validate_environment_variables(self) -> None:
        missing_vars = [var for var in self.REQUIRED_ENV_VARS if not os.getenv(var)]
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

    def get_schema(self) -> str:
        """Retrieves the schema of the SQLite database."""
        self.logger.info("Fetching database schema")
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT name, sql FROM sqlite_master WHERE type='table';")
            schema_info = cursor.fetchall()

            tables_count = len(schema_info)
            self.logger.debug(f"Found {tables_count} tables in the database")

            schema = "\n".join(
                f"Table: {row['name']}\n{row['sql']}" for row in schema_info if row['sql']
            )
            self.logger.debug(f"Schema retrieved: {schema}\n")
            return schema
        except sqlite3.DatabaseError as e:
            error_msg = f"Error retrieving database schema: {str(e)}\n"
            self.logger.error(error_msg)
            raise Exception(error_msg)

    def execute_query(self, query: str) -> List[Dict[str, Any]]:
        """Executes a SQL query on the SQLite database and returns the results."""
        self.logger.info(f"Executing query: {query}")
        try:
            is_select = query.strip().lower().startswith("select")

            if not is_select:
                operation = query.strip().split("/")[0]
                self.logger.warning(f"Attempted execution of disallowed SQL operation '{operation}'")
                raise Exception(f"SQL operation '{operation}' is not allowed")

            cursor = self.connection.cursor()
            start_time = datetime.now()
            cursor.execute(query)

            results = [dict(row) for row in cursor.fetchall()]

            execution_time = (datetime.now() - start_time).total_seconds()
            self.logger.info(f"Execution time: {execution_time:.3f} seconds\n")

            return results
        except sqlite3.DatabaseError as e:
            error_msg = f"Error executing query: {str(e)}\n"
            self.logger.error(error_msg)
            raise Exception(error_msg)

    def close(self):
        """Closes the connection to the database."""
        self.logger.info("Closing database connection")
        try:
            self.connection.close()
            self.logger.info("Database connection closed successfully\n")
        except sqlite3.Error as e:
            self.logger.error(f"Error closing the database connection: {str(e)}\n")