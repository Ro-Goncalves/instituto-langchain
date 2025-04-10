from typing import Dict, Any, TypedDict, List, Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from instituto_langchain.automatize_me.agents.prompts.code_review_prompts import (
    CODE_READER_SYSTEM_PROMPT,
    QUALITY_REVIEW_SYSTEM_PROMPT,
    DESIGN_REVIEW_SYSTEM_PROMPT,
    REPORT_GENERATOR_SYSTEM_PROMPT
)
from instituto_langchain.automatize_me.configuracoes import configuracoes
from instituto_langchain.automatize_me.agents.utils.gerenciador_modelo import GerenciadorModelo

# Definir a estrutura do estado
class RevisorCodigoState(TypedDict):
    code_files: Dict[str, str]  # Arquivos de código a serem analisados
    code_structure: Dict  # Estrutura identificada pelo agente leitor
    quality_review: Dict  # Resultados da análise de qualidade
    design_review: Dict  # Resultados da análise de design
    final_report: str  # Relatório final

# Implementação dos nós do grafo
class RevisorCodigoGraph:
    def __init__(self):
        self.logger = configuracoes.LOGGER
        self.gerenciador_modelo = GerenciadorModelo()
        self.graph = self._build_graph()
    
    def _build_graph(self):
        # Criar o grafo
        graph = StateGraph(RevisorCodigoState)
        
        # Adicionar nós
        graph.add_node("code_reader", self.code_reader_agent)
        graph.add_node("quality_reviewer", self.quality_reviewer_agent)
        graph.add_node("design_reviewer", self.design_reviewer_agent)
        graph.add_node("report_generator", self.report_generator_agent)
        
        # Definir fluxo
        graph.add_edge("code_reader", "quality_reviewer")
        graph.add_edge("quality_reviewer", "design_reviewer")
        graph.add_edge("design_reviewer", "report_generator")
        graph.add_edge("report_generator", END)
        
        # Compilar
        return graph.compile()
    
    async def code_reader_agent(self, state: RevisorCodigoState) -> RevisorCodigoState:
        """Agente que lê o código e identifica sua estrutura"""
        llm = self.gerenciador_modelo.obter_llm_deepseek()
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", CODE_READER_SYSTEM_PROMPT),
            ("human", "Analise os seguintes arquivos e identifique sua estrutura:\n{code_files}")
        ])
        
        chain = prompt | llm
        response = await chain.ainvoke({"code_files": state["code_files"]})
        
        return {"code_structure": response.content}
    
    async def quality_reviewer_agent(self, state: RevisorCodigoState) -> RevisorCodigoState:
        """Agente que avalia a qualidade do código"""
        llm = self.gerenciador_modelo.obter_llm_deepseek()
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", QUALITY_REVIEW_SYSTEM_PROMPT),
            ("human", "Analise a qualidade do seguinte código:\n{code_files}\nEstrutura identificada: {code_structure}")
        ])
        
        chain = prompt | llm
        response = await chain.ainvoke({
            "code_files": state["code_files"],
            "code_structure": state["code_structure"]
        })
        
        return {"quality_review": response.content}
    
    async def design_reviewer_agent(self, state: RevisorCodigoState) -> RevisorCodigoState:
        """Agente que avalia o design da implementação"""
        llm = self.gerenciador_modelo.obter_llm_deepseek()
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", DESIGN_REVIEW_SYSTEM_PROMPT),
            ("human", "Analise o design da seguinte implementação:\n{code_files}\nEstrutura identificada: {code_structure}")
        ])
        
        chain = prompt | llm
        response = await chain.ainvoke({
            "code_files": state["code_files"],
            "code_structure": state["code_structure"]
        })
        
        return {"design_review": response.content}
    
    async def report_generator_agent(self, state: RevisorCodigoState) -> RevisorCodigoState:
        """Agente que gera o relatório final"""
        llm = self.gerenciador_modelo.obter_llm_deepseek()
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", REPORT_GENERATOR_SYSTEM_PROMPT),
            ("human", "Gere um relatório baseado nas análises:\nQualidade: {quality_review}\nDesign: {design_review}")
        ])
        
        chain = prompt | llm
        response = await chain.ainvoke({
            "quality_review": state["quality_review"],
            "design_review": state["design_review"]
        })
        
        return {"final_report": response.content}
    
    async def executar_review(self, code_files: Dict[str, str]) -> str:
        """Executa o fluxo completo de análise de código"""
        # Estado inicial
        initial_state = {"code_files": code_files}
        
        # Executar o grafo
        final_state = await self.graph.ainvoke(initial_state)
        
        # Retornar o relatório final
        return final_state["final_report"]