# Processo: Seleção de Candidato

> Este processo descreve as etapas genéricas desde o momento em que um candidato pré-selecionado entra na fase de avaliação ativa até a decisão final de contratação ou rejeição. Ele opera individualmente para cada candidato aprovado na triagem.
>Todo o contéudo foi gerado com a ajuda do Gemini, modelo 2.5 Pro(experimental).

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

Recrutador (RH), Entrevistador de RH

**Descrição do Procedimento:**

* A atividade deve hibernar até dois dias antes da entrevista.
* O Entrevistador do RH conduz a entrevista com o candidato (presencial, telefone ou vídeo).
* O Entrevistador avalia aspectos comportamentais (soft skills), alinhamento cultural, entendimento da vaga, histórico profissional e pretensão salarial.
* O Entrevistador apresenta a empresa e a vaga ao candidato, esclarece dúvidas.
* O Entrevistador registra o feedback/parecer sobre o candidato no ATS ou formulário padrão.
* O Entrevistador decide se o candidato avança no processo.

**Roteamento:**

***Aprovar Candidato:***
Encaminha para a atividade `Agendar Entrevista Técnica`.

***Reprovar Candidato:***
Encaminha para a atividade `Rejeitado na Entrevista Inicial`.

**Integrações:**

* ATS (para registrar feedback e atualizar status).
* Plataforma de Videoconferência.

**Pontos de Atenção:**

Manter um roteiro de entrevista estruturado para garantir comparabilidade. Focar em perguntas situacionais e comportamentais. Registrar o feedback logo após a entrevista.

Perfeito! Entendi a sua ideia. Você quer focar esta atividade especificamente no ato de **definir e agendar** as próximas etapas (técnicas/gestor), tratando a confirmação ou impossibilidade de agendamento com o candidato.

Vamos refinar a descrição, mantendo a sua ideia central e a estrutura que estamos usando:

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
    * O Analista RH atualiza o status do candidato no ATS e registra os detalhes do agendamento no formulário do processo.
    * O processo avança para a próxima etapa (`Realizar Entrevista e Avaliação Técnica`).
  * **Se o candidato recusar** as opções, não responder após um número razoável de tentativas (definir política interna, ex: 3 tentativas em 48h), ou desistir do processo:
    * O Analista RH registra o motivo no ATS/formulário.
    * O processo é desviado para a notificação de rejeição.

**Roteamento:**

***Aprovação - Agendamento Confirmado***
Encaminha para a atividade `Realizar Entrevista e Avaliação Técnica` (ou um estado de "Aguardando Realização da Entrevista/Avaliação" se preferir marcar essa espera no fluxo).

***Rejeição - Não Agendado / Desistência***
Encaminha para a atividade `Entrevista Técnica Cancelada` (para formalizar o encerramento da participação do candidato no processo).

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

### Realizar Entrevistas e Avaliações Técnica

**Usuário(s) responsável:**

Gestor Solicitante, Avaliadores Técnicos, (Analista RH como suporte/coordenador)

**Descrição do Procedimento:**

* **Ativação:** A tarefa é ativada no sistema para os responsáveis (Gestor, Avaliadores) pouco antes da data/hora agendada para a entrevista/avaliação (Ex: 1-2 dias antes, ou no próprio dia). O sistema pode enviar lembretes.
* **Condução:** Os entrevistadores/avaliadores designados conduzem as sessões (entrevista técnica, comportamental, apresentação de case, teste prático, etc.) conforme planejado e agendado na etapa anterior.
* **Registro de Feedback:** **Imediatamente após** cada sessão (ou o mais breve possível), cada entrevistador/avaliador acessa o sistema (ATS ou formulário do workflow) e registra suas percepções de forma estruturada:
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
Encaminha para a atividade `Proposta de Contratação`.

***Rejeição - Não Recomendado***
* Encaminha para a atividade `Rejeitado na Entrevista e Avaliação Técnica`.

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

### Comunicar Rejeição

**Usuário(s) responsável:** Recrutador (RH), Sistema (para mensagens automáticas)

**Descrição do Procedimento:**

* O Recrutador (ou o sistema) identifica os candidatos que foram reprovados em alguma etapa.
* O Recrutador define o momento do envio da comunicação (logo após a reprovação ou ao final do processo seletivo).
* O Recrutador seleciona o modelo de mensagem de feedback (pode ser genérico ou, idealmente, com algum ponto específico, se a política da empresa permitir e o volume não for impeditivo).
* O Recrutador (ou o sistema) envia a comunicação para o candidato (normalmente por e-mail).
* O Recrutador atualiza o status final do candidato no ATS.

**Roteamento:**

* Comunicação Enviada:
  * Finaliza o fluxo para este candidato específico (End Event).

**Regra de Formulário:**

Mensagem de comunicação é obrigatória.

**Integrações:**

* ATS (para obter lista de rejeitados e atualizar status).
* Sistema de E-mail.

**Casos de Uso fora do Escopo:**

Feedback detalhado por telefone (geralmente para fases mais avançadas).

**Pontos de Atenção:**

Manter um tom respeitoso e profissional. Agradecer a participação do candidato. Garantir que todos os rejeitados recebam comunicação para preservar a imagem empregadora.






---

### (Opcional) Verificar Referências

**Usuário(s) responsável:**

Analista RH

**Descrição do Procedimento:**

* Se definido no processo, o Analista RH solicita ao candidato os contatos de referências profissionais.
* O Analista RH entra em contato com as referências (geralmente ex-gestores ou pares) para coletar feedback sobre o desempenho e comportamento profissional do candidato.
* O feedback é registrado de forma confidencial.

**Roteamento:**

***Aprovação - Referências OK / Prosseguir***
Encaminha para a atividade `Tomar Decisão Final (Contratar/Rejeitar)` (ou para a próxima etapa definida, se houver mais alguma antes da decisão).

***Rejeição - Alerta nas Referências / Rejeitar***
Encaminha para a atividade `Notificar Candidato Rejeitado` (ou pode voltar para `Tomar Decisão Final` para uma análise mais aprofundada do alerta). *Simplificando, vamos direto para a decisão.*

**Integrações:**

* **ATS:** Registro do status e resumo da verificação de referências.

**Pontos de Atenção:**

* Realizar a verificação apenas com o consentimento explícito do candidato.
* Fazer perguntas objetivas e relevantes para a vaga.
* Respeitar a confidencialidade das informações.

---

### Tomar Decisão Final (Contratar/Rejeitar)

**Usuário(s) responsável:**

Gestor Solicitante, Analista RH (Decisão Colaborativa)

**Descrição do Procedimento:**

* O Gestor Solicitante e o Analista RH revisam todo o histórico do candidato no processo: currículo, resultados das entrevistas, avaliações, (e referências, se aplicável).
* Comparam o candidato com os requisitos da vaga e, implicitamente, com outros candidatos finalistas (embora este processo seja por candidato, a decisão considera o pool).
* Tomam a decisão final: fazer uma proposta de contratação ou rejeitar o candidato.
* A decisão é registrada no sistema.

**Roteamento:**

***Aprovação - Fazer Proposta***
Encaminha para a atividade `Elaborar/Enviar Proposta de Contratação`

***Rejeição - Rejeitar Candidato***
Encaminha para a atividade `Notificar Candidato Rejeitado`

**Integrações:**

* **ATS:** Registro da decisão final.

**Pontos de Atenção:**

* Decisão deve ser baseada em critérios objetivos e nos dados coletados durante o processo.
* Alinhamento claro entre RH e Gestor é crucial.

---

### Elaborar/Enviar Proposta de Contratação

**Usuário(s) responsável:**

Analista RH

**Descrição do Procedimento:**

* O Analista RH formaliza a proposta de contratação, incluindo: cargo, salário, benefícios, data de início, local de trabalho e outras condições relevantes.
* A proposta pode precisar de aprovações internas adicionais (Ex: Diretor da área, Financeiro), dependendo da política da empresa (este sub-fluxo de aprovação não está detalhado aqui para manter genérico).
* Após aprovações (se necessárias), o Analista RH envia a proposta formal ao candidato por um canal oficial (Ex: e-mail, plataforma ATS).

**Roteamento:**

***Aprovação - Proposta Enviada***
Encaminha para a atividade `Aguardar Resposta do Candidato`

**Integrações:**

* **ATS:** Registro do envio da proposta e seus detalhes.
* **Sistema de RH (HRIS):** Pode ser consultado para padronizar dados da proposta.

**Pontos de Atenção:**

* Garantir que a proposta esteja clara, completa e em conformidade com o que foi discutido e com as políticas da empresa.
* Definir um prazo para o candidato responder.

---

### Aguardar Resposta do Candidato

**Usuário(s) responsável:**

Sistema/Workflow, Analista RH

**Descrição do Procedimento:**

* O sistema aguarda a resposta do candidato dentro do prazo estipulado.
* O candidato pode:
    * Aceitar a proposta.
    * Rejeitar a proposta.
    * Tentar negociar (neste fluxo genérico, uma negociação pode levar de volta à `Tomar Decisão Final` ou `Elaborar/Enviar Proposta` após discussão interna, ou ser tratada como rejeição se os termos não forem aceitos pela empresa).
* O Analista RH monitora o status e pode fazer follow-up se necessário.
* A resposta do candidato é registrada.

**Roteamento:**

***Aprovação - Proposta Aceita***
Encaminha para a atividade `Formalizar Contratação` (Evento Final de Sucesso)

***Rejeição - Proposta Rejeitada***
Encaminha para a atividade `Notificar Candidato Rejeitado` (Considerando a rejeição da proposta como um tipo de notificação final)

**Integrações:**

* **ATS:** Atualização do status do candidato (Aceitou Oferta, Recusou Oferta).

**Pontos de Atenção:**

* Estar preparado para responder a dúvidas ou tentativas de negociação do candidato de forma ágil.

---

### Notificar Candidato Rejeitado

**Usuário(s) responsável:**

Analista RH, Sistema/Workflow (para mensagens automáticas)

**Descrição do Procedimento:**

* Esta atividade é acionada sempre que um candidato é rejeitado em qualquer etapa anterior (`Entrevista Inicial`, `Avaliações`, `Verificar Referências`, `Decisão Final`) ou quando ele rejeita a proposta (`Aguardar Resposta`).
* O Analista RH (ou o sistema com um template aprovado) envia uma comunicação formal ao candidato informando sobre a decisão.
* Idealmente, oferecer um feedback construtivo, mesmo que breve, dependendo da política da empresa e da fase do processo.
* A comunicação visa manter uma boa imagem empregadora (Employer Branding).
* O status final do candidato é atualizado no sistema.

**Roteamento:**

***Conclusão - Notificação Enviada***
Encaminha para o evento final `Seleção Finalizada - Rejeitado`

**Integrações:**

* **ATS:** Registro da comunicação e atualização final do status do candidato.
* **Ferramenta de E-mail/Comunicação.**

**Pontos de Atenção:**

* Ser respeitoso e profissional na comunicação.
* Evitar linguagem que possa gerar problemas legais.
* Manter um registro da comunicação enviada.
* Dar o retorno o mais rápido possível após a decisão.

---

### Formalizar Contratação (Evento Final - Sucesso)

**Tipo:** Evento Final

**Descrição:**

* Acionado quando o candidato aceita a proposta na atividade `Aguardar Resposta do Candidato`.
* Marca o fim bem-sucedido do processo de *Seleção* para este candidato específico.
* Atualiza o status final do candidato no ATS/HRIS como "Contratado".
* **Importante:** Geralmente, esta etapa **aciona o início de um novo processo: "Admissão/Onboarding"**, que cuidará da coleta de documentos, exames admissionais, integração à empresa, etc.

**Integrações:**

* **ATS/HRIS:** Atualização final do status.
* **Sistema de Workflow:** Pode disparar o processo de Admissão/Onboarding.

---

### Seleção Finalizada - Rejeitado (Evento Final - Falha)

**Tipo:** Evento Final

**Descrição:**

* Acionado após a atividade `Notificar Candidato Rejeitado`.
* Marca o fim do processo de *Seleção* para este candidato, que não foi selecionado ou não aceitou a proposta.
* Garante que todos os candidatos que participaram do processo tenham um status final registrado.

**Integrações:**

* **ATS:** Confirmação do status final (Rejeitado/Desistiu).

---
