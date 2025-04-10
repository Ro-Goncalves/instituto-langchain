
from typing import Dict
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, SystemMessage

from instituto_langchain.automatize_me.agents.prompts.code_review_prompts import (
    CODE_REVIEW_SYSTEM_PROMPT, 
    CODE_REVIEW_USER_PROMPT
)
from instituto_langchain.automatize_me.configuracoes import configuracoes
from instituto_langchain.automatize_me.agents.utils.gerenciador_modelo import GerenciadorModelo

class CodeReviewAgent:
    def __init__(self):
        self.logger = configuracoes.LOGGER
        self.gerenciador_modelo = GerenciadorModelo()

    async def executar_agente_review(self, controller, facade, services, infrastructure) -> Dict[str, str]:
        systemMessage = SystemMessage(content=CODE_REVIEW_SYSTEM_PROMPT)
        humanMessage = HumanMessage(content=CODE_REVIEW_USER_PROMPT, additional_kwargs={"controller": controller, "facade": facade, "services": services, "infrastructure": infrastructure})
        
        code_review_agent = create_react_agent(
            model=self.gerenciador_modelo.obter_llm_deepseek(),
            name="CodeReviewAgent"           
        )

        retorno_agente = await code_review_agent.ainvoke({"messages": [systemMessage, humanMessage]})

        return {"review": retorno_agente['messages'][-1].content}   