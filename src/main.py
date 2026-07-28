import matplotlib.pyplot as plt
import pandas as pd


def carregar_dados(arquivo):
    """Carrega o CSV enviado ou usa a base de exemplo do projeto."""
    origem = arquivo if arquivo is not None else "data/gastos.csv"

    try:
        dados = pd.read_csv(origem)
    except (pd.errors.EmptyDataError, pd.errors.ParserError, UnicodeDecodeError) as erro:
        raise ValueError("Não foi possível ler o arquivo CSV enviado.") from erro

    dados.columns = dados.columns.str.strip()

    if "Valor" in dados.columns:
        try:
            dados["Valor"] = pd.to_numeric(dados["Valor"])
        except (TypeError, ValueError) as erro:
            raise ValueError("A coluna 'Valor' deve conter apenas números.") from erro

    return dados


def calcular_resumo(dados):
    """Separa receitas e gastos e calcula os principais indicadores."""
    gastos = dados[dados["Valor"] < 0]
    receitas = dados[dados["Valor"] > 0]
    total_receitas = receitas["Valor"].sum()
    total_gastos = gastos["Valor"].abs().sum()
    saldo = total_receitas - total_gastos

    return gastos, receitas, total_receitas, total_gastos, saldo


def analisar_categorias(gastos):
    """Agrupa e ordena os gastos por categoria."""
    return (
        gastos.groupby("Categoria")["Valor"]
        .sum()
        .abs()
        .sort_values()
    )


def criar_grafico(gastos_categoria):
    """Cria o gráfico de barras dos gastos por categoria."""
    if gastos_categoria.empty:
        return None

    fig, eixo = plt.subplots(figsize=(8, 5))
    eixo.bar(
        gastos_categoria.index,
        gastos_categoria.values,
        color="#C0392B",
    )
    eixo.set_title("Gastos por categoria")
    eixo.set_xlabel("Categoria")
    eixo.set_ylabel("Valor (R$)")
    eixo.tick_params(axis="x", rotation=45)
    eixo.grid(axis="y", linestyle="--", alpha=0.4)
    fig.tight_layout()

    return fig


def criar_pizza(gastos_categoria):
    """Cria o gráfico de distribuição percentual dos gastos."""
    if gastos_categoria.empty:
        return None

    fig, eixo = plt.subplots(figsize=(8, 5))
    eixo.pie(
        gastos_categoria.values,
        labels=gastos_categoria.index,
        autopct="%.1f%%",
        startangle=90,
    )
    eixo.set_title("Distribuição dos gastos")
    fig.tight_layout()

    return fig
