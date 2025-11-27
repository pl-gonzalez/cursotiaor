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

st.subheader("Previsão do tempo para hoje:")

data_previsao = previsao_api['daily']['time']
prob_chuva = previsao_api['daily']['precipitation_probability_max'][0]
temp_max = previsao_api['daily']['temperature_2m_max'][0]
temp_min = previsao_api['daily']['temperature_2m_min'][0]

if  prob_chuva > 60:
    st.write("Não é necessário irrigar hoje!")
    st.write(f"Probabilidade de chuva: {prob_chuva} %")

previsao_col1, previsao_col2, previsao_col3 = st.columns(3)

with previsao_col1:
    st.metric("Temperatura Maxima" ,f"{temp_max}°C")
with previsao_col2:
    st.metric("Temperatura Minina", f"{temp_min}°C")
with previsao_col3:    
    st.metric("Probabilidade de Chuva", f"{prob_chuva}%")


lista_dispositivos = dispositivos_cadastrados()


mqtt = conectar_mqtt()
df = generate_data()


# columns para cada dispositivo 
st.subheader("Ultimas Leituras:")
dados_dispositivos = leituras()

st.write(df)


        
