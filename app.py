import streamlit as st
from src.main import carregar_dados, calcular_resumo, criar_grafico, analisar_categorias, criar_pizza
from datetime import datetime

st.set_page_config(
    page_title="Dashboard Financeiro",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Dashboard Financeiro")

arquivo = st.file_uploader(
    label="Adicione seu arquivo CSV",
    type="csv"
)

st.divider()

dados = carregar_dados(arquivo)

if dados.empty:
    st.warning("⚠️ Nenhum dado encontrado.")
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

    st.subheader("Estatísticas")
    st.metric("Total de registros", dados.shape[0])
    st.metric("Categorias", len(categorias) - 1)

if categoria == "Todas":
    dados_filtrados = dados
else:
    dados_filtrados = dados[dados["Categoria"] == categoria]

gastos, receitas, total_receitas, total_gastos, saldo = calcular_resumo(dados_filtrados)
gastos_categoria = analisar_categorias(gastos)
chart = criar_grafico(gastos_categoria)
pizza = criar_pizza(gastos_categoria)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Saldo", f"R$ {saldo:.2f}")

with col2:
    st.metric("Total Receitas", f"R$ {total_receitas:.2f}")

with col3:
    st.metric("Total Gastos", f"R$ {total_gastos:.2f}")

st.subheader("Receitas")
st.dataframe(receitas, hide_index=True, width="stretch")

st.subheader("Gastos")
st.dataframe(gastos, hide_index=True, width="stretch")

st.download_button(
    label="Download dos Dados Filtrados",
    file_name="dados_filtrados.csv",
    data=dados_filtrados.to_csv(index=False)
)

if arquivo is None:
    nome_arquivo = "gastos.csv (padrão)"
else:
    nome_arquivo = arquivo.name

st.subheader("📂 Arquivo carregado")
st.write(f"**Nome do Arquivo:** {nome_arquivo}")

st.subheader("📈 Métricas")

col4, col5 = st.columns(2)

with col4:
    st.metric("Registros", dados_filtrados.shape[0])

with col5:
    st.metric("Colunas", dados_filtrados.shape[1])

st.divider()

st.subheader("📊 Gráficos")

col6, col7 = st.columns(2)

with col6:
    if chart is not None:
        st.pyplot(chart)
    else:
        st.info("Não há gastos para exibir nessa categoria.")

with col7:
    if pizza is not None:
        st.pyplot(pizza)
    else:
        st.info("Não há gastos para exibir nessa categoria.")

ultima_atualizacao = datetime.now().strftime("%d/%m/%Y, %H:%M")

st.divider()
st.caption("📊 Dashboard Financeiro")
st.caption("Desenvolvido por Murillo Alves Lourenço")
st.caption("Python • Pandas • Streamlit • Matplotlib")
st.caption(f"🕒 Última atualização: {ultima_atualizacao}")
