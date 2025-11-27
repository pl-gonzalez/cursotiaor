# Central apenas recebe informações MQTT, por isso nao tem pub
# e fica sempre aguardando publicação no topico inscrito
from datetime import datetime, timedelta

from config import BROKER, PORT, TOKEN, CLIENT_ID, TOPIC 
import paho.mqtt.client as mqtt
from database.database import gravar_leitura
import streamlit as st
import pandas as pd 

ultima_mensagem = None

# Callback quando conecta
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe(TOPIC)
    else:
        print(f"Falha na conexão. Código: {rc}")

# Callback quando recebe mensagem
def on_message(client, userdata, msg):
    global ultima_mensagem
    try:
        payload = msg.payload.decode()  # converte bytes -> string

        valores = payload.split(";")
        
        # Converte para dicionário
        # INPUT: 2602; cande-de-acucar; 19.7; 43.0; 6.0; baixo; medio; alto; 30;
        dados_mqtt = {
            "id": int(valores[0]),
            # "data": datetime.now(), ---> Nao é necessário pois horario sera dado pelo banco
            "cultura": valores[1],
            "temperatura": float(valores[2]),
            "umidade": float(valores[3]),
            "n": str(valores[5]),
            "p": str(valores[6]),
            "k": str(valores[7]),
            "ph": float(valores[4]),
            "irrigacao": int(valores[8])
        }
        print(dados_mqtt)

        gravar_leitura(dados_mqtt)
               
        ultima_mensagem = dados_mqtt

        return dados_mqtt
    except Exception as e:
        print("Erro ao processar mensagem:", e)



def conectar_mqtt():
    client = mqtt.Client(client_id=CLIENT_ID)
    client.username_pw_set(TOKEN)
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.reconnect_delay_set(min_delay=1, max_delay=300)
    client.connect(BROKER, PORT, 60)
    client.loop_start() 

def on_disconnect(client, userdata, rc):
    if rc != 0:
        
        client.reconnect()

def get_ultima_mensagem():
    return ultima_mensagem