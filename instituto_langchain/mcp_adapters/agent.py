import os, asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

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
                "command": "python",
                "args": ["instituto_langchain/mcp_adapters/servers/calculadora_server.py"],
                "transport": "stdio",
            }
        }
    ) as client:
        tools = client.get_tools()
        agent = create_react_agent(model, tools)

        system_message = SystemMessage(content=(
            "You have access to multiple tools that can help answer queries."
            "Use them dynamically and efficiently based on the user's request. "
        ))

        agent_response = await agent.ainvoke({"messages": [system_message, HumanMessage(content=query)]})
        
        for m in agent_response["messages"]:
            m.pretty_print()

        return agent_response['messages'][-1].content
    
if __name__ == "__main__":
    response = asyncio.run(run_agent())
    print("\nFinal Response:", response)