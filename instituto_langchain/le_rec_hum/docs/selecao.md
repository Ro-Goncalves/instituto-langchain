# Processo: Seleção de Candidato

> Este processo descreve as etapas genéricas desde o momento em que um candidato pré-selecionado entra na fase de avaliação ativa até a decisão final de contratação ou rejeição. Ele opera individualmente para cada candidato aprovado na triagem.  
> >
>**Todo o contéudo foi gerado com a ajuda do Gemini, modelo 2.5 Pro(experimental).**

## Atividades

### Agendar Entrevista Inicial

**Usuário(s) responsável:**

Analista RH

**Descrição do Procedimento:**

* Esta atividade é iniciada automaticamente pela atividade `Abrir Processos Seleção` do processo de Recrutamento.
* Uma Integração recebe os dados do candidato (ID, informações básicas) e da vaga (ID, Gestor Solicitante, Analista RH responsável).
* O Sistema atribui formalmente o candidato ao Analista RH responsável pela condução da seleção para aquela vaga.
* O Analista RH é notificado que um novo candidato está pronto para iniciar as etapas de seleção.
* O Analista RH agendado o horário da entrevista inicial e envia o convite para o candidato.
* O Analista RH atualiza o formulário com as informações da entrevista.
* Caso o candidato aceite a entrevista, o processo desse aguardar até que a entrevista aconteça.
* Caso o candidato não aceite, ou o Analista RH não consiga fazer contato com ele, o processo deve ser finalizado.

**Roteamento:**

***Aprovação - Entrevista Agendada***  
Encaminha para a atividade `Realizar Entrevista Inicial`

***Reprovação - Processo Finalizado***  
Encaminha para a atividade `Entrevista Inicial Rejeitada`

**Integrações:**

* **Sistema de Workflow:** Recebe dados do processo de Recrutamento.
* **ATS (Applicant Tracking System):** Para buscar/atualizar o status do candidato.
* **Ferramenta de Agenda:** (Ex: Google Calendar, Outlook Calendar) para verificar disponibilidade e enviar convites.
* **Plataforma de Videoconferência:** (Ex: Google Meet, Zoom, Teams) para gerar links.

**Pontos de Atenção:**

* Garantir que a transição entre o processo de Recrutamento e Seleção seja fluida e sem perda de dados.
* O Analista RH deve ter acesso rápido ao currículo e informações da triagem.

---

### Realizar Entrevista Inicial

**Usuário(s) responsável:**

Entrevistador de RH

**Descrição do Procedimento:**

* A atividade deve hibernar até dois dias antes da entrevista.
* O Entrevistador do RH conduz a entrevista com o candidato (presencial, telefone ou vídeo).
* O Entrevistador avalia aspectos comportamentais (soft skills), alinhamento cultural, entendimento da vaga, histórico profissional e pretensão salarial.
* O Entrevistador apresenta a empresa e a vaga ao candidato, esclarece dúvidas.
* O Entrevistador registra o feedback/parecer sobre o candidato no formulário.
* O Entrevistador decide se o candidato avança no processo.

**Roteamento:**

***Aprovar Candidato:***  
Encaminha para a atividade `Agendar Entrevista e Avaliação Técnica`.

***Reprovar Candidato:***  
Encaminha para a atividade `Rejeitado na Entrevista Inicial`.

**Integrações:**

* ATS (para registrar feedback e atualizar status).
* Plataforma de Videoconferência.

**Pontos de Atenção:**

* Manter um roteiro de entrevista estruturado para garantir comparabilidade. Focar em perguntas situacionais e comportamentais. Registrar o feedback logo após a entrevista.

---

### Agendar Entrevistas e Avaliações Técnica

**Usuário(s) responsável:**

Analista RH

**Descrição do Procedimento:**

* O Analista RH recebe a notificação de que o candidato foi aprovado na entrevista inicial e deve prosseguir para as próximas etapas.
* **Alinhamento:** O Analista RH confirma com o Gestor Solicitante (ou consulta a definição da vaga) quais avaliações e entrevistas específicas são necessárias para esta fase (Ex: teste técnico online, case prático, entrevista técnica, entrevista comportamental/fit com gestor, painel com equipe). Define quem serão os entrevistadores/avaliadores.
* **Verificação de Disponibilidade Interna:** O Analista RH consulta as agendas dos entrevistadores/avaliadores internos para identificar possíveis horários.
* **Contato com Candidato:** O Analista RH entra em contato com o candidato para:
  * Informar sobre as próximas etapas (tipos de entrevista/avaliação).
  * Propor datas e horários compatíveis com a disponibilidade interna.
* **Confirmação ou Recusa:**
  * **Se o candidato confirmar** a disponibilidade para as datas/horários propostos:
    * O Analista RH formaliza o agendamento enviando os convites (via ferramenta de agenda) para o candidato e entrevistadores/avaliadores, incluindo links de videoconferência (se aplicável) e qualquer instrução necessária.
    * O Analista RH atualiza o status do candidato e registra os detalhes do agendamento no formulário do processo.
    * O processo avança para a próxima etapa (`Realizar Entrevista e Avaliação Técnica`).
  * **Se o candidato recusar** as opções, não responder após um número razoável de tentativas (definir política interna, ex: 3 tentativas em 48h), ou desistir do processo:
    * O Analista RH registra o motivo no formulário.
    * O processo é finalizado.

**Roteamento:**

***Aprovação - Agendamento Confirmado***  
Encaminha para a atividade `Realizar Entrevista e Avaliação Técnica`.

***Rejeição - Não Agendado / Desistência***  
Encaminha para a atividade `Entrevista e Avalição Técnica Cancelada` (para formalizar o encerramento da participação do candidato no processo).

**Integrações:**

* **ATS (Applicant Tracking System):** Para buscar dados do candidato, registrar o status do agendamento (confirmado, falhou), e armazenar detalhes das entrevistas/avaliações agendadas.
* **Ferramenta de Agenda:** (Ex: Google Calendar, Outlook Calendar) para verificar disponibilidade interna e enviar os convites formais para todos os participantes.
* **Plataforma de Videoconferência:** (Ex: Google Meet, Zoom, Teams) para gerar e incluir os links nos convites, se aplicável.
* **E-mail/Comunicação:** Para o contato inicial com o candidato para propor horários.

**Pontos de Atenção:**

* **Clareza na Comunicação:** Ser claro com o candidato sobre quais etapas serão realizadas, a duração estimada e com quem ele irá interagir.
* **Flexibilidade:** Oferecer, se possível, mais de uma opção de horário ao candidato.
* **Tempo de Resposta:** Definir um prazo máximo para o candidato responder às tentativas de agendamento.
* **Disponibilidade:** Garantir a confirmação da disponibilidade de *todos* os entrevistadores/avaliadores internos antes de propor ao candidato.
* **Profissionalismo:** Manter uma comunicação ágil e profissional, mesmo em caso de recusa ou desistência do candidato.
* **Registro:** Assegurar que todos os agendamentos (e tentativas/falhas) sejam devidamente registrados no ATS ou sistema de controle.

---

### Realizar Entrevistas e Avaliações Técnica

**Usuário(s) responsável:**

Gestor Solicitante, Avaliadores Técnicos, (Analista RH como suporte/coordenador)

**Descrição do Procedimento:**

* **Ativação:** A tarefa é ativada no sistema para os responsáveis (Gestor, Avaliadores) pouco antes da data/hora agendada para a entrevista/avaliação (Ex: 1-2 dias antes, ou no próprio dia). O sistema pode enviar lembretes.
* **Condução:** Os entrevistadores/avaliadores designados conduzem as sessões (entrevista técnica, comportamental, apresentação de case, teste prático, etc.) conforme planejado e agendado na etapa anterior.
* **Registro de Feedback:** **Imediatamente após** cada sessão (ou o mais breve possível), cada entrevistador/avaliador acessa o sistema (formulário do workflow) e registra suas percepções de forma estruturada:
  * Pontos fortes e fracos observados.
  * Respostas a perguntas chave ou desempenho em tarefas.
  * Avaliação de competências técnicas e/ou comportamentais.
  * Recomendações (Ex: pontuação, parecer descritivo).
  * Anexo de materiais relevantes (Ex: código de teste, anotações, resultado de avaliação online, se não integrado automaticamente).
* **Consolidação (Opcional/Analista RH):** O Analista RH pode verificar se todos os feedbacks foram submetidos e consolidar as informações, se necessário, para facilitar a decisão.
* **Decisão da Etapa:** Com base nos feedbacks registrados, toma-se a decisão referente a esta fase: o candidato demonstrou ter o perfil técnico e/ou comportamental esperado?
  * **Sim (Aprovar):** O candidato é considerado apto e será contratado.
  * **Não (Rejeitar):** O candidato não atendeu aos requisitos avaliados nesta etapa.

**Roteamento:**

***Aprovação - Recomendado para Contratação***  
Encaminha para a atividade `Proposta e Formalização da Contratação`.

***Rejeição - Não Recomendado***  
Encaminha para a atividade `Rejeitado na Entrevista e Avaliação Técnica`.

**Integrações:**

* **ATS (Applicant Tracking System):** Essencial para registrar os feedbacks detalhados, pontuações, pareceres e a decisão desta etapa (Aprovado/Reprovado na fase técnica/gestor).
* **Plataformas de Avaliação Online:** Para buscar resultados de testes técnicos ou comportamentais, idealmente de forma automática.
* **Ferramenta de Agendamento/Calendário:** Como referência da data/hora/participantes da avaliação realizada.
* **Sistema de Workflow:** Para gerenciar a tarefa, coletar os formulários de feedback e executar o roteamento.

**Pontos de Atenção:**

* **Pontualidade e Qualidade do Feedback:** É crucial que os avaliadores registrem seus feedbacks rapidamente após a interação, enquanto as impressões estão frescas, e de forma clara e objetiva.
* **Padronização:** Usar formulários ou critérios de avaliação padronizados para garantir consistência entre diferentes avaliadores e candidatos.
* **Experiência do Candidato:** Garantir uma experiência positiva para o candidato durante as entrevistas e avaliações, sendo profissional e respeitoso.
* **Comunicação Interna:** Assegurar que todos os avaliadores entendam como e onde registrar seus feedbacks.
* **Hibernação/Ativação:** O controle de tempo para ativação da tarefa ajuda a organizar o trabalho dos avaliadores, mas o registro do feedback deve ocorrer logo após a avaliação, independentemente da ativação prévia.

---

### Proposta e Formalização da Contratação

**Usuário(s) responsável:**

Analista RH

**Descrição do Procedimento:**

O Analista RH gerencia esta atividade atualizando o **status** no formulário do Workflow conforme o progresso:

**Início:**  
A atividade é iniciada após a decisão final de contratar (`Tomar Decisão Final`).

* **(Status: Em Elaboração)** O Analista RH reúne todas as informações validadas (cargo, salário, benefícios, data de início, etc.) e elabora a minuta da proposta/contrato oficial.

**Aprovações Internas (Se aplicável):**  

* **(Status: Aguardando Aprovações Internas)** Se a política da empresa exigir aprovações (Ex: Gestor da Área, Diretor, Financeiro), o Analista RH submete a minuta para validação através do fluxo apropriado (pode ser um sub-processo ou tarefa paralela). O Workflow aguarda o retorno.
* *Se Rejeitada Internamente:* O processo pode ser cancelado (Status: `Cancelada - Interna`) ou retornar para ajuste (Status: `Em Elaboração`), dependendo da configuração. Para simplificar, consideraremos que uma rejeição aqui leva ao cancelamento.
* *Se Aprovada Internamente:* O status avança.

**Envio ao Candidato:**

* **(Status: Aguardando Envio ao Candidato)** Com a proposta pronta e aprovada internamente (ou se não houver aprovação necessária).
* **(Status: Enviada / Aguardando Resposta Candidato)** O Analista RH envia a proposta formal ao candidato pelo canal definido (Ex: E-mail, Plataforma ATS, Ferramenta de E-signature) e define um prazo para resposta/assinatura. O Workflow aguarda a ação do candidato ou o fim do prazo.

**Resposta do Candidato:**

* *Se o Candidato Rejeitar ou Contrapropor (e não for aceito):* O Analista RH atualiza o status para **(Status: Cancelada - Recusada pelo Candidato)**.
* *Se o Candidato Não Responder no Prazo:* O Analista RH atualiza o status para **(Status: Cancelada - Sem Retorno)**.
* *Se o Candidato Aceitar (Verbalmente/Email):* O Analista RH pode atualizar para **(Status: Aceita / Aguardando Assinatura)** e prossegue para a coleta da assinatura formal.

**Assinatura do Contrato:**

* O Analista RH gerencia o processo de assinatura (digital via plataforma ou coleta física).
* **(Status: Assinada / Em Verificação)** Assim que o documento assinado é recebido (upload no workflow, notificação da plataforma de e-signature), o Analista RH verifica a conformidade e autenticidade da assinatura.

**Conclusão:**

* *Se Assinatura OK:* O Analista RH atualiza o status final para **(Status: Concluída - Assinada)** e aprova a atividade no Workflow.
* *Se Houver Problema na Assinatura/Verificação:* Pode retornar a um status anterior ou ser cancelado, dependendo do problema.

**Roteamento:**

***Aprovação - Proposta Assinada e Verificada*** (Disparado quando o Status final é `Concluída - Assinada`)  
Encaminha para a atividade `Disparar Processo de Admissão`.

***Rejeição - Proposta Não Concretizada*** (Disparado quando o Status final é `Cancelada - Interna`, `Cancelada - Recusada pelo Candidato` ou `Cancelada - Sem Retorno`)  
Encaminha para a atividade `Proposta Rejeitada`.

**Integrações:**

* **ATS (Applicant Tracking System):** Para registrar cada status da proposta, armazenar o documento final e atualizar o status geral do candidato.
* **Sistema de RH (HRIS):** Consulta de dados para elaboração da proposta; pode receber a informação final para iniciar a pré-admissão.
* **Plataforma de Assinatura Eletrônica (E-signature):** (Ex: DocuSign, Clicksign, ZapSign) Para envio, acompanhamento e recebimento do documento assinado digitalmente.
* **Sistema de Workflow:** Fundamental para gerenciar os status, tarefas, prazos e roteamento.
* **Mecanismo de Aprovação Interna:** (Pode ser dentro do Workflow ou um sistema separado).

**Pontos de Atenção:**

* **Clareza dos Status:** Garantir que os status no Workflow sejam claros e que o Analista RH os atualize corretamente a cada etapa.
* **Prazos:** Gerenciar os prazos para aprovações internas, resposta do candidato e assinatura.
* **Conformidade Legal:** Assegurar que a proposta/contrato esteja em conformidade com a legislação trabalhista e as políticas da empresa.
* **Comunicação:** Manter o candidato informado sobre o status da proposta, especialmente se houver demoras nas aprovações internas.
* **Segurança da Informação:** Cuidado ao manusear dados sensíveis do candidato e da empresa durante a elaboração e envio da proposta.
* **Versionamento:** Controlar as versões do documento caso haja ajustes durante as aprovações ou negociações.

---

### Disparar Processo de Admissão

**Usuário(s) responsável:**

Robô (Sistema de Automação/Workflow)

**Descrição do Procedimento:**

* Esta atividade é acionada automaticamente após a conclusão bem-sucedida da atividade `Proposta e Formalização da Contratação` (Status: `Concluída - Assinada`).
* O Robô coleta os dados essenciais do candidato e da contratação que foram confirmados no processo de Seleção (Ex: ID do Candidato, ID da Vaga, Cargo, Salário Aprovado, Data de Início, Gestor, Centro de Custo, Dados Pessoais básicos coletados).
* O Robô **inicia uma nova instância** do processo de negócio `Admissão de Colaborador`.
* O Robô passa os dados coletados como parâmetros iniciais para o novo processo de Admissão.
* O Robô registra o ID da nova instância do processo de Admissão no processo de Seleção atual para fins de rastreabilidade.

**Roteamento:**

***Aprovação - Finalização do Processo***  
Encaminha a atividade `Seleção Finalizada`.

**Integrações:**

* **Sistema de Workflow:** Fundamental para:
  * Receber o gatilho da atividade anterior.
  * Ler os dados necessários do processo de Seleção.
  * Iniciar a nova instância do processo Admissão de Colaborador.
  * Passar os dados para o novo processo.
* **ATS (Applicant Tracking System):** Pode ser consultado para obter dados complementares do candidato, se necessário.
* **Sistema de RH (HRIS):** Pode ser o sistema onde o processo de Admissão é efetivamente executado, recebendo os dados via integração com o Workflow.

**Pontos de Atenção:**

* **Mapeamento de Dados:** Garantir que todos os dados necessários para iniciar a Admissão sejam corretamente mapeados e transferidos.
* **Tratamento de Erros:** Prever o que acontece se o Robô falhar ao tentar iniciar o processo de Admissão (Ex: log de erro, notificação para o RH, tentativa de retentativa).
* **Rastreabilidade:** Assegurar que seja fácil navegar entre o processo de Seleção finalizado e o processo de Admissão recém-criado.
* **Timing:** A execução deve ser rápida para não atrasar o início formal da admissão.

---

### Atividades de Finalização por Rejeição

**Nomes:** `Entrevista Inicial Cancelada`, `Entrevista e Avalição Técnica Cancelada`, `Proposta Rejeitada`, `Rejeitado na Entrevista Inicial`, `Rejeitado na Entrevista e Avaliação Técnica`.

**Usuário(s) responsável:**

Robô (Sistema de Automação/Workflow)

**Descrição do Procedimento:**

* Estas atividades são eventos finais do processo, acionados quando uma rota de rejeição.
* O Robô captura um "snapshot" (uma cópia congelada) das informações relevantes do processo no momento da finalização (Ex: dados da vaga, dados do candidato, etapa da rejeição, motivo registrado, feedbacks relevantes se aplicável).
* **Todos os campos de dados nesta atividade são marcados como somente leitura (bloqueados)**, servindo como um registro histórico final do motivo e do momento da saída do candidato do processo de seleção.
* O status final do candidato no ATS é confirmado como "Rejeitado" (ou status específico da rejeição).

**Roteamento:**

Estas são atividades finais, não possuem roteamento de saída para outras atividades dentro deste processo. Elas encerram o fluxo para este candidato.

**Integrações:**

* Sistema de Workflow: Responsável por receber o fluxo das etapas anteriores, congelar os dados no formulário final e encerrar a instância do processo.
* ATS (Applicant Tracking System): Confirmação/atualização final do status do candidato.

**Pontos de Atenção:**

* **Consistência dos Dados:** Garantir que os dados "congelados" reflitam com precisão o estado do processo no momento da rejeição.
* **Clareza do Motivo:** O motivo da rejeição, registrado na etapa anterior, deve estar claramente visível neste registro final.
* **Não Edição:** Assegurar que os dados nesta atividade final não possam ser alterados após a conclusão

---

### Seleção Finalizada

**Usuário(s) responsável:**

Robô (Sistema de Automação/Workflow)

**Descrição do Procedimento:**

* Esta é a atividade final do processo para os casos de sucesso, acionada após a atividade `Disparar Processo de Admissão` ser concluída com êxito.
* O Robô captura um "snapshot" das informações finais do processo de seleção (dados da vaga, dados do candidato contratado, ID do processo de Admissão iniciado, principais marcos alcançados).
* **Todos os campos de dados nesta atividade são marcados como somente leitura (bloqueados)**, servindo como um registro histórico final da conclusão bem-sucedida da seleção.
* O status final do candidato no ATS é confirmado como "Contratado" ou "Admissão Iniciada".

**Roteamento:**

Esta é uma atividade final, não possui roteamento de saída. Ela encerra o fluxo do processo de Seleção para este candidato.

**Integrações:**

* **Sistema de Workflow:** Responsável por receber o fluxo da atividade Disparar Processo de Admissão, congelar os dados no formulário final e encerrar a instância do processo de Seleção.
* **ATS (Applicant Tracking System):** Confirmação/atualização final do status do candidato.

**Pontos de Atenção:**

* **Link para Admissão:** O ID ou link para o processo de Admissão iniciado deve estar claramente registrado para rastreabilidade.
* **Consistência dos Dados:** Garantir que os dados finais reflitam a conclusão bem-sucedida.
* **Não Edição:** Assegurar que os dados não possam ser alterados após a conclusão.
