# Dashboard Financeiro

Aplicação web desenvolvida com Python, Pandas, Matplotlib e Streamlit para analisar receitas e despesas a partir de arquivos CSV.

O projeto transforma movimentações financeiras em indicadores, filtros, tabelas e gráficos. Também permite importar uma base própria e exportar os dados filtrados.

## Demonstração online

[Acessar o Dashboard Financeiro](https://dashboard-financeiro-murilloalvz.streamlit.app/)

## Visão geral

![Visão geral do dashboard](<images/Captura de tela_20-7-2026_12610_localhost.jpeg>)

## Funcionalidades

- Upload de arquivos CSV
- Base de exemplo disponível ao abrir a aplicação
- Validação de arquivo vazio, estrutura e valores numéricos
- Cálculo de receitas, despesas e saldo
- Filtro de movimentações por categoria
- Análise de gastos por categoria
- Gráficos de barras e distribuição percentual
- Tabelas separadas de receitas e gastos
- Download dos dados filtrados em CSV

## Tecnologias

- Python
- Pandas
- Matplotlib
- Streamlit
- Git e GitHub

## Formato dos dados

O CSV precisa conter, no mínimo, as colunas `Categoria` e `Valor`. Valores positivos são tratados como receitas e valores negativos como despesas.

Exemplo:

```csv
Data,Categoria,Descricao,Valor
2026-06-01,Salário,Pagamento,2500
2026-06-02,Alimentação,Almoço,-35
```

As colunas `Data` e `Descricao` são opcionais para os cálculos atuais, mas ajudam a contextualizar as movimentações exibidas nas tabelas.

## Estrutura do projeto

```text
dashboard-financeiro/
├── data/
│   └── gastos.csv
├── images/
├── src/
│   └── main.py
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```

## Como executar localmente

Clone o repositório e entre na pasta:

```bash
git clone https://github.com/murilloalvz/dashboard-financeiro.git
cd dashboard-financeiro
```

Crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente no Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

No Linux ou macOS:

```bash
source venv/bin/activate
```

Instale as dependências e execute a aplicação:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Outras telas

![Gráficos da análise](<images/Captura de tela_20-7-2026_12641_localhost-1.jpeg>)

![Filtros interativos](<images/Captura de tela_20-7-2026_12713_localhost.jpeg>)

## Aprendizados

O projeto foi utilizado para praticar:

- Manipulação de DataFrames e Series
- Filtragem com máscaras booleanas
- Agregações com `groupby`
- Modularização de código Python
- Validação de dados e tratamento de estados vazios
- Visualização de dados com Matplotlib
- Desenvolvimento e deploy de aplicações com Streamlit
- Controle de versão com Git e GitHub

## Escopo futuro

Possíveis evoluções, mantidas fora da versão atual para preservar o foco do projeto:

- Filtro por período
- Testes automatizados
- Visualizações temporais
- Exportação de relatório

## Autor

**Murillo Alves Lourenço**  
Estudante de Análise e Desenvolvimento de Sistemas na FATEC Sorocaba.

Interesses: Dados, Inteligência Artificial, Automação e Engenharia de Software.
