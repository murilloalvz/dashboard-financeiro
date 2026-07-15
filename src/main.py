import pandas as pd
import matplotlib.pyplot as plt

def carregar_dados(arquivo):
    if arquivo is None:
        dados = pd.read_csv("data/gastos.csv")
    else:
        dados = pd.read_csv(arquivo)
    
    return dados

def calcular_resumo(dados):
    gastos = dados[dados["Valor"] < 0]
    receitas = dados[dados["Valor"] > 0]
    total_receitas = receitas["Valor"].sum()
    total_gastos = gastos["Valor"].abs().sum()
    saldo = total_receitas - total_gastos
    
    return gastos, receitas, total_receitas, total_gastos, saldo 

def analisar_categorias(gastos):
    gastos_categoria = (
        gastos.groupby("Categoria")["Valor"]
        .sum()
        .abs()
        .sort_values()
        )                                                                                                                                                   
    
    return gastos_categoria 

def criar_grafico(gastos_categoria):
    if gastos_categoria.empty:
        return None
    
    fig = plt.figure(figsize=(8,5))

    plt.bar(
        gastos_categoria.index,
        gastos_categoria.values,
        color="red"
    )

    plt.title("Gastos Por Categoria")
    plt.xlabel("Categoria")
    plt.ylabel("Valor (R$)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    return fig

def criar_pizza(gastos_categoria):
    if gastos_categoria.empty:
        return None
     
    fig2 = plt.figure(figsize=(8,5))

    plt.pie(
        gastos_categoria.values,
        labels = gastos_categoria.index,
        autopct= "%.1f%%"
    ) 

    plt.tight_layout()
    
    return fig2
      
def main():
    dados = carregar_dados()

    gastos, receitas, total_receitas, total_gastos, saldo  = calcular_resumo(dados)

    gastos_categoria = analisar_categorias(gastos)

    criar_grafico(gastos_categoria)
    
    print("\nReceitas:")
    print(receitas)

    print("\nGastos:")
    print(gastos)

    print(f"\nTotal de Receitas: R${total_receitas:.2f}")
    print(f"\nTotal de Gastos: R${total_gastos:.2f}")
    print(f"\nSaldo: R$ {saldo:.2f}")

    print("\nGastos por categoria:")
    print(gastos_categoria)


if __name__ == "__main__":
    main()
   








