import os, asyncio, sys
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

script_dir = os.path.dirname(os.path.abspath(__file__))
server_path = os.path.join(script_dir, "servers", "calculadora_server.py")


# Exemplo de pergunta
# * Quanto é (5 + 2) * 3?
query = input("Digite uma pergunta: ")

model = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.8,
    max_retries=2,
)

async def run_agent():
    async with MultiServerMCPClient(
        {
            "calculadora": {
                "command": sys.executable,
                "args": [server_path],
                "transport": "stdio",
            },
            "youtube_transcript": {
                "command": sys.executable,
                "args": ["instituto_langchain/mcp_adapters/servers/yt_transcript_server.py"],
                "transport": "stdio",
            },
            "file_system": {
                "command": sys.executable,
                "args": ["instituto_langchain/mcp_adapters/servers/file_system_server.py"],
                "transport": "stdio",
            },
        }
    ) as client:
        tools = client.get_tools()
        agent = create_react_agent(model, tools)

        system_message = SystemMessage(content=(
            "You have access to multiple tools, transcript tools and file system tools, that can help answer queries."
            "Use them dynamically and efficiently based on the user's request. "
        ))

        agent_response = await agent.ainvoke({
            "messages": [system_message, HumanMessage(content=query)],          
        })
        
        for m in agent_response["messages"]:
            m.pretty_print()

        return agent_response['messages'][-1].content
    
if __name__ == "__main__":
    response = asyncio.run(run_agent())
    print("\nFinal Response:", response)