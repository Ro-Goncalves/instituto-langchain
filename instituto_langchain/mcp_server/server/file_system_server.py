from mcp.server.fastmcp import FastMCP
from instituto_langchain.mcp_server.configuracoes import configuracoes
import os

mcp = FastMCP("file_system")
DIRETORIO_ARQUIVOS = configuracoes.CAMINHO_ARQUIVOS

@mcp.tool(
    name="escrever_arquivo",
    description="Escreve um arquivo com o conteúdo fornecido.",
)
def escrever_arquivo(nome_arquivo: str, conteudo: str) -> str:
    
    if not os.path.exists(DIRETORIO_ARQUIVOS):
        os.makedirs(DIRETORIO_ARQUIVOS)
        
    with open(DIRETORIO_ARQUIVOS + nome_arquivo, "w") as f:
        f.write(conteudo)   
    return f"Arquivo '{DIRETORIO_ARQUIVOS + nome_arquivo}' escrito com sucesso."

if __name__ == "__main__":   
    mcp.run(transport='stdio')