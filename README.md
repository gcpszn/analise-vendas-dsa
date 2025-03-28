Análise de Vendas - Projeto 2 - Data Science Academy
Este repositório contém um projeto de análise de dados de vendas, utilizando Python e as bibliotecas pandas, numpy, matplotlib e seaborn. O objetivo é explorar um dataset de vendas e responder a perguntas de negócios cruciais para a análise de desempenho de vendas.

Perguntas de Negócio
1. Qual cidade com maior valor de venda de produtos da categoria 'Office Supplies'?
python
Copiar
Editar
df_dsa_p1 = df_dsa[df_dsa['Categoria'] == 'Office Supplies']
df_dsa_p1_total = df_dsa_p1.groupby('Cidade')['Valor_Venda'].sum()
cidade_maior_venda = df_dsa_p1_total.idxmax()
print("Cidade com maior valor de venda para 'Office Supplies':", cidade_maior_venda)
2. Qual o total de vendas por data do pedido?
python
Copiar
Editar
df_dsa_p2 = df_dsa.groupby('Data_Pedido')['Valor_Venda'].sum()
df_dsa_p2.plot(x='Data_Pedido', y='Valor_Venda', color='green')
plt.title('Total de Vendas por Data do Pedido')
plt.show()
3. Qual o total de vendas por estado?
python
Copiar
Editar
df_dsa_p3 = df_dsa.groupby('Estado')['Valor_Venda'].sum().reset_index()
sns.barplot(data=df_dsa_p3, y='Valor_Venda', x='Estado').set(title='Vendas Por Estado')
plt.xticks(rotation=80)
plt.show()
4. Quais são as 10 cidades com maior total de vendas?
python
Copiar
Editar
df_dsa_p4 = df_dsa.groupby('Cidade')['Valor_Venda'].sum().reset_index().sort_values(by='Valor_Venda', ascending=False).head(10)
sns.barplot(data=df_dsa_p4, y='Valor_Venda', x='Cidade').set(title='As 10 Cidades com Maior Total de Vendas')
plt.show()
5. Qual segmento teve o maior total de vendas?
python
Copiar
Editar
df_dsa_p5 = df_dsa.groupby('Segmento')['Valor_Venda'].sum().reset_index().sort_values(by='Valor_Venda', ascending=False)
plt.pie(df_dsa_p5['Valor_Venda'], labels=df_dsa_p5['Segmento'], autopct='%1.1f%%', startangle=90)
plt.title('Total de Vendas Por Segmento')
plt.show()
6. Qual o total de vendas por segmento e por ano?
python
Copiar
Editar
df_dsa['Ano'] = df_dsa['Data_Pedido'].dt.year
df_dsa_p6 = df_dsa.groupby(['Ano', 'Segmento'])['Valor_Venda'].sum()
print(df_dsa_p6)
7. Quantas vendas receberiam 15% de desconto?
python
Copiar
Editar
df_dsa['Desconto'] = np.where(df_dsa['Valor_Venda'] > 1000, 0.15, 0.10)
print(df_dsa['Desconto'].value_counts())
8. Qual seria a média do valor de venda antes e depois do desconto de 15%?
python
Copiar
Editar
df_dsa['Valor_Venda_Desconto'] = df_dsa['Valor_Venda'] - (df_dsa['Valor_Venda'] * df_dsa['Desconto'])
media_vendas_antes_desconto = df_dsa[df_dsa['Desconto'] == 0.15]['Valor_Venda'].mean()
media_vendas_depois_desconto = df_dsa[df_dsa['Desconto'] == 0.15]['Valor_Venda_Desconto'].mean()
print("Média das vendas antes do desconto de 15%:", media_vendas_antes_desconto)
print("Média das vendas depois do desconto de 15%:", media_vendas_depois_desconto)
9. Qual a média de vendas por segmento, por ano e por mês?
python
Copiar
Editar
df_dsa['Mês'] = df_dsa['Data_Pedido'].dt.strftime('%m')
df_dsa_p9 = df_dsa.groupby(['Ano', 'Mês', 'Segmento'])['Valor_Venda'].agg([np.sum, np.mean, np.median])
sns.relplot(kind='line', data=df_dsa_p9, y='mean', x='Mês', hue='Segmento', col='Ano', col_wrap=4)
plt.show()
10. Qual o total de vendas por categoria e subcategoria, considerando somente as top 12 subcategorias?
python
Copiar
Editar
df_dsa_p10 = df_dsa.groupby(['Categoria', 'SubCategoria']).sum(numeric_only=True).sort_values('Valor_Venda', ascending=False).head(12)
sns.pie(df_dsa_p10['Valor_Venda'], labels=df_dsa_p10['SubCategoria'])
plt.title('Total de Vendas Por Categoria e Top 12 SubCategorias')
plt.show()
Bibliotecas Utilizadas
pandas: Para manipulação e análise de dados.

numpy: Para operações numéricas e de agregação.

matplotlib: Para visualização gráfica dos dados.

seaborn: Para visualização gráfica aprimorada e análises estatísticas.
