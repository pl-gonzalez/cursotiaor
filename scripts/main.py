import time
from datetime import datetime, timedelta
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random

from mqtt.mqtt_client import conectar_mqtt
from servicos.previsao_api import consultar_open_meteo
from database.database import leituras,dispositivos_cadastrados,cadastrar_dispositivo
from database.datageneration import generate_data
from servicos.alertas import alertas
# from config import dados_mqtt


# Dashboard
st.set_page_config(page_title="Dashboard", layout="centered")
st.title("FarmTech Solutions")
previsao_api = consultar_open_meteo()
# st.write(previsao_api)

data_previsao = previsao_api['daily']['time']
prob_chuva = 70
temp_max = previsao_api['daily']['temperature_2m_max'][0]
temp_min = previsao_api['daily']['temperature_2m_min'][0]
if  prob_chuva > 60:
    st.write("Não é necessário irrigar hoje!")
    st.write(f"Probabilidade de chuva: {prob_chuva} %")

previsao_col1, previsao_col2, previsao_col3 = st.columns(3)

with previsao_col1:
    st.write(f"Temperatura Maxima: {temp_max}°C")
with previsao_col2:
    st.write(f"Temperatura Minima: {temp_min}°C")
with previsao_col3:    
    st.write(f"Probabilidade de Chuva: {prob_chuva}%")


lista_dispositivos = dispositivos_cadastrados()


mqtt = conectar_mqtt()
print(mqtt)
df = generate_data()
st.write(mqtt)


# columns para cada dispositivo 
st.subheader("Ultima Leitura:")
dados_dispositivos = leituras()

st.write(df)

# st.write(dados_dispositivos)


# st.write(dados_dispositivos)
# dispositivo_col1, dispositivo_col2 = st.columns(2)

### Esse é o card da ultima leitura

# id_dispositivo = dados_dispositivos.at[0, "ID_DEVICE"]
# cultura = dados_dispositivos.at[0, "NM_CULTURA"]
# temp_solo = dados_dispositivos.at[0, "VL_TEMPERATURA"]
# umidade_solo = dados_dispositivos.at[0, "VL_UMIDADE_SOLO"]
# ph_solo = dados_dispositivos.at[0, "VL_PH"]
# npk = dados_dispositivos.at[0, "NPK"]

# with dispositivo_col1:
#     st.write(f"Dispositivo: {id_dispositivo}")
#     st.write(f"Cultura: {cultura}")
#     st.write(f"Temperatura Solo: {temp_solo}°C")
#     st.write(f"Umidade do Solo: {umidade_solo}%")
#     st.write(f"pH do Solo: {ph_solo}")
#     st.write(f"Necessidade: {npk}")


# # columns para filtros por dispositivo, dia/sem/mes, e formato display
# ## Minimo display em tabela

# filtro_col1, filtro_col2, filtro_col3 = st.columns(3)

# with filtro_col1:
#     columns = dados_dispositivos["ID_DISPOSITIVO"].unique().tolist()

#     selec_disp = st.selectbox("Selecione o dispositivo", columns)

#     df_filtrado = dados_dispositivos[dados_dispositivos["ID_DISPOSITIVO"] == selec_disp]
#     df_combined = df_filtrado[['DATA_HORA_GRAVACAO', 'TEMP_SOLO', 'UMIDADE_SOLO']].copy()
#     df_combined = df_combined.set_index('DATA_HORA_GRAVACAO')

# with filtro_col2:
#      # Seleção do modo de visualização
#     modo_visualizacao = st.selectbox(
#         "Modo de Visualização",
#         options=["Gráficos", "Tabela"],
#         index=0  # Padrão em Gráficos
#     )

# if modo_visualizacao == "Gráficos":
# # Gráfico combinado
#     st.subheader("Temperatura e Umidade do Solo")
#     chart_combined = st.line_chart(
#         df_combined[['TEMP_SOLO', 'UMIDADE_SOLO']],
#         width='stretch'
#     )

#     st.subheader("pH do Solo")
#     chart_ph = df_filtrado[['PH_SOLO','DATA_HORA_GRAVACAO']]
#     chart_ph = chart_ph.set_index('DATA_HORA_GRAVACAO')
#     st.line_chart(
#         chart_ph['PH_SOLO'],
#         width='stretch'
#     )

# else:
#     st.write(df_filtrado)

# conectar_mqtt()
# Programa principal

# while True:

#     dados = ler_banco()

#     alerta_temperatura = dados.at[0, "temp_solo"]
#     alerta_umidade = dados.at[0, "umidade_solo"]
#     alerta_ph = dados.at[0, "ph_solo"]
#     alerta_npk = dados.at[0, "npk"]
 
#     # #printa primeira linha
#     # ultimo_registro(dados)

#     #printa tabela
#     # tabela(dados)

#     hoje = datetime.now()
#     # printa previsao do tempo
#     if hoje.hour == 7 and hoje.minute == 26:
#         # previsao = previsao_semana()

#         #printa alertas
#         # alertas(alerta_temperatura, alerta_umidade, alerta_ph, alerta_npk)

#         time.sleep(61)

#     # else:
#     #     if len(previsao) == 0:
#     #         #printa alertas
#     #         # alertas(alerta_temperatura, alerta_umidade, alerta_ph, alerta_npk)

#     #         # time.sleep(30)

#     #     else:
#     #         # printa previsao
#     #         print(f"\n{previsao["data"]}")
#     #         print(previsao["msg"])

#     #         #printa alertas
#     #         alertas(alerta_temperatura, alerta_umidade, alerta_ph, alerta_npk)

#     #         # time.sleep(30)

        
