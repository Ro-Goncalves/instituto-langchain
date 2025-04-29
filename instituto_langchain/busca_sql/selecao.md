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
Encaminha para a atividade `Aguardar Entrevista Inicial`

***Reprovação - Processo Finalizado***
Encaminha para a atividade `Entrevista Inicial Rejeitada`

**Integrações:**

* **Sistema de Workflow:** Recebe dados do processo de Recrutamento.
* **ATS (Applicant Tracking System):** Para buscar/atualizar o status do candidato.

**Pontos de Atenção:**

* Garantir que a transição entre o processo de Recrutamento e Seleção seja fluida e sem perda de dados.
* O Analista RH deve ter acesso rápido ao currículo e informações da triagem.

---





### Aguardar Entrevista Inicial (RH)

**Usuário(s) responsável:**

Analista de RH

**Descrição do Procedimento:**

* O Recrutador recebe a lista de candidatos aprovados na triagem.
* O Recrutador entra em contato com os candidatos (e-mail, telefone, plataforma) para verificar interesse e disponibilidade.
* O Recrutador agenda a entrevista (presencial, telefone ou vídeo-conferência), conciliando agenda com o entrevistador do RH (que pode ser o próprio Recrutador).
* O Recrutador envia confirmação/convite da entrevista para o candidato e entrevistador(es).
* O Recrutador atualiza o status do candidato no ATS.

**Roteamento:**

* Agendamento Confirmado:
  * Encaminha para a atividade `Realizar Entrevista Inicial (RH)`.
* Candidato Indisponível/Desistiu:
  * Encaminha para a atividade `Comunicar Rejeição` ou atualiza status como desistente.

**Regra de Formulário:**

Data, hora e formato da entrevista são obrigatórios.

**Integrações:**

* ATS (para buscar contatos e atualizar status).
* Ferramenta de Agenda (Ex: Google Calendar, Outlook Calendar) para verificar disponibilidade e enviar convites.
* Plataforma de Videoconferência (Ex: Google Meet, Zoom, Teams) para gerar links.

**Casos de Uso fora do Escopo:**

Agendamento de entrevistas coletivas.

**Pontos de Atenção:**

Ser claro na comunicação com o candidato sobre os próximos passos. Confirmar o recebimento do convite.

---

### Realizar Entrevista Inicial (RH)

**Usuário(s) responsável:**

Recrutador (RH), Entrevistador de RH

**Descrição do Procedimento:**

* O Entrevistador do RH conduz a entrevista com o candidato (presencial, telefone ou vídeo).
* O Entrevistador avalia aspectos comportamentais (soft skills), alinhamento cultural, entendimento da vaga, histórico profissional e pretensão salarial.
* O Entrevistador apresenta a empresa e a vaga ao candidato, esclarece dúvidas.
* O Entrevistador registra o feedback/parecer sobre o candidato no ATS ou formulário padrão.
* O Entrevistador decide se o candidato avança no processo.

**Roteamento:**

* Aprovar Candidato:
  * Encaminha para a atividade `Agendar Entrevista Técnica/Gestor`.
* Reprovar Candidato:
  * Encaminha para a atividade `Comunicar Rejeição`.

**Regra de Formulário:**

Parecer (feedback estruturado) sobre o candidato é obrigatório.

**Integrações:**

* ATS (para registrar feedback e atualizar status).
* Plataforma de Videoconferência.

**Casos de Uso fora do Escopo:**

Entrevistas assíncronas (vídeos gravados pelos candidatos).

**Pontos de Atenção:**

Manter um roteiro de entrevista estruturado para garantir comparabilidade. Focar em perguntas situacionais e comportamentais. Registrar o feedback logo após a entrevista.

---

>O processo continuaria com atividades como: Agendar Entrevista Técnica/Gestor, Realizar Entrevista Técnica/Gestor, Aplicar Testes/Avaliações, Verificar Referências, Aprovar Contratação Final, Gerar Carta Oferta, Aguardar Aceite, Comunicar Rejeição, Iniciar Admissão, etc., seguindo a mesma estrutura

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








Okay, entendido! Com base no processo de "Recrutamento" que definimos e no formato que utilizamos, vamos criar agora o processo genérico de **Seleção de Candidato**.

Este processo inicia para cada candidato individualmente, logo após a conclusão da triagem e o acionamento da atividade `Abrir Processos Seleção` no fluxo de Recrutamento.

---



### Agendar/Realizar Entrevista Inicial (RH)

**Usuário(s) responsável:**

Analista RH

**Descrição do Procedimento:**

* O Analista RH entra em contato com o candidato para agendar a primeira entrevista (geralmente um screening).
* O Analista RH realiza a entrevista, focando em:
    * Apresentação da empresa e da vaga.
    * Validação de requisitos chave e experiências do currículo.
    * Avaliação inicial de fit cultural e soft skills.
    * Alinhamento de expectativas (salariais, modalidade de trabalho, etc.).
    * Esclarecimento de dúvidas do candidato.
* O Analista RH registra suas percepções e o resultado da entrevista no sistema.

**Roteamento:**

***Aprovação - Avançar para Próxima Etapa***
Encaminha para a atividade `Agendar/Realizar Avaliações Técnicas/Comportamentais`

***Rejeição - Rejeitar Candidato***
Encaminha para a atividade `Notificar Candidato Rejeitado`

**Integrações:**

* **ATS:** Registro do feedback da entrevista.
* **Ferramenta de Agendamento/Calendário:** Para marcar a entrevista.

**Pontos de Atenção:**

* Manter uma comunicação clara e profissional com o candidato.
* Ser pontual e respeitar o tempo agendado.
* Dar um feedback claro (interno) sobre os motivos de aprovação ou rejeição.

---

### Agendar/Realizar Avaliações Técnicas/Comportamentais

**Usuário(s) responsável:**

Analista RH, Gestor Solicitante, Avaliadores Técnicos (se aplicável)

**Descrição do Procedimento:**

* O Analista RH, em conjunto com o Gestor Solicitante, define quais avaliações são necessárias (Ex: teste técnico online, case prático, entrevista técnica, entrevista comportamental/fit com gestor, painel com equipe).
* O Analista RH (ou o Gestor) agenda e coordena a aplicação das avaliações e/ou entrevistas.
* As entrevistas/avaliações são conduzidas pelos responsáveis designados.
* Os resultados e feedbacks de cada avaliação são compilados e registrados no sistema.

**Roteamento:**

***Aprovação - Avançar para Decisão***
Encaminha para a atividade `Tomar Decisão Final (Contratar/Rejeitar)`

***Rejeição - Rejeitar Candidato***
Encaminha para a atividade `Notificar Candidato Rejeitado`

**Integrações:**

* **ATS:** Registro dos resultados das avaliações.
* **Plataformas de Avaliação Online:** (Ex: HackerRank, Mettl, Gupy Clima & Engajamento - se aplicável).
* **Ferramenta de Agendamento/Calendário.**

**Pontos de Atenção:**

* Garantir que as avaliações sejam relevantes para a função e aplicadas de forma padronizada.
* Manter o candidato informado sobre as próximas etapas e prazos estimados.
* Coletar feedback de todos os envolvidos na avaliação de forma estruturada.
* Pode haver múltiplas rodadas aqui; esta atividade representa o conjunto delas.

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

Espero que este detalhamento do processo de **Seleção de Candidato**, seguindo a estrutura anterior e buscando ser genérico, atenda às suas necessidades!
