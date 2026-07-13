import streamlit as st
from src.main import carregar_dados, calcular_resumo, criar_grafico, analisar_categorias

dados = carregar_dados()

categorias = dados["Categoria"].unique().tolist()
categorias.insert(0, "Todas")

st.title("📊 Dashboard Financeiro") 

categoria = st.selectbox(
    "Escolha uma categoria",
    categorias
)

selecao = dados[dados["Categoria"] == categoria]

if categoria == "Todas":
    dados_filtrados = dados
else:
    dados_filtrados = selecao

gastos, receitas, total_receitas, total_gastos, saldo  = calcular_resumo(dados_filtrados)
gastos_categoria = analisar_categorias(gastos)
chart = criar_grafico(gastos_categoria)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Saldo", f"R$ {saldo:.2f}")

with col2:
    st.metric("Total Receitas", f"R$ {total_receitas:.2f}")

with col3:
    st.metric("Total Gastos", f"R$ {total_gastos:.2f}")

st.subheader("Receitas")
st.dataframe(receitas)

st.subheader("Gastos")
st.dataframe(gastos)

st.pyplot(chart)
