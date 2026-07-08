import pandas as pd

def carregar_dados():
    dados = pd.read_csv("data/gastos.csv")
    
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
        .sort_values()
        )
    
    return gastos_categoria 

def main():
    dados = carregar_dados()

    gastos, receitas, total_receitas, total_gastos, saldo  = calcular_resumo(dados)

    gastos_categoria = analisar_categorias(gastos)
    
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
   








