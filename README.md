# 🚀 INSTITUTO LANGCHAIN  

Os Agentes de IA estão mudando a forma como automatizamos tarefas e criamos aplicações; esse é um fato inegável. Acompanhar tudo o que é lançado ficou humanamente impossível: um framework novo por semana, duas atualizações de LLMs por semana, 75 técnicas novas de RAG por semana... enfim, um 📚 catatal de informações.  

Esse é o mal do nosso tempo: existe um monte de produtos sendo lançados, e nós ficamos perdidos no meio deles. Para resolver isso, devemos lançar nossa âncora ⚓ nesse oceano.  

Experimentei um ou outro framework agente e gostei muito do LangGraph. A estrutura dele lembra muito os processos de negócio que digitalizo e automatizo, o que me ajuda a pensar melhor em como funciona a estrutura do sistema multiagente 🤖, como cada parte impacta o todo e me instiga a aprender sobre cada componente desse novo mundo – afinal, ele não empacota tudo e entrega uma solução pronta.  

Neste Instituto, irei compartilhar o pouco que estou aprendendo e evoluindo 📈. Espero poder criar soluções que impactem a minha vida, resolvam alguns problemas, criem outros e, se Deus quiser, desenvolvam algo que resolva um problema seu.  

## 🔧 Pré-Requisitos  

É esperado que você saiba algo de Python, Agentes de IA e Poetry. Que tenha o Python >=3.10,<4.0.0 instalado, junto com o Poetry. E, claro, uma IDE bacanuda – recomendo o VSCode. 😎  

Para começar, basta usar o Poetry para criar o ambiente e instalar as dependências. 🚀  

## 📂 Notebooks  

Nesta pasta você encontrará meus estudos sobre determinados temas, onde pretendo me aprofundar em cada tópico antes de partir para a criação do sistema em si.  

💡 Sinta-se à vontade para me contatar e dar sugestões de melhorias e de projetos que poderiam ser experimentados.  

### 🔍 Busca SQL - TTQ (TEXT TO QUERY)  

Pensei em criar um sistema que pegue um texto e o transforme em uma query SQL. Queria fazer isso para um banco inteiro – por exemplo, pegar esse banco do meu ERP e montar uma consulta de forma simples para mim. Parece que ainda não chegamos ao ponto de conseguir fazer isso com as tecnologias atuais 🤯; porém, criar uma consulta para uma tabela me parece factível, e é isso que demonstro neste notebook.  

> **Imagino que uma solução para o que realmente quero fazer seja:**  
>  
> Em um ERP, poucas tabelas são relevantes para o negócio. Trabalho com o Newcon há 7 anos, fiz um certo número de relatórios, e tudo o que pedem sempre envolve as mesmas tabelas. 📊  
>  
> Então pensei o seguinte: e se eu criasse uma documentação sobre a tabela de cotas e como ela se relaciona com algumas outras tabelas – fazendo isso para as mais comuns – e se pegasse alguns dos relatórios mais frequentes que já elaborei? Cerca de 80% dos relatórios que me pedem podem ser resolvidos com 20% dos que já criei, seja adaptando algo que já foi feito ou criando um "frankenstein" 🧩. Agora, basta usar tudo isso como base de conhecimento para um sistema multiagente.  
>  
> Em palavras mais bonitas: criar metadados para as tabelas mais utilizadas nas consultas, estruturando-os de forma que os modelos de linguagem consigam pesquisá-los com facilidade; além disso, criar um banco de consultas já criadas e validadas – também com metadados. Esse conjunto deve ser capaz de orientar o LLM na criação de uma nova consulta.  

Quem sabe um dia eu não ataque esse problema? 🤔 Por hora, fiquem com meu estudo - [Busca SQL](https://github.com/Ro-Goncalves/instituto-langchain/blob/master/.notebooks/busca-sql.ipynb).
