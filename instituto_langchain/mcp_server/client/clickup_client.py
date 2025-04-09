import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from instituto_langchain.mcp_server.configuracoes import configuracoes

query = input("Digite uma pergunta: ")

model = ChatGroq(
    model=configuracoes.MODELO_DEEPSEEK,
    api_key=configuracoes.GROQ_API_KEY,
    temperature=0.8,
    max_retries=2,
)

async def run_agent():
    async with MultiServerMCPClient(
        {
            "ClickUp": {
                "command": "npx",
                "args": [ 
                    "-y",
                    "@taazkareem/clickup-mcp-server@latest"],
                "env": {
                    "CLICKUP_API_KEY":configuracoes.CLICKUP_API_KEY,
                    "CLICKUP_TEAM_ID":configuracoes.CLICKUP_TEAM_ID,
                },
                "transport": "stdio",
            },
        }
    ) as client:
        tools = client.get_tools()
        agent = create_react_agent(model, tools)

        system_message = SystemMessage(content=(
            "You have access to multiple tools."
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