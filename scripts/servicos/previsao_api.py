import datetime
import requests
import time

from config import API_URL
# Retorna dados em JSON
def consultar_open_meteo() -> dict:
    response = requests.get(API_URL)
        
    data = response.json()

    return data

def horario_previsão():
    previsao = datetime.datetime.now()

    # Todo dia, as 06:30H, é realizada uma consulta a OpenMeteo API para termos previsão do tempo, chuva e temperaturas maxima e minima
    if previsao.hour == 6 and previsao.minutes == 0:
        data = consultar_open_meteo()
        # Para evitar rodar varias vezes no mesmo minuto
        time.sleep(5 * 60)
        
        

    else:
        # Espera 30 segundos e verifica de novo
        time.sleep(30)

# f'{dados_api['daily']['time'][0]};{dados_api['daily']['temperature_2m_min'][0]};{dados_api['daily']['temperature_2m_max'][0]};{dados_api['daily']['precipitation_probability_max'][0]}'