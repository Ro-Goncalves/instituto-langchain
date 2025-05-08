import chainlit as cl

from instituto_langchain.busca_sql.graph.graph import criar_grafo_busca_sql
from instituto_langchain.busca_sql.graph.utils.gerenciador_llm import GerenciadorLLM
from langchain_core.prompts import ChatPromptTemplate

from instituto_langchain.busca_sql.core.prompts import (
  BRIAN_SYSTEM_PROMPT,
  BRIAN_HUMAN_PROMPT
)

GERENCIADOR_LLM = GerenciadorLLM()

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="Olá, Usuário Lindo, inicie com a pergunta: Do que se trata o processo da Ana Souza?").send()
    
@cl.on_message
async def on_message(message: cl.Message):

    async with cl.Step(type="run"):
        grafo = criar_grafo_busca_sql().compile()
        resultado_grafo = await grafo.ainvoke({"pergunta": message.content})

        prompt = ChatPromptTemplate.from_messages([
            ("system", BRIAN_SYSTEM_PROMPT),
            ("human", BRIAN_HUMAN_PROMPT),
        ])

        resposta = GERENCIADOR_LLM.invoke(prompt, resultado_sql=resultado_grafo['resultados'], pergunta=message.content)

    msg = cl.Message(content=resposta)
    await msg.send()