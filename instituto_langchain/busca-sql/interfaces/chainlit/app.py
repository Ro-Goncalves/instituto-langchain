import chainlit as cl

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="Olá, Usuário Lindo, como eu lhe ajudo hoje?").send()
    
@cl.on_message
async def on_message(message: cl.Message):
    
    msg = cl.Message(content="Você disse: " + message.content)
    await msg.send()