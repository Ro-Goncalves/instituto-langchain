# Admissão de Colaborador

> Este processo descreve as etapas genéricas desde o momento em que a contratação de um novo colaborador é formalizada até a sua efetiva integração inicial na empresa, incluindo os cadastros sistêmicos necessários. Ele opera individualmente para cada candidato aprovado e com proposta aceita no processo de Seleção.
> >
> **Todo o conteúdo foi gerado com a ajuda do Gemini.**

## Atividades

### Coletar Documentação

**Usuário(s) responsável:**

Analista RH

**Descrição do Procedimento:**

* Esta atividade é iniciada automaticamente pela atividade `Disparar Processo de Admissão` do processo de Seleção de Candidato.
* Uma Integração recebe os dados do candidato aprovado (ID, informações básicas, cargo, salário, data de início, gestor, etc.) e da vaga.
* O Sistema atribui formalmente o novo colaborador ao Analista RH responsável pela condução da admissão.
* O Analista RH é notificado que um novo processo de admissão foi iniciado.
* **(Status: Aguardando Contato Inicial)** O Analista RH entra em contato com o novo colaborador para:
    * Parabenizá-lo e dar as boas-vindas formais.
    * Informar sobre os próximos passos do processo de admissão.
    * Solicitar a documentação necessária (lista de documentos, formatos, prazos).
    * Disponibilizar um canal para envio seguro da documentação (Ex: portal do candidato, e-mail seguro, upload no sistema de workflow).
    * Agendar exames admissionais, se aplicável e ainda não realizado.
* **(Status: Aguardando Documentação)** O processo aguarda o envio da documentação pelo novo colaborador e a realização dos exames.
* **(Status: Documentação Recebida / Em Análise)** O Analista RH recebe e confere toda a documentação (física ou digital). Verifica pendências ou inconsistências.
    * *Se houver pendências:* Retorna ao status `Aguardando Documentação` ou um status específico como `Aguardando Correção de Documentos`, com comunicação ao novo colaborador.
* **(Status: Documentação Validada)** Após toda a documentação estar correta e os resultados dos exames (se aplicáveis) estiverem OK.
* O Analista RH atualiza o formulário com o status da documentação e anexa os comprovantes.

**Roteamento:**

***Aprovação - Documentação Completa e Validada***
Encaminha para as atividades `Realizar Cadastro no Sistema de TI` E `Realizar Cadastro no ERP e Sistemas Operacionais` (podem ocorrer em paralelo).

***Rejeição - Desistência / Problema Impeditivo***
Encaminha para a atividade `Admissão Cancelada` (Ex: candidato desiste, reprova no exame admissional, documentação fundamental irregular).

**Integrações:**

* **Sistema de Workflow:** Recebe dados do processo de Seleção, gerencia status e tarefas.
* **ATS (Applicant Tracking System):** Para buscar dados complementares e atualizar o status final do candidato para "Em Admissão" ou "Admitido".
* **HRIS (Sistema de Informação de RH):** Para consulta de listas de documentos padrão, e futuramente, para o cadastro efetivo do colaborador.
* **E-mail/Comunicação:** Para contato com o novo colaborador.
* **Plataforma de Gestão de Documentos/Portal do Colaborador:** Para upload e gestão segura de documentos.
* **Clínica de Saúde Ocupacional:** Para agendamento e recebimento de resultados de exames.

**Pontos de Atenção:**

* Garantir clareza na lista de documentos e nos prazos.
* Assegurar a segurança e privacidade dos dados e documentos do novo colaborador (LGPD).
* Comunicar-se de forma acolhedora e eficiente com o novo colaborador.
* Definir um processo claro para tratamento de pendências documentais.

---

### Realizar Cadastro no Sistema de TI

**Usuário(s) responsável:**

Analista de TI / Suporte de TI

**Descrição do Procedimento:**

* A atividade é iniciada após a validação da documentação básica necessária para criação de acessos.
* O Analista de TI recebe uma notificação com os dados do novo colaborador (Nome completo, CPF, Cargo, Departamento, Gestor Direto, Data de Início).
* **Criação de Credenciais:**
    * Criação da conta de usuário no Active Directory (AD) ou sistema similar de gerenciamento de identidades.
    * Criação da conta de e-mail corporativo.
    * Atribuição a grupos de segurança e listas de distribuição iniciais conforme o cargo/departamento.
* **Provisionamento de Acessos:**
    * Concessão de acesso básico a sistemas corporativos (Ex: Intranet, sistema de chamados).
    * Liberação de acesso a pastas de rede, se aplicável.
* **Preparação de Equipamentos (se aplicável e sob responsabilidade da TI Central):**
    * Verificação e reserva de hardware (notebook, desktop, monitor).
    * Instalação de softwares padrão e específicos para a função (pode ser uma imagem padrão).
* O Analista de TI registra no formulário do workflow a conclusão das criações, os nomes de usuário, e-mails e qualquer informação relevante (Ex: patrimônio do equipamento preparado).
* O Analista de TI notifica o Analista RH e/ou o Gestor Direto sobre a conclusão e as credenciais (forma segura de repasse de senhas provisórias).

**Roteamento:**

***Concluído - Cadastros de TI Realizados***
Encaminha para a atividade `Verificar Conclusão de Cadastros e Preparar Integração`.

***Falha - Erro no Cadastro TI***
Retorna a tarefa para o Analista de TI com a descrição do erro para correção, ou notifica o Analista RH para intervenção.

**Integrações:**

* **Sistema de Workflow:** Para atribuição da tarefa, recebimento de dados e registro da conclusão.
* **HRIS:** Como fonte de dados validados do novo colaborador.
* **Active Directory (AD) / LDAP:** Para criação e gerenciamento de contas de usuário.
* **Sistema de E-mail Corporativo:** (Ex: Microsoft Exchange, Google Workspace).
* **Ferramentas de Provisionamento de Software/Imagem:** (Ex: SCCM, Intune).
* **Sistema de Gerenciamento de Ativos (ITAM):** Para registrar o hardware alocado.
* **Sistema de Service Desk (ITSM):** Para registrar a solicitação e o atendimento.

**Pontos de Atenção:**

* Garantir que os acessos sejam criados ANTES da data de início do colaborador.
* Seguir as políticas de segurança da informação para criação de senhas e concessão de acessos (princípio do menor privilégio).
* Assegurar que os equipamentos estejam prontos e testados.
* Ter um procedimento claro para o repasse seguro das credenciais iniciais.

---

### Realizar Cadastro no ERP e Sistemas Operacionais

**Usuário(s) responsável:**

Analista Operacional / Usuário Chave do Departamento (ou Analista RH, dependendo da estrutura)

**Descrição do Procedimento:**

* A atividade é iniciada após a validação da documentação e, idealmente, em paralelo com os cadastros de TI.
* O responsável recebe uma notificação com os dados do novo colaborador (Nome completo, CPF, Cargo, Departamento, Centro de Custo, Gestor Direto, Data de Início, dados bancários se já coletados).
* **Cadastro no ERP:**
    * Criação do registro do funcionário no sistema ERP.
    * Associação ao departamento, centro de custo e estrutura hierárquica correta.
    * Configuração de perfis de acesso aos módulos e funcionalidades do ERP necessários para a função.
* **Cadastro em Outros Sistemas Operacionais/Negócio:**
    * Criação de usuários em outros sistemas específicos da área de atuação do novo colaborador (Ex: CRM, sistemas de Ponto, plataformas de e-learning, sistemas de gestão de projetos, etc.).
* **Acessos Físicos (se aplicável):**
    * Solicitação ou confecção de crachá de acesso.
    * Liberação de acesso a áreas restritas, se necessário.
* O responsável registra no formulário do workflow a conclusão dos cadastros e quaisquer informações relevantes (Ex: ID do usuário no ERP, número do crachá).
* O responsável notifica o Analista RH e/ou o Gestor Direto sobre a conclusão.

**Roteamento:**

***Concluído - Cadastros Operacionais Realizados***
Encaminha para a atividade `Verificar Conclusão de Cadastros e Preparar Integração`.

***Falha - Erro no Cadastro Operacional***
Retorna a tarefa para o responsável com a descrição do erro para correção, ou notifica o Analista RH para intervenção.

**Integrações:**

* **Sistema de Workflow:** Para atribuição da tarefa, recebimento de dados e registro da conclusão.
* **HRIS:** Como fonte principal de dados do novo colaborador.
* **ERP (Enterprise Resource Planning):** (Ex: SAP, Oracle EBS, Totvs Protheus).
* **Sistemas de CRM, Ponto Eletrônico, LMS, etc.**
* **Sistema de Controle de Acesso Físico.**

**Pontos de Atenção:**

* Garantir que os cadastros sejam realizados ANTES da data de início.
* Assegurar que os perfis de acesso estejam corretos e alinhados com as responsabilidades do cargo.
* A correta alocação em centros de custo e departamentos é crucial para fins de relatórios e gestão.
* Coordenar com a TI para que os acessos a sistemas que dependem do usuário de rede (AD) sejam feitos na ordem correta.

---

### Verificar Conclusão de Cadastros e Preparar Integração

**Usuário(s) responsável:**

Analista RH

**Descrição do Procedimento:**

* Esta atividade é iniciada quando as atividades `Realizar Cadastro no Sistema de TI` E `Realizar Cadastro no ERP e Sistemas Operacionais` são concluídas. O workflow aguarda a finalização de ambas (junção paralela).
* O Analista RH verifica no workflow se todos os cadastros foram efetivados e se há alguma pendência ou observação registrada pelas equipes de TI e Operacional.
* **(Status: Em Preparação da Integração)**
    * Confirmação da data e horário da sessão de integração/boas-vindas.
    * Preparo do kit de boas-vindas (material institucional, crachá (se já disponível), brindes, formulários pendentes para assinatura física, etc.).
    * Comunicação ao novo colaborador sobre os detalhes do primeiro dia (horário de chegada, local, quem procurar, agenda inicial).
    * Coordenação com o Gestor Direto para a recepção no primeiro dia (apresentação à equipe, ambiente de trabalho, etc.).
    * Reserva de sala e equipamentos para a sessão de integração, se presencial.
* **(Status: Tudo Pronto para Início)** O Analista RH atualiza o formulário indicando que todos os preparativos estão concluídos.

**Roteamento:**

***Aprovação - Preparativos Concluídos***
Encaminha para a atividade `Realizar Integração e Primeiros Passos`.

***Reprovação - Pendências nos Cadastros/Preparações***
Se houver pendências críticas, pode notificar os responsáveis (TI/Operacional) para correção urgente ou, em casos extremos, encaminhar para `Admissão Cancelada` (se a pendência for impeditiva e não solucionável a tempo). Idealmente, volta para a atividade específica que precisa de ajuste. Para simplificar, consideramos aqui que pendências são tratadas antes de aprovar.

**Integrações:**

* **Sistema de Workflow:** Para consolidar o status das atividades paralelas e gerenciar a tarefa do Analista RH.
* **HRIS:** Para confirmar dados e registrar informações.
* **Ferramenta de Agenda:** Para agendar a integração e convidar participantes.
* **Comunicação Interna:** Com o Gestor Direto e o novo colaborador.

**Pontos de Atenção:**

* Garantir que NADA falte para o primeiro dia do novo colaborador.
* A comunicação prévia sobre o primeiro dia ajuda a reduzir a ansiedade do novo integrante.
* O kit de boas-vindas deve ser completo e bem apresentado.

---

### Realizar Integração e Primeiros Passos

**Usuário(s) responsável:**

Analista RH, Gestor Direto

**Descrição do Procedimento:**

* Esta atividade ocorre na data de início do novo colaborador.
* **Recepção pelo Analista RH:**
    * Boas-vindas formais.
    * Apresentação da agenda do dia/semana inicial.
    * Entrega do kit de boas-vindas e crachá.
    * Sessão de integração (apresentação da empresa, cultura, políticas de RH, benefícios, canais de comunicação interna, ferramentas essenciais).
    * Coleta de assinaturas em documentos admissionais pendentes (Termo de Responsabilidade de Equipamentos, Acordos de Confidencialidade, etc.).
    * Esclarecimento de dúvidas iniciais.
* **Recepção pelo Gestor Direto:**
    * Apresentação à equipe e ao local de trabalho.
    * Entrega de equipamentos (notebook, celular corporativo) e verificação das credenciais de acesso (TI e Operacionais) junto ao colaborador.
    * Orientações sobre as primeiras tarefas, projetos e expectativas.
    * Indicação de "padrinho/madrinha" ou colega de referência para apoio nos primeiros dias.
* O Analista RH e/ou Gestor Direto registram no formulário do workflow a conclusão da integração inicial, confirmando que o colaborador está instalado e com acessos funcionais.

**Roteamento:**

***Aprovação - Integração Inicial Concluída***
Encaminha para a atividade `Admissão Concluída e Efetivada`.

***Pendência - Problemas na Integração / Acessos***
Se houver problemas críticos (Ex: acesso principal não funciona, equipamento com defeito), a atividade pode ficar em espera e gerar subtarefas para TI/Suporte/Operacional para resolução urgente. Após solução, o fluxo é retomado.

**Integrações:**

* **Sistema de Workflow:** Para registrar a conclusão da etapa.
* **HRIS:** Para atualizar o status do colaborador para "Ativo" e registrar a data de início efetiva.
* **Lista de Presença/Confirmação:** Para registrar a participação na sessão de integração.
* **Plataforma de Assinatura Eletrônica ou física:** Para formalizar documentos.

**Pontos de Atenção:**

* Tornar o primeiro dia uma experiência positiva e acolhedora.
* Garantir que o novo colaborador se sinta amparado e orientado.
* Verificar ativamente se todos os acessos e ferramentas estão funcionando.
* O papel do gestor direto é crucial para uma boa integração à equipe e às atividades.

---

### Admissão Concluída e Efetivada

**Usuário(s) responsável:**

Robô (Sistema de Automação/Workflow)

**Descrição do Procedimento:**

* Esta atividade é acionada automaticamente após a conclusão bem-sucedida da atividade `Realizar Integração e Primeiros Passos`.
* O Robô coleta os dados finais da admissão (Ex: ID do Colaborador no HRIS, confirmação de todos os cadastros, data de início efetiva, registro da integração realizada).
* O Robô atualiza o status final do colaborador no HRIS para "Ativo" (se não feito na etapa anterior) e no ATS para "Contratado/Admitido".
* O Robô pode disparar notificações para áreas relevantes (Ex: Folha de Pagamento confirmando a inclusão, Segurança do Trabalho para agendamento de treinamentos obrigatórios, etc.).
* **Todos os campos de dados nesta atividade são marcados como somente leitura (bloqueados)**, servindo como um registro histórico final da admissão bem-sucedida.

**Roteamento:**

Esta é uma atividade final, não possui roteamento de saída. Ela encerra o fluxo do processo de Admissão.

**Integrações:**

* **Sistema de Workflow:** Para receber o gatilho, consolidar dados finais e encerrar a instância do processo.
* **HRIS:** Para atualização final do status e dados do colaborador.
* **ATS:** Para atualização final do status do candidato.
* **Sistema de Folha de Pagamento:** Para notificação de inclusão.
* **Outros sistemas corporativos que necessitem ser informados.**

**Pontos de Atenção:**

* Garantir que todos os sistemas estejam sincronizados com o status final do colaborador.
* Assegurar a rastreabilidade completa do processo de admissão.
* Confirmar que as notificações para outras áreas foram enviadas com sucesso.

---

### Admissão Cancelada

**Usuário(s) responsável:**

Robô (Sistema de Automação/Workflow)

**Descrição do Procedimento:**

* Esta atividade é um evento final do processo, acionado quando uma rota de cancelamento/rejeição é seguida em etapas anteriores (Ex: desistência do candidato após aceite da proposta, reprovação em exame admissional crítico, falha grave e insolúvel na documentação).
* O Robô captura um "snapshot" das informações relevantes do processo no momento do cancelamento (Ex: dados do candidato, etapa do cancelamento, motivo registrado).
* **Todos os campos de dados nesta atividade são marcados como somente leitura (bloqueados)**.
* O status final do candidato no ATS/HRIS é atualizado para "Admissão Cancelada" ou similar.
* Se cadastros parciais (TI, ERP) foram iniciados, o Robô pode disparar tarefas de "rollback" ou notificar as equipes responsáveis para desfazer as configurações e liberar recursos.

**Roteamento:**

Esta é uma atividade final, não possui roteamento de saída para outras atividades dentro deste processo.

**Integrações:**

* **Sistema de Workflow:** Responsável por receber o fluxo das etapas anteriores, congelar os dados e encerrar a instância.
* **ATS/HRIS:** Confirmação/atualização final do status.
* **Sistemas de TI/ERP (via notificação/tarefa):** Para solicitar o cancelamento de contas/acessos criados.

**Pontos de Atenção:**

* Garantir que o motivo do cancelamento seja claramente registrado.
* Assegurar que quaisquer recursos provisionados (contas, licenças, hardware) sejam devidamente revertidos ou cancelados para evitar custos e falhas de segurança.
* Comunicar o cancelamento às partes interessadas que já haviam sido notificadas sobre a admissão.