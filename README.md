# projeto-qualidade

O objetivo desse projeto é criar uma base para aprender as bibliotecas em Python e entender como funciona a automação de tabelas em Python, porque eu trabalho com muitos dados, apesar de trabalhar com a área da qualidade, estudo programação, e tenho experiencia em Excel e Power Bi, também com KPI e indicadores, então quero resolver gargalos e agilizar o povoamento de dados nas tabelas que eu uso,  aprendendo essas automações tanto para povoar as tabelas quanto para leitura em Power BI vai ajudar muito, ainda tenho muito para aprender e entender sobre dados e automação, mas estou no caminho para evoluir.

Esse projeto de automação de planilha de Excel, facilita a implementação de dados com uma interface e também para futuras leituras em gráficos com o Power BI.

Antes os dados apenas eram preenchidos diretamente na tabela do Excel, com esse projeto, eu preencho os dados na interface e os dados são guardados em um banco de dados e uma planilha com resumo de dados é gerado automaticamente, além de que são dados que serão usados para futuras análises em Power BI.

**O projeto foi dividido em 3 fases:**

A **Fase 1** foi a automação da planilha de resumos com o uso da biblioteca Pandas, o programa usava os dados da planilha do Excel ainda, e assim criava a planilha de resumos automaticamente com gráficos de colunas.

A **Fase 2** foi implementado o banco de dados, e as interfaces para povoamento da tabela, nessa fase a tabela de resumos lê os dados do banco de dados, e aí não uso mais a planilha em Excel, apenas a do banco de dados, legal dessa fase foi a implementação do banco de dados em Python, usar os comandos em SQL e também criar as interfaces com o CustomTkinter. Nessa fase deixo tudo pronto para a fase 3 que é a mais intuitiva já que vamos criar tabelas em Power BI.

A **Fase 3** ainda está em andamento, mas logo atualizo.

**Linguagem:** Python\
**Bibliotecas:** Pandas, Openpyxl, CustomTkinter\
**Banco de dados:** SQLite3\
**Ferramentas:** Excel, Power BI

## Como rodar

- 1\. Instale as dependências:\
pip install pandas openpyxl customtkinter

- 2\. Execute a migração inicial (apenas uma vez):\
python fase2\_sql/migrar\_dados.py

- 3\. Para cadastrar registros:\
python fase2\_sql/interface.py\
python fase2\_sql/interface\_reclamacao.py

- 4\. Para gerar o relatório semanal:\
python fase1\_excel/relatório\_semanal.py

