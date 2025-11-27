import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error, r2_score
from database.datageneration import generate_data  

# Configurações gerais
st.set_page_config(page_title='Modelagem Preditiva', layout='wide')
# Título do aplicativo
st.title('Modelagem Preditiva')
df = generate_data()
# ================================================# 1. Carregar  os Dados# ================================================

st.subheader('Amostra dos dados')
st.write(df.head())


# ================================================# 2. Preparar os Dados para Modelagem# ================================================

st.subheader("Previsão")

# Transformar variáveis categóricas em variáveis dummies
df_ml   =  pd.get_dummies(df, columns=['N', 'P', 'K'])

#  Separar  as  variáveis  independentes  (X)  e  a  variável dependente (y)
X = df_ml.drop(['Produção', 'data_hora'], axis=1)
y = df_ml['Produção']

# ================================================# 3. Treinar o Modelo de Machine Learning# ================================================

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Instanciar o modelo de Random Forest Regressor
model = LinearRegression()
# Treinar o modelo com os dados de treinamento
model.fit(X_train, y_train)

# ================================================# 4. Fazer Previsões com o Modelo# ================================================

st.write('Insira os valores de temperatura, umidade, pH, e macronutrientes NPK desejados para prever quantidade de produção')

# Coletar entrada do usuário para previsão
temp_input = st.number_input('Temperatura    (°C)', value=float(df['Temperatura'].mean()))
ph_input = st.number_input('pH', value=float(df['pH'].mean()))
umidade_input    =    st.number_input('Umidade    (%)', value=float(df['Umidade'].mean()))
# fertilizante_input     =     st.selectbox('Fertilizante', df['Fertilizante'].unique())
n_input  =  st.selectbox('N',  df['N'].unique())
p_input  =  st.selectbox('P',  df['P'].unique())
k_input  =  st.selectbox('K',  df['K'].unique())

# ----------------------------------# 4.1. Validar Entradas do Usuário# ----------------------------------
# # Inicializar variável de controle
input_error = False
# Validar temperatura
if not(-10<= temp_input <= 50):
    st.error('A  temperatura  deve  estar  entre -10°C  e 50°C.')
    input_error = True
# Validar precipitação
if not(0<= ph_input <= 14):
    st.error('O pH deve ser entre 0 e 14.')
    input_error = True
# Validar umidade
if not(0<= umidade_input <= 100):
    st.error('A umidade deve ser entre 0% e 100%.')
    input_error = True

#  Se  não  houver  erros  nas  entradas,  proceder  com  a previsão
if not input_error:
    
    # ----------------------------------# 4.2. Preparar os Dados de Entrada# ----------------------------------
    # Criar um dicionário com os dados de entrada
    input_data = {
        'Temperatura': [temp_input],
        'pH': [ph_input],
        'Umidade': [umidade_input],
        # Variáveis dummies para NPK
        'N_baixo': [1 if n_input == 'baixo' else 0],
        'N_medio': [1 if n_input == 'medio' else 0],
        'N_alto': [1 if n_input == 'alto' else 0],
        'P_baixo': [1 if p_input == 'baixo' else 0],
        'P_medio': [1 if p_input == 'medio' else 0],
        'P_alto': [1 if p_input == 'alto' else 0],
        'K_baixo': [1 if k_input == 'baixo' else 0],
        'K_medio': [1 if k_input == 'medio' else 0],
        'K_alto': [1 if k_input == 'alto' else 0],
    }

    # Converter o dicionário em um DataFrame
    input_df = pd.DataFrame(input_data)
    # Garantir que todas as colunas necessárias estejam presentes
    for col in X.columns:
        if col not in input_df.columns:
            input_df[col]  = 0
            #  Adicionar  coluna  com valor zero
            # Reordenar as colunas para corresponder ao conjunto de treinamento
            input_df = input_df[X.columns]

    # ----------------------------------# 4.3. Realizar a Previsão# ----------------------------------
    # # Fazer a previsão com o modelo treinado
    # prediction = model.predict(X_test)
    # Exibir o resultado da previsão
    y_pred = model.predict(X_test)

    # Calcular métricas de regressão
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    # Exibir no Streamlit
    st.subheader("📈 Métricas de Avaliação - Regressão Linear")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("MSE", f"{mse:.2f}")
    col2.metric("RMSE", f"{rmse:.2f}") 
    col3.metric("MAE", f"{mae:.2f}")
    col4.metric("R²", f"{r2:.2f}")
    st.subheader('Resultado da Previsão') 
    st.write(f'Previsão de Produção:   {y_pred[0]:.2f} ton/ha')

   