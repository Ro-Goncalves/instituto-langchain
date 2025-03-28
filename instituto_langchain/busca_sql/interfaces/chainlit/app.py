import chainlit as cl

from instituto_langchain.busca_sql.graph.graph import criar_grafo_busca_sql

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="Olá, Usuário Lindo, como eu lhe ajudo hoje?").send()
    
@cl.on_message
async def on_message(message: cl.Message):

    async with cl.Step(type="run"):
        grafo = criar_grafo_busca_sql().compile()
        texto_msg = await grafo.ainvoke({"pergunta": message.content})

    msg = cl.Message(content=texto_msg["pergunta_analisada"])
    await msg.send()