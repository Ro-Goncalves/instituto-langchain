# 📄 Documento de Requisitos — **Sistema de Análise de Código com Agentes de IA**

## 🧠 Objetivo Geral

Desenvolver um sistema de IA baseado em agentes, orquestrados com LangGraph, capaz de realizar **code reviews automatizados** em projetos Java, com foco na **camada de domínio**. O sistema será utilizado inicialmente para validar a implementação de requisitos exigidos, e futuramente será integrado ao VS Code como um assistente de revisão técnica.

## ⚙️ Funcionamento Geral

O sistema será iniciado como uma aplicação via **Streamlit** e receberá como entrada arquivos Java. Utilizando LLMs via API, ele aplicará um **script de análise de código** previamente configurado para gerar relatórios de revisão técnica com sugestões, críticas e elogios. Os relatórios serão exportados em Markdown e organizados por classe analisada.

## 🔁 Fluxo de Funcionamento

### 1. **Entrada**

- Tipo: Arquivos `.java` (ou blocos de código colados na interface)
- Escopo inicial: Um **método** implementado na `controler`
- Requisitos:
  - Organização por pacotes (ex: `domain`, `application`, `infrastructure`)
  - Possibilidade de múltiplos arquivos por análise
  - Leitura de dependências entre classes e interfaces

### 2. **Análise (via LLM + Agentes)**

- O código será analisado por um ou mais agentes especializados, coordenados via LangGraph:
  - **Agente Leitor**: identifica estrutura, pacotes, importações e dependências
  - **Agente Avaliador**: aplica o *script de análise* com foco em:
    - Boas práticas de codificação (Java, OO, DDD)
    - Nomeclatura
    - Complexidade dos métodos
    - Coesão e acoplamento
    - Conformidade com padrões da arquitetura (Ports & Adapters)
  - **Agente de Contexto**: identifica relações entre arquivos da camada
  - **Agente de Relatório**: gera saída formatada em Markdown

> ⚠️ O prompt de análise será definido pelo usuário e poderá ser atualizado iterativamente conforme os testes evoluem.

### 3. **Saída**

- Arquivo `.md` com a análise técnica estruturada

## 🔧 Tecnologias e Infraestrutura

| Recurso               | Escolha                       |
|-----------------------|-------------------------------|
| LLM                   | Via API externa (Gemini)      |
| Framework de Agentes  | LangGraph                     |
| Interface Inicial     | Streamlit                     |
| Interface Futura      | MCP para VS Code              |
| Formato de Saída      | Markdown (`.md`)              |

## 🧪 Cenários de Uso

1. **Verificar implementação de requisitos**
   - Input: Classes criadas para atender a um requisito
   - Output: Avaliação crítica da aderência do código aos princípios e práticas esperadas

2. **Code review geral da camada de domínio**
   - Input: Pacote completo de domínio (`domain.*`)
   - Output: Relatório geral por classe, com insights sobre estrutura e coesão

3. **Análise de impacto entre arquivos**
   - O sistema deve conseguir analisar arquivos relacionados, entendendo dependências para avaliar acoplamento e design.

## 📌 Restrições e Considerações

- O sistema **não terá limite de tamanho** dos arquivos de entrada, mas pode segmentar o código internamente se necessário para respeitar o limite do contexto da LLM.
- A análise **não será apenas estática**, mas **contextual**, considerando interdependência entre as classes da camada.
- O prompt de análise será **personalizável**, mas deve seguir um esqueleto base para manter a padronização dos relatórios.

## ✅ Próximos Passos

1. Definir arquitetura inicial no LangGraph
2. Gerar primeiro agente de leitura + formatação
3. Iterar com o prompt atual, ajustando o agente de avaliação
4. Implementar Streamlit com upload de arquivos
