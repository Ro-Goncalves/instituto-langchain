import sys
from pathlib import Path

src_path = Path(__file__).parent.parent.parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))
    
print(f"src_path: {src_path}", file=sys.stderr)

from instituto_langchain.mcp_server.server.sumarizer_server import mcp

def run():
    """Runs the MCP server using stdio transport."""
    print("Starting Summarizer MCP Server on stdio...", file=sys.stderr)
    # Carrega variáveis de ambiente do .env (se existir)
    from dotenv import load_dotenv
    load_dotenv()
    mcp.run(transport='stdio')

if __name__ == "__main__":
    run()