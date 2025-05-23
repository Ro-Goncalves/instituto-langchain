import chainlit as cl

from instituto_langchain.le_rec_hum.graph.graph import create_sql_search_graph
from instituto_langchain.le_rec_hum.graph.utils.llm_manager import LLMManager
from langchain_core.prompts import ChatPromptTemplate

from instituto_langchain.le_rec_hum.core.prompts import (
  BRIAN_SYSTEM_PROMPT,
  BRIAN_HUMAN_PROMPT
)

LLM_MANAGER = LLMManager()

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(
        content="Hello, Beautiful User, start with the question: What is Ana Souza's case about?"
    ).send()
    
@cl.on_message
async def on_message(message: cl.Message):

    async with cl.Step(type="run"):
        graph = create_sql_search_graph().compile()
        graph_result = await graph.ainvoke({"question": message.content})

        prompt = ChatPromptTemplate.from_messages([
            ("system", BRIAN_SYSTEM_PROMPT),
            ("human", BRIAN_HUMAN_PROMPT),
        ])

        response = LLM_MANAGER.invoke(
            prompt,
            resultado_sql=graph_result['resultados'],
            pergunta=message.content
        )

    msg = cl.Message(content=response)
    await msg.send()
