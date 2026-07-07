import pandas as pd

dados = pd.read_csv("data/gastos.csv")

gastos = dados[dados["Valor"] < 0]

receitas = dados[dados["Valor"] > 0]

print("\nReceitas:")
print(receitas)

print("\nGastos:")
print(gastos)

total_receitas = receitas["Valor"].sum()

total_gastos = gastos["Valor"].abs().sum()

saldo = total_receitas + total_gastos

print("\nTotal de receitas:", total_receitas)
print("Total de gastos:", total_gastos)
print("Saldo:", saldo)

gastos_categoria = (gastos.groupby("Categoria")["Valor"].sum().sort_values())

print(gastos_categoria)

