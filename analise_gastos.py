import pandas as pd
import matplotlib.pyplot as plt
import os

# Verifica se o arquivo existe
if not os.path.exists('gastos.csv'):
    print("ERRO: Arquivo 'gastos.csv' não encontrado!")
    print("Certifique-se que ele está na mesma pasta que este script.")
    exit()

try:
    # Tenta ler o arquivo
    df = pd.read_csv('gastos.csv')
    
    # Remove espaços extras dos nomes das colunas
    df.columns = df.columns.str.strip()
    
    # Verifica se a coluna 'valor' existe antes de prosseguir
    if 'valor' not in df.columns:
        print("ERRO: A coluna 'valor' não foi encontrada no arquivo 'gastos.csv'!")
        print("Certifique-se de que o arquivo contém as colunas corretas.")
        exit()

    # Verifica se o DataFrame está vazio
    if df.empty:
        print("ERRO: O arquivo 'gastos.csv' está vazio!")
        exit()
    
    # Restante do seu código...
    print("📊 Registros de gastos:")
    print(df.head())
    
except pd.errors.EmptyDataError:
    print("ERRO: O arquivo 'gastos.csv' está vazio ou mal formatado!")
    print("Verifique se contém dados no formato correto.")
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")

# Análise estatística básica  
print("\n📈 Estatísticas dos gastos:")  
print(df["valor"].describe())  

# Soma dos gastos por categoria  
gastos_por_categoria = df.groupby("categoria")["valor"].sum().sort_values()  
print("\n💰 Gastos por categoria:")  
print(gastos_por_categoria)  

# Gera um gráfico  
gastos_por_categoria.plot(kind="barh", color="#4CAF50")  
plt.title("Gastos por Categoria (R$)")  
plt.xlabel("Valor Gasto")  
plt.tight_layout()  
plt.savefig("gastos_categoria.png")  # Salva o gráfico  
print("\n✅ Gráfico salvo como 'gastos_categoria.png'!")