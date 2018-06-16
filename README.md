# databases-buffet
Project for databases discipline.


##Requisitos:
```
Oi Pessoal, 

Como  vários grupos estão com dúvidas sobre o que implementar no protótipo, definimos o mínimo que deve ser feito:

- suporte em interface às operações CRUD da entidade festa e seus relacionamentos 1:N (suporte a cadastro e alteração de 1 dos tipos de festa e parte de  seus serviços, e consultas às festas cadastradas).  

- suporte em interface a 6 consultas de complexidade média/alta (ou seja: junções internas/externas, group by, estatísticas, etc... )

-  implementação de tratamento de consistência para aspectos que, nas Partes 1 e 2 do projeto, foram indicados para  serem tratados em aplicação. 

- tratamento de erros para as operações CRUD. 

Esse "mínimo"  deve ser implementado considerando um sub-esquema da base, ou seja, envolvendo entidades e relacionamentos "conectados" (similar a um sub-grafo), de modo a criar um subsistema funcional  do sistema proposto. 

Na versão corrigida da Parte 2, apenas os erros do esquema relacional precisam ser corrigidos (as justificativas não precisam ser refeitas). 

Além disso, verifiquem os  requisitos que estão definidos no documentos de especificação do projeto (Parte 3): scripts para criação e alimentação da base completa, documentação, relatório, etc... 

Elaine, Guilherme e Thais. 
```

##Principais operações:
```
Inserção e atualização de dados de pessoas, incluindo clientes, funcionários e especialistas;

Inserção de eventos e contratos;

Inserção e atualização de dados relativos a fornecimento de produtos, fornecedores, pratos, bebidas e cardápio;

Consultar quantas pessoas estão envolvidas em determinado evento;

Consultar quais fornecedores estão envolvidos nos produtos de um item;

Consultar quais são as melhores opções de fornecimento dos produtos necessários para formar todos os itens de um cardápio;

Consultar quais são os fornecedores com maior volume de transações considerando os tipos de evento;

Consultar contrato, local, cardápio, data, hora, tipo de festa e pessoas envolvidas em cada evento (cliente, funcionário e especialista).
```


##Criando a base de dados:
```
Para criar automaticamente a base de dados, bastar executar o script run.sh.

Note que é para esta operação, é necessário o auxílio do seguinte programa:

https://github.com/FelSiq/bllsht-my-database/
```
