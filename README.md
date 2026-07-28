# Dashboard Financeiro

Dashboard financeiro desenvolvido em Python para análise e visualização de receitas e despesas.

O projeto permite importar arquivos CSV, calcular indicadores financeiros, filtrar informações por categoria e visualizar os dados através de tabelas e gráficos interativos utilizando Streamlit.

---

## Link de execução web

https://dashboard-financeiro-murilloalvz.streamlit.app/

---

## Objetivos

Este projeto foi desenvolvido para praticar conceitos de:

- Python
- Pandas
- Streamlit
- Matplotlib
- Estruturação de projetos
- Manipulação e análise de dados
- Git e GitHub

---

## Funcionalidades

- Upload de arquivos CSV
- Leitura e tratamento de dados com Pandas
- Validação das colunas obrigatórias do arquivo
- Separação entre receitas e despesas
- Cálculo do saldo financeiro
- Análise de gastos por categoria
- Gráfico de barras
- Gráfico de pizza
- Filtro por categoria
- Download dos dados filtrados
- Exibição de métricas financeiras
- Informações do arquivo carregado

---

## Tecnologias

- Python
- Pandas
- Matplotlib
- Streamlit
- Git
- GitHub

---

## Estrutura do projeto

```text
dashboard-financeiro/
│
├── data/
│   └── gastos.csv
│
├── images/
│
├── src/
│   └── main.py
│
├── .gitignore
├── app.py
├── requirements.txt
└── README.md
```

---

## Como executar localmente

Clone o repositório:

```bash
git clone https://github.com/murilloalvz/dashboard-financeiro.git
```

Entre na pasta:

```bash
cd dashboard-financeiro
```

Crie um ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente.

Windows:

```bash
.\venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
streamlit run app.py
```

---

## Funcionalidades implementadas

- Estruturação do projeto
- Organização em módulos
- Leitura de arquivos CSV
- Manipulação de DataFrames
- Separação de receitas e despesas
- Cálculo de indicadores financeiros
- Agrupamento por categoria
- Visualizações com Matplotlib
- Dashboard interativo com Streamlit
- Upload e download de arquivos
- Tratamento de dados vazios
- Validação de colunas obrigatórias
- Deploy com Streamlit Community Cloud

---

## Conceitos praticados

Durante o desenvolvimento deste projeto foram utilizados conceitos como:

- Funções
- Parâmetros
- Return
- Modularização
- DataFrames
- Series
- GroupBy
- Máscaras booleanas
- Tratamento de erros
- Visualização de dados
- Estruturação de aplicações
- Controle de versão com Git

---

## Próximas melhorias

- Filtro por período
- Novos tipos de gráficos
- Dashboard com Plotly
- Exportação em PDF
- Integração com banco de dados

---

## Imagens

![Exemplo do dashboard em funcionamento](<images/Captura de tela_20-7-2026_12610_localhost.jpeg>)

![Gráficos dos dados recebidos](<images/Captura de tela_20-7-2026_12641_localhost-1.jpeg>)

![Uso dos filtros](<images/Captura de tela_20-7-2026_12713_localhost.jpeg>)

---

## Autor

Murillo Alves Lourenço

Estudante de Análise e Desenvolvimento de Sistemas — FATEC Sorocaba

Áreas de interesse:

- Ciência de Dados
- Engenharia de Dados
- Inteligência Artificial
- Machine Learning
- Quantitative Finance
