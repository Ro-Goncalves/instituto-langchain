import chainlit as cl
from langchain_core.prompts import ChatPromptTemplate

from instituto_langchain.busca_sql.graph.utils.gerenciador_llm import GerenciadorLLM

llm = GerenciadorLLM()

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="Olá, Usuário Lindo, como eu lhe ajudo hoje?").send()
    
@cl.on_message
async def on_message(message: cl.Message):
    template = ChatPromptTemplate([
        ("system", "Seu nome é Brian, você está sempre feliz e alegre, sempre respondendo em PT-BR."),
        ("human", message.content),   
    ])
    texto_msg = llm.invoke(template)  
    msg = cl.Message(content=texto_msg)
    await msg.send()