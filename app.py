import streamlit as st
from src.main import carregar_dados, calcular_resumo, criar_grafico, analisar_categorias, criar_pizza
from datetime import datetime

st.set_page_config(
    page_title="Dashboard Financeiro",
    page_icon="📈",
    layout="wide"
)

arquivo = st.file_uploader(
    label = "Adcione seu arquivo CSV",
    type = "csv"
)

st.divider()

dados = carregar_dados(arquivo)
categorias = dados["Categoria"].unique().tolist()
categorias.insert(0, "Todas")

if dados.empty:
    st.info("⚠️ Nenhum dado encontrado.")

st.title("📈 Dashboard Financeiro") 
 
with st.sidebar:
    st.subheader("Filtros")

    categoria = st.selectbox("Escolha uma categoria", categorias)

    st.divider()

    st.subheader("Estatísticas")
    st.metric("Total de registros: ", dados.shape[0])
    st.metric("Categorias: ", dados.shape[1])

selecao = dados[dados["Categoria"] == categoria]

if categoria == "Todas":
    dados_filtrados = dados
else:
    dados_filtrados = selecao

gastos, receitas, total_receitas, total_gastos, saldo  = calcular_resumo(dados_filtrados)
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
st.dataframe(receitas, hide_index = True, width="stretch")

st.subheader("Gastos")
st.dataframe(gastos, hide_index = True, width="stretch")

st.download_button(
    label= "Download dos Dados Filtrados",
    file_name= "Dados_filtrados",
    data= dados_filtrados.to_csv(index=False)
)

col4, col5 = st.columns(2)

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
    if chart:
        st.pyplot(chart)
    else:
        st.info("Não há gastos para exibir nessa categoria.")

with col7:
    if pizza:
        st.pyplot(pizza)
    else:
        st.info("Não há gastos para exibir nessa categoria.")

ultima_atualizacao = datetime.now().strftime("%d/%m/%Y, %H:%M")

st.divider()

st.caption("📊 Dashboard Financeiro")
st.caption("Desenvolvido por Murillo Alves Lourenço")
st.caption("Python • Pandas • Streamlit • Matplotlib")
st.caption(f"🕒 Última atualização: {ultima_atualizacao}")
