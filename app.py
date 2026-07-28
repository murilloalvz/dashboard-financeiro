from datetime import datetime

import streamlit as st

from src.main import (
    analisar_categorias,
    calcular_resumo,
    carregar_dados,
    criar_grafico,
    criar_pizza,
)

st.set_page_config(
    page_title="Dashboard Financeiro",
    page_icon="📈",
    layout="wide",
)

st.title("📈 Dashboard Financeiro")
st.write("Analise receitas e despesas a partir de um arquivo CSV.")

arquivo = st.file_uploader(
    label="Adicione seu arquivo CSV",
    type=["csv"],
    help="O arquivo deve conter as colunas Categoria e Valor.",
)

try:
    dados = carregar_dados(arquivo)
except ValueError as erro:
    st.error(str(erro))
    st.stop()

if dados.empty:
    st.warning("Nenhum dado foi encontrado no arquivo.")
    st.stop()

colunas_obrigatorias = {"Categoria", "Valor"}
colunas_ausentes = colunas_obrigatorias - set(dados.columns)

if colunas_ausentes:
    st.error(
        "O arquivo CSV precisa conter as colunas: "
        + ", ".join(sorted(colunas_obrigatorias))
    )
    st.stop()

categorias = dados["Categoria"].dropna().unique().tolist()
categorias.insert(0, "Todas")

with st.sidebar:
    st.subheader("Filtros")
    categoria = st.selectbox("Escolha uma categoria", categorias)

    st.divider()
    st.subheader("Estatísticas da base")
    st.metric("Total de registros", dados.shape[0])
    st.metric("Categorias", len(categorias) - 1)

if categoria == "Todas":
    dados_filtrados = dados
else:
    dados_filtrados = dados[dados["Categoria"] == categoria]

gastos, receitas, total_receitas, total_gastos, saldo = calcular_resumo(
    dados_filtrados
)
gastos_categoria = analisar_categorias(gastos)
grafico_barras = criar_grafico(gastos_categoria)
grafico_pizza = criar_pizza(gastos_categoria)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Saldo", f"R$ {saldo:.2f}")

with col2:
    st.metric("Total de receitas", f"R$ {total_receitas:.2f}")

with col3:
    st.metric("Total de gastos", f"R$ {total_gastos:.2f}")

st.divider()
st.subheader("Movimentações")

aba_receitas, aba_gastos = st.tabs(["Receitas", "Gastos"])

with aba_receitas:
    st.dataframe(receitas, hide_index=True, width="stretch")

with aba_gastos:
    st.dataframe(gastos, hide_index=True, width="stretch")

st.download_button(
    label="Baixar dados filtrados",
    file_name="dados_filtrados.csv",
    data=dados_filtrados.to_csv(index=False).encode("utf-8"),
    mime="text/csv",
)

nome_arquivo = arquivo.name if arquivo is not None else "gastos.csv (exemplo)"

st.subheader("Arquivo analisado")
st.write(f"**Nome:** {nome_arquivo}")

col4, col5 = st.columns(2)

with col4:
    st.metric("Registros filtrados", dados_filtrados.shape[0])

with col5:
    st.metric("Colunas", dados_filtrados.shape[1])

st.divider()
st.subheader("Gráficos")

col6, col7 = st.columns(2)

with col6:
    if grafico_barras is not None:
        st.pyplot(grafico_barras)
    else:
        st.info("Não há gastos para exibir nesta seleção.")

with col7:
    if grafico_pizza is not None:
        st.pyplot(grafico_pizza)
    else:
        st.info("Não há gastos para exibir nesta seleção.")

pagina_atualizada = datetime.now().strftime("%d/%m/%Y às %H:%M")

st.divider()
st.caption("Desenvolvido por Murillo Alves Lourenço")
st.caption("Python • Pandas • Streamlit • Matplotlib")
st.caption(f"Página atualizada em {pagina_atualizada}")
