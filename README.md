# Dashboard Financeiro

Aplicação web desenvolvida com **Python, Pandas e Streamlit** para importar, validar e analisar dados financeiros em arquivos CSV.

O dashboard transforma registros de receitas e despesas em indicadores, filtros e visualizações que facilitam a interpretação dos dados.

## Aplicação online

**Acesse o projeto:** https://dashboard-financeiro-murilloalvz.streamlit.app/

## Principais funcionalidades

- Upload de arquivos CSV
- Validação das colunas obrigatórias
- Cálculo de receitas, despesas e saldo
- Filtro de registros por categoria
- Análise de gastos por categoria
- Gráficos de barras e pizza
- Download dos dados filtrados
- Tratamento de arquivos vazios ou inválidos

## Tecnologias

- Python
- Pandas
- Streamlit
- Matplotlib
- Git e GitHub

## Estrutura

```text
dashboard-financeiro/
├── data/
│   └── gastos.csv
├── images/
├── src/
│   └── main.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Executando localmente

```bash
git clone https://github.com/murilloalvz/dashboard-financeiro.git
cd dashboard-financeiro
python -m venv venv
```

Ative o ambiente virtual.

Windows:

```bash
.\venv\Scripts\activate
```

Linux ou macOS:

```bash
source venv/bin/activate
```

Instale as dependências e execute:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Demonstração

![Visão geral do dashboard](<images/Captura de tela_20-7-2026_12610_localhost.jpeg>)

![Gráficos da análise](<images/Captura de tela_20-7-2026_12641_localhost-1.jpeg>)

![Filtros interativos](<images/Captura de tela_20-7-2026_12713_localhost.jpeg>)

## Aprendizados

O projeto foi utilizado para praticar:

- Manipulação de DataFrames
- Filtragem com máscaras booleanas
- Agregações com `groupby`
- Modularização de código Python
- Validação e tratamento de erros
- Visualização de dados
- Desenvolvimento e deploy de aplicações com Streamlit
- Controle de versão com Git

## Próximos passos

- Adicionar filtro por período
- Criar visualizações com Plotly
- Integrar banco de dados
- Adicionar testes automatizados
- Exportar relatórios

## Autor

**Murillo Lourenço**  
Estudante de Análise e Desenvolvimento de Sistemas na FATEC Sorocaba.

Interesses: Dados, Inteligência Artificial, Automação e Engenharia de Software.