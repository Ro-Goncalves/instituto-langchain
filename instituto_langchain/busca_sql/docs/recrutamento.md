# Processo: Recrutamento

>Este processo descreve as etapas genéricas desde a identificação da necessidade de contratação de um candidato.  
>Todo o contéudo foi gerado com a utilização do Gemini

## Atividades

### Abrir Vaga

**Usuário(s) responsável:**

Solicitante - Gestor da área

**Descrição do Procedimento:**

* O Requisitante acessa o formulário `Recrutamento e Seleção`.
* O Requisitante preenche as informações da vaga (Cargo, Departamento, Justificativa, Perfil desejado - hard skills e soft skills, Requisitos obrigatórios e desejáveis, Faixa salarial/Nível, Tipo de Contrato, Local de trabalho, etc.).
* O Requisitante anexa descrição detalhada do cargo, se disponível.
* O Requisitante submete o formulário para validação.

**Roteamento:**

***Aprovação - Submeter para Validação***  
Encaminha para a atividade `Validar Requisição de Vaga`

***Rejeição - Cancelar Solicitação***  
Encaminha para a atividade `Solicitação Cancelada`

**Integrações:**

* Consulta à Estrutura Organizacional (para validar Departamento/Cargo).
* Consulta ao Orçamento (para validar disponibilidade financeira).
* Sistema de RH (para buscar descrições de cargo padronizadas, se houver).

**Pontos de Atenção:**

Garantir que a descrição da vaga e os requisitos estejam claros e objetivos para evitar retrabalho e atrair os candidatos corretos. Validar a real necessidade da vaga e o orçamento disponível.

---

### Validar Requisição de Vaga

**Usuário(s) responsável:**

Gestor de RH

**Descrição do Procedimento:**

* O Usuário recebe a notificação de que a solicitação de vaga requer revisão.
* O Usuário acessa o formulário da solicitação.
* O Usuário analisa os comentários e pontos que precisam de ajuste (Ex: Detalhamento do perfil, Justificativa, Alinhamento com orçamento/estrutura).
* O Usuário adiciona comentários que podem ser sobre três situações:
  * Solicitação de ajustes no formulário de solicitação de vaga.
  * Rejeição da solicitação de vaga.
  * Aprovação da solicitação de vaga.
* De acordo com a análise do Usuário, ele escolherá uma das seguintes rotas:
  * Se aprovar: processo deve ser encaminhado para a atividade `Divulgar Vaga`.
  * Se rejeitar: processo deve ser encaminhado para a atividade `Solicitação Cancelada`.
  * Se solicitar ajustes: processo deve ser encaminhado para a atividade `Revisar Solicitação`.

**Roteamento:**

***Aprovação - Submeter para divulgação da vaga***
Encaminha para a atividade `Divulgar Vaga`

***Rejeição - Cancelar Solicitação***
Encaminha para a atividade `Solicitação Cancelada`

***Rejeição -Ressubmeter para Revisão:***
Encaminha para a atividade `Revisar Solicitação`

**Integrações:**

* Não se aplicam.

**Pontos de Atenção:**

* Garantir que o feedback da etapa anterior seja claro para o Requisitante.
* Pode haver um limite de ciclos de revisão para evitar loops infinitos.
* O Requisitante deve ter acesso fácil aos motivos da devolução da solicitação.

---

### Revisar Solicitação

**Usuário(s) responsável:**

Solicitante

**Descrição do Procedimento:**

* O Solicitante recebe a notificação indicando que a requisição de vaga foi devolvida para revisão, juntamente com os motivos/comentários do validador (RH).
* O Solicitante acessa o formulário da requisição no sistema.
* O Solicitante analisa os comentários/feedback para entender quais ajustes são necessários.
* O Solicitante realiza as modificações pertinentes nos campos da requisição (Ex: ajusta descrição do perfil, corrige informações orçamentárias, detalha justificativa).
* Após os ajustes, o Solicitante ressubmete a solicitação para uma nova validação.

**Roteamento:**

***Aprovação - Ressubmeter para Validação:***
    * Encaminha a solicitação ajustada de volta para a atividade `Validar Requisição de Vaga`.

**Integrações:**

* Não se aplicam.

**Pontos de Atenção:**

* É crucial que o feedback fornecido na etapa anterior (`Validar Requisição de Vaga`) seja claro e específico para orientar o Solicitante.
* Pode existir um limite de quantas vezes uma solicitação pode passar por este ciclo de revisão antes de ser cancelada automaticamente ou escalada.
* O Solicitante deve ter um prazo para realizar a revisão.

---

### Divulgar Vaga

**Usuário(s) responsável:**

Analista (RH)

**Descrição do Procedimento:**

* O Analista recebe a notificação de vaga aprovada.
* O Analista revisa/ajusta a descrição da vaga para publicação (tornando-a atraente para candidatos).
* O Analista define os canais de divulgação (Ex: Portal de Carreiras interno/externo, LinkedIn, Vagas.com, Catho, Indeed, Redes sociais, Indicações).
* O Analista publica a vaga nos canais selecionados.
* O Analista configura a recepção de candidaturas.
* O Analista marca a atividade como concluída.

**Roteamento:**

***Aprovação - Submeter para Triagem de Currículos:***
Encaminha para a atividade `Triagem de Currículos` (esta atividade pode iniciar automaticamente após um período ou quando um número mínimo de currículos for recebido, ou pode ser iniciada manualmente pelo recrutador).

**Integrações:**

* Plataformas de Emprego (APIs para publicação automática, Ex: LinkedIn API, Gupy, Kenoby, etc.).
* Portal de Carreiras da Empresa.
* Workflow (para centralizar as candidaturas).

**Pontos de Atenção:**

Escolher os canais mais adequados para o perfil da vaga. Monitorar o volume e a qualidade das candidaturas recebidas.

---

### Triagem de Currículos

**Usuário(s) responsável:**

Robô (IA), Analista RH, Solicitante (participação opcional)

**Descrição do Procedimento:**

***Momento 1: Pré-Triagem Automática (Robô)***

* Robô é ativado quando a vaga está em divulgação e currículos começam a chegar (via ATS/Webhook).
* Robô aplica filtros automáticos baseados nos requisitos obrigatórios definidos (formação, palavras-chave, localização, etc.).
* Robô classifica os candidatos iniciais (Ex: Compatível, Incompatível).
* Ao atingir um critério (Ex: nº mínimo de compatíveis, tempo decorrido), o Robô compila a lista de candidatos "Compatíveis" e encaminha a análise para o Analista RH.

***Momento 2: Análise Qualitativa (Analista RH)***

* Analista RH recebe a lista pré-filtrada pelo Robô.
* Analista RH revisa os perfis/currículos, avaliando requisitos desejáveis, qualidade da experiência, aderência cultural (inicial), etc.
* Analista RH refina a classificação (Ex: Aprovado para Entrevista, Aprovado - Validar com Solicitante, Stand-by, Rejeitado).
* (Ponto de Decisão 1 - Analista RH): Com base na quantidade e qualidade dos candidatos Aprovados:
  * Opção A: Se há candidatos suficientes e o processo prevê validação do gestor nesta fase -> Ir para Momento 3 (Validação).
  * Opção B: Se há candidatos suficientes e NÃO há validação do gestor nesta fase -> Ir para Momento 4 (Decisão Final).
  * Opção C: Se há POUCOS ou NENHUM candidato adequado -> Ir para Momento 1 (Análise Qualitativa).

***Momento 3: Validação Opcional (Solicitante)***

* Analista RH (se escolheu Opção A acima) compartilha a lista de candidatos (Aprovado - Validar com Solicitante) com o Solicitante.
* Solicitante analisa a lista enviada pelo Analista RH.
* Solicitante fornece seu feedback (Ex: OK para estes, remover aquele, preocupação com X).
* Solicitante devolve o feedback para o Analista RH.

***Momento 4: Decisão Final da Triagem (Analista RH)***

* Analista RH recebe o feedback do Solicitante (se aplicável - vindo do Momento 3) ou considera sua própria lista (se veio da Opção B do Momento 2).
* Analista RH consolida a lista final de candidatos que avançarão para a entrevista.
* (Ponto de Decisão 2 - Analista RH):
  * Resultado 1 (Ideal): Há candidatos suficientes e qualificados na lista final -> Encaminha para a atividade que irá abrir os processos de seleção.
  * Resultado 2 (Insuficiente, mas há esperança): Número de candidatos é baixo ou inadequado, mas acredita-se que ajustar a busca/divulgação pode trazer mais -> Decide buscar mais candidatos, volta ao momento 1.
  * Resultado 3 (Problema na origem): Número é baixo/nulo e há suspeita de que a descrição da vaga ou os critérios precisam de revisão -> devolver para `Divulgar Vaga` ou finalizar o processo encaminhando para `Triagem Cancelada`.

**Roteamento:**

***Aprovação - Atingido a Quantidade de Canditatos Desejados***
Encaminha a atividade ao Analista do RH

***Aprovação - Delegar atividade ao Solicitante***
Opcional, pode encaminhar ao solicitante para que ele também analise os currículos previamente classificados pelo Analista RH.

***Aprovação - Submeter para aguardar entrevista***
Encaminha a atividade `Abrir Processos Selecão`

***Reprovação - Processo Finalizado***
Encaminhar a atividade `Triagem Cancelada`

***Reprovação - Corrigir a descrição da vaga ou aumentar o alcance***
Encaminhar a atividade `Divulgar Vaga`

**Integrações:**

* Webhook do Workflow com sistema de captura de currículos.
* Ferramentas de IA para análise e ranqueamento de currículos (opcional).

**Pontos de Atenção:**

* Evitar vieses inconscientes na triagem.
* Garantir que os filtros automáticos (se usados) não eliminem candidatos qualificados indevidamente.
* Manter o Workflow atualizado.

---

### Abrir Processos Seleção

**Usuário(s) responsável:**

Robô (Sistema de Automação/Workflow)

**Descrição do Procedimento:**

* Esta atividade é **acionada automaticamente** quando a atividade `Triagem de Currículos` é concluída com o resultado `Prosseguir para Entrevistas` (ou similar), indicando que há uma lista final de candidatos aprovados na triagem.
* O Robô recebe a lista de IDs dos candidatos aprovados e o ID da Vaga associada.
* Para **cada ID de candidato** na lista recebida:
  * O Robô inicia uma **nova instância** do processo de negócio "Seleção de Candidato".
  * O Robô passa os dados necessários para a nova instância (Ex: ID Candidato, ID Vaga, possivelmente ID do Recrutador responsável).
* Após iniciar com sucesso todos os processos de seleção individuais, o Robô finaliza esta atividade.

**Roteamento:**

**Aprovação - Processos de Seleção Iniciados:**
Encaminha para o evento final `Recrutamento Finalizado` (marcando o fim do fluxo principal do processo de Recrutamento).

**Integrações:**

* **Sistema de Workflow:** Fundamental para receber a lista de candidatos da atividade anterior e para iniciar as novas instâncias do processo "Seleção de Candidato".
* **ATS/Banco de Dados de Candidatos:** Para buscar dados adicionais do candidato, se necessário, para passar ao processo de Seleção.

**Pontos de Atenção:**

* **Tratamento de Erros:** O que acontece se o Robô falhar ao tentar criar um ou mais processos de Seleção? É preciso haver um mecanismo de log, notificação ou retentativa.
* **Rastreabilidade:** Garantir que cada novo processo de Seleção tenha uma referência/link para o processo de Recrutamento "pai" (a requisição de vaga original) para facilitar o rastreamento e a visão consolidada.
* **Consistência de Dados:** Assegurar que os dados essenciais do candidato e da vaga sejam passados corretamente para cada novo processo de Seleção.
* **Timing:** Esta atividade deve ser rápida para não atrasar o início da fase de Seleção para os candidatos.

---

### Solicitação Cancelada, Triagem Cancelada e Recrutamento Finalizado

Essas são atividades de finalização, devem conter as informações da atividade enterior, congeladas.