import streamlit as st
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from database.datageneration import generate_data  # Carrega o dataset

# Configurações gerais
st.set_page_config(page_title='Análisede     Dados', layout='wide')
# Título do aplicativo
st.title('Exploração de Dados')

# ================================================# 1. Carregar os Dados# ================================================
st.header('1. Carregar os Dados')
# Carregar os dados gerados
df = generate_data()
# Mostrar os primeiros registros
st.subheader('Visualização dos Dados')
st.dataframe(df.head())

# ================================================# 2. Visão Geral dos Dados# ================================================
st.header('2. Visão Geral dos Dados')
# Informações sobre o DataFrame
st.subheader('Informações do DataFrame')
st.write('Dimensões do DataFrame:')
st.write(f'Linhas: {df.shape[0]}, Colunas: {df.shape[1]}')

st.subheader('Tipos de Dados')
# Converter os tipos de dados para string
df_types = pd.DataFrame({'Tipos de Dados': df.dtypes.astype(str)})
st.write(df_types)

# Verificar valores ausentes
st.subheader('Valores Ausentes')
st.write(df.isnull().sum())

# Estatísticas Descritivas
st.subheader('Estatísticas Descritivas')
st.write(df.describe())


# Verificar valores outliers
st.subheader('Outliers')
fig = plt.figure(figsize=(12,6))
sns.boxplot(data=df)
plt.title("Boxplot para detectar Outliers")
plt.xticks(rotation=45)

st.pyplot(fig)

st.write("Não há outliers significativos no dataset. Os outliers encontrados em produção, se referem a resultados diferentes")

# ================================================# 3. Análise Univariada# ================================================
st.header('3. Análise Univariada')

numeric_columns = ['Temperatura', 'Umidade','pH', 'Produção']
categorical_columns = ['N', 'P', 'K']

# Histogramas das variáveis numéricas
st.subheader('Distribuições das Variáveis Numéricas')
for col in numeric_columns:
    st.write(f'**{col}**')
    fig = px.histogram(df, x=col, nbins=30, title=f'Distribuição de {col}')
    st.plotly_chart(fig, use_container_width=True)

# Box plots das variáveis numéricas
st.subheader('Box Plots das Variáveis Numéricas')
for col in numeric_columns:
    st.write(f'**{col}**')
    fig = px.box(df,  y=col, title=f'Box Plot de {col}')
    st.plotly_chart(fig, use_container_width=True)

# Distribuição das variáveis categóricas
st.subheader('Distribuições das Variáveis Categóricas')
for col in categorical_columns:
    st.write(f'**{col}**')
    fig = px.histogram(df, x=col, title=f'Distribuição de {col}')
    st.plotly_chart(fig, use_container_width=True)


# ================================================# 4. Análise Bivariada# ================================================
st.header('4. Análise Bivariada')
    
# Gráficos de dispersão entre variáveis numéricas
st.subheader('Gráficos  de  Dispersão  entre  Variáveis Numéricas')
variable_pairs = [('Temperatura', 'Produção'),('pH', 'Produção'), ('Umidade', 'Produção'),('Temperatura', 'Umidade')]
for x_var, y_var in variable_pairs:
    st.write(f'**{x_var} vs {y_var}**')
    fig = px.scatter(df,x=x_var,y=y_var,color='Dispositivo',title=f'{y_var} vs {x_var}')
    st.plotly_chart(fig, use_container_width=True)

# Distribuição de Produção por Macronutrientes NPK
st.subheader('Distribuição de Produção por Fertilizante e Tipo de Solo')

# Por nivel de N
st.write('**Produção por N**')
fig = px.box(df, x='N', y='Produção', title='Distribuição de Produção por Nível de Nitrogênio')
st.plotly_chart(fig, use_container_width=True)

# Por nivel de P
st.write('**Produção por P**')
fig = px.box(df,x='P',y='Produção',title='Distribuição de Produção por P')
st.plotly_chart(fig, use_container_width=True)

# Por nivel de K
st.write('**Produção por K**')
fig = px.box(df,x='K',y='Produção',title='Distribuição de Produção por P')
st.plotly_chart(fig, use_container_width=True)

st.write("Podemos observar que os macronutrientes que mais influenciam na produção são N em nível médio, P em nível baixo. Enquanto K, influencia de forma mais branda a produção, sendo maior quando em nível médio")

# ================================================ 5. Análise de Correlação ================================================
st.header('5. Análise de Correlação')

# Mapa de calor de correlação
st.subheader('Mapa de Calor de Correlação')

df_encoded = df.copy()

# Codificar variáveis categóricas (NPK)
categorical_columns = ['N', 'P', 'K']  

for col in categorical_columns:
    if col in df.columns:
        # Converter categorias para numérico
        df_encoded[col] = pd.Categorical(df_encoded[col]).codes


numeric_cols = df.select_dtypes(include=[np.number]).columns
all_cols = list(numeric_cols) + categorical_columns


corr = df_encoded[all_cols].corr()


fig_heatmap, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax, fmt='.2f', 
            center=0, linewidths=0.5)
plt.title('Matriz de Correlação - Incluindo NPK (Codificado)')
st.pyplot(fig_heatmap)

st.write("Como podemos observar na matrix de correlação, temos correlação moderada entre temperatura e produção.")
st.write("Verificamos tambem que há alguma influencia dos macronutrientes, principalmente N e K.")


# ================================================ 6. Análise Multivariada# ================================================
st.header('6. Análise Multivariada')

# Pairplot das variáveis numéricas
st.subheader('Pair Plot das Variáveis Numéricas')

# Converter 'Fertilizante' e 'Tipo de Solo' em códigos numéricos para coloração
# df_encoded['Fertilizante'] = df_encoded['Fertilizante'].map({'Orgânico': 0, 'Sintético': 1})
df_encoded['N']   =   df_encoded['N'].map({'baixo': 0, 'medio': 1, 'alto': 2})
df_encoded['P']   =   df_encoded['P'].map({'baixo': 0, 'medio': 1, 'alto': 2})
df_encoded['K']   =   df_encoded['K'].map({'baixo': 0, 'medio': 1, 'alto': 2})

fig = sns.pairplot(df_encoded,vars=numeric_columns,hue='Dispositivo',diag_kind='kde',corner=True)
st.pyplot(fig)
