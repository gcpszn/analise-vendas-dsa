import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

caminho = "dados\dataset.csv"

# Carregar o dataset
df_dsa = pd.read_csv(caminho)

# Pergunta 1: Qual cidade com maior valor de venda de produtos da categoria 'Office Supplies'?
df_dsa_p1 = df_dsa[df_dsa['Categoria'] == 'Office Supplies']
df_dsa_p1_total = df_dsa_p1.groupby('Cidade')['Valor_Venda'].sum()
cidade_maior_venda = df_dsa_p1_total.idxmax()
print("Cidade com maior valor de venda para 'Office Supplies':", cidade_maior_venda)
df_dsa_p1_total.sort_values(ascending=False)
# Resposta: Cidade com maior valor de venda para 'Office Supplies': New York City

# Pergunta 2: Qual o total de vendas por data do pedido? 
df_dsa_p2 = df_dsa.groupby('Data_Pedido')['Valor_Venda'].sum()
print(df_dsa_p2.head())
# Plot
plt.figure(figsize=(20, 6))
df_dsa_p2.plot(x='Data_Pedido', y='Valor_Venda', color='green')
plt.title('Total de Vendas por Data do Pedido')
plt.show()

# Pergunta 3: Qual o total de vendas por estado? 
df_dsa_p3 = df_dsa.groupby('Estado')['Valor_Venda'].sum().reset_index()
# Plot
plt.figure(figsize=(16, 6))
sns.barplot(data=df_dsa_p3, y='Valor_Venda', x='Estado').set(title='Vendas Por Estado')
plt.xticks(rotation=80)
plt.show()

# Pergunta 4: Quais são as 10 cidades com maior total de vendas?
df_dsa_p4 = df_dsa.groupby('Cidade')['Valor_Venda'].sum().reset_index().sort_values(by='Valor_Venda', ascending=False).head(10)
print(df_dsa_p4.head(10))
# Plot
plt.figure(figsize=(16, 6))
sns.set_palette('coolwarm')
sns.barplot(data=df_dsa_p4, y='Valor_Venda', x='Cidade').set(title='As 10 Cidades com Maior Total de Vendas')
plt.show()

# Pergunta 5: Qual segmento teve o maior total de vendas? 
df_dsa_p5 = df_dsa.groupby('Segmento')['Valor_Venda'].sum().reset_index().sort_values(by='Valor_Venda', ascending=False)
print(df_dsa_p5.head())
# Função para converter os dados em valor absoluto
def autopct_format(values):
    def my_format(pct):
        val = int(round(pct * total / 100.0))
        return ' $ {v:d}'.format(v=val)
    return my_format
# Plot
plt.figure(figsize=(16, 6))
plt.pie(df_dsa_p5['Valor_Venda'], labels=df_dsa_p5['Segmento'], autopct=autopct_format(df_dsa_p5['Valor_Venda']), startangle=90)
# Limpa o círculo central 
centre_circle = plt.Circle((0, 0), 0.82, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
# Labels e anotações
plt.annotate(text='Total de Vendas: ' + '$ ' + str(int(sum(df_dsa_p5['Valor_Venda']))), xy=(-0.25, 0))
plt.title('Total de Vendas Por Segmento')
plt.show()

# Pergunta 6: Qual o total de vendas por segmento e por ano? 
df_dsa['Data_Pedido'] = pd.to_datetime(df_dsa['Data_Pedido'], dayfirst=True)
df_dsa['Ano'] = df_dsa['Data_Pedido'].dt.year
df_dsa_p6 = df_dsa.groupby(['Ano', 'Segmento'])['Valor_Venda'].sum()
print(df_dsa_p6)

# Pergunta 7: Quantas vendas receberiam 15% de desconto?
# Se o Valor_Venda for maior que 1000 recebe 15% de desconto.
# Se o Valor_Venda for menor que 1000 recebe 10% de desconto.
df_dsa['Desconto'] = np.where(df_dsa['Valor_Venda'] > 1000, 0.15, 0.10)
print(df_dsa.head()) 
print(df_dsa['Desconto'].value_counts())
print('No Total 457 Vendas Receberiam Desconto de 15%.')

# Pergunta 8: Qual seria a média do valor de venda antes e depois do desconto de 15%? 
df_dsa['Valor_Venda_Desconto'] = df_dsa['Valor_Venda'] - (df_dsa['Valor_Venda'] * df_dsa['Desconto'])
print(df_dsa.head())

df_dsa_p8_vendas_antes_desconto = df_dsa.loc[df_dsa['Desconto'] == 0.15, 'Valor_Venda']
df_dsa_p8_vendas_depois_desconto = df_dsa.loc[df_dsa['Desconto'] == 0.15, 'Valor_Venda_Desconto']

media_vendas_antes_desconto = df_dsa_p8_vendas_antes_desconto.mean()
media_vendas_depois_desconto = df_dsa_p8_vendas_depois_desconto.mean()

print("Média das vendas antes do desconto de 15%:", round(media_vendas_antes_desconto, 2))
print("Média das vendas depois do desconto de 15%:", round(media_vendas_depois_desconto, 2))

# Pergunta 9: Qual a média de vendas por segmento, por ano e por mês?
df_dsa['Mês'] = df_dsa['Data_Pedido'].dt.strftime('%m')
df_dsa_p9 = df_dsa.groupby(['Ano', 'Mês', 'Segmento'])['Valor_Venda'].agg([np.sum, np.mean, np.median])
print(df_dsa_p9)

anos = df_dsa_p9.index.get_level_values(0)
meses = df_dsa_p9.index.get_level_values(1)
segmentos = df_dsa_p9.index.get_level_values(2)

# Plot 
plt.figure(figsize=(12, 6))
sns.set()
fig1 = sns.relplot(kind='line', data=df_dsa_p9, y='mean', x=meses, hue=segmentos, col=anos, col_wrap=4)
plt.show()

# Pergunta 10: Qual o total de vendas por categoria e subcategoria, considerando somente as top 12 subcategorias?
df_dsa_p10 = df_dsa.groupby(['Categoria', 'SubCategoria']).sum(numeric_only=True).sort_values('Valor_Venda', ascending=False).head(12)
df_dsa_p10 = df_dsa_p10[['Valor_Venda']].astype(int).sort_values(by='Categoria').reset_index()

df_dsa_p10_cat = df_dsa_p10.groupby('Categoria').sum(numeric_only=True).reset_index()

# Cores para as categorias e subcategorias
cores_categorias = ['#5d00de', '#0ee84f', '#e80e27']
cores_subcategorias = ['#aa8cd4', '#aa8cd5', '#aa8cd6', '#aa8cd7', '#26c957', '#26c958', '#26c959', '#26c960',
                       '#e65e65', '#e65e66', '#e65e67', '#e65e68']

# Função para formatação do gráfico de pizza
def autopct_format(valor, valores):
    total = sum(valores)
    valor_em_dolar = valor * total / 100  # Calculando o valor absoluto para cada fatia
    return '${:.0f}'.format(valor_em_dolar)

# Plot
fig, ax = plt.subplots(figsize=(18, 12))

# Gráfico das categorias
p1 = ax.pie(df_dsa_p10_cat['Valor_Venda'], 
            radius=1,
            labels=df_dsa_p10_cat['Categoria'],
            wedgeprops=dict(edgecolor='white'),
            colors=cores_categorias)

# Gráfico das subcategorias
p2 = ax.pie(df_dsa_p10['Valor_Venda'],
            radius=0.9,
            labels=df_dsa_p10['SubCategoria'],
            autopct=lambda p: autopct_format(p, df_dsa_p10['Valor_Venda']),  # Agora mostrando o valor em $
            colors=cores_subcategorias,
            labeldistance=0.7,
            wedgeprops=dict(edgecolor='white'),
            pctdistance=0.53,
            rotatelabels=True)

# Limpar o centro do gráfico (fazendo ele parecer um gráfico de pizza com buraco no meio)
centre_circle = plt.Circle((0, 0), 0.6, fc='white')
fig.gca().add_artist(centre_circle)

# Adicionar o total de vendas no centro do gráfico
plt.annotate(text='Total de Vendas: $' + str(int(sum(df_dsa_p10['Valor_Venda']))), xy=(-0.2, 0), fontsize=14, color='black', weight='bold')

# Título do gráfico
plt.title('Total de Vendas Por Categoria e Top 12 SubCategorias')

# Exibir o gráfico
plt.show()
