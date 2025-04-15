PROMPT_ANALISE_MEMORIA = """
Extraia e formate fatos pessoais importantes sobre o usuário a partir da mensagem dele.
Concentre-se nas informações reais, não em meta-comentários ou solicitações.

Os fatos importantes incluem:
- Detalhes pessoais (nome, idade, localização)
- Informações profissionais (trabalho, educação, habilidades)
- Preferências (gostos, desgostos, favoritos)
- Circunstâncias de vida (família, relacionamentos)
- Experiências ou conquistas significativas
- Objetivos ou aspirações pessoais

Regras:
1. Extraia apenas fatos reais, ignorando solicitações ou comentários sobre lembrar de algo
2. Converta os fatos em declarações claras na terceira pessoa
3. Se não houver fatos reais, marque como "não importante"
4. Remova elementos conversacionais e foque apenas na informação essencial

Exemplos:
Entrada: "Ei, você pode lembrar que eu amo Star Wars?"
Saída: {{
    "is_importante": true,
    "memoria_formatada": "Ama Star Wars"
}}

Entrada: "Por favor, anote que trabalho como engenheiro"
Saída: {{
    "is_importante": true,
    "memoria_formatada": "Trabalha como engenheiro"
}}

Entrada: "Lembre-se disso: eu moro em Madri"
Saída: {{
    "is_importante": true,
    "memoria_formatada": "Mora em Madri"
}}

Entrada: "Você pode lembrar meus detalhes para a próxima vez?"
Saída: {{
    "is_importante": false,
    "memoria_formatada": null
}}

Entrada: "Ei, como você está hoje?"
Saída: {{
    "is_importante": false,
    "memoria_formatada": null
}}

Entrada: "Estudei ciência da computação no MIT e adoraria que você lembrasse disso"
Saída: {{
    "is_importante": true,
    "memoria_formatada": "Estudou ciência da computação no MIT"
}}

Mensagem: {message}
Saída:
"""
