import chainlit as cl

def agente_joao(msg):
    return f"João responde: {msg}"

def agente_maria(msg):
    return f"Maria responde: {msg}"

AGENTES = {
    "joao": agente_joao,
    "maria": agente_maria
}


@cl.on_message
async def handle_message(message: cl.Message):
    content = message.content.strip()
    
    if content.startswith("@"):
        parts = content.split(" ", 1)
        agent_tag = parts[0][1:]  # Remove o "@"
        msg_body = parts[1] if len(parts) > 1 else ""
        
        if not msg_body:
            await cl.Message(content=f"Você mencionou @{agent_tag}, mas não escreveu uma mensagem.").send()
            return

        agent = AGENTES.get(agent_tag)
        if agent:
            response = agent(msg_body)
        else:
            response = f"Agente @{agent_tag} não encontrado."

        await cl.Message(content=response).send()
    else:
        await cl.Message(content="Por favor, mencione um agente com @NomeAgente.").send()
