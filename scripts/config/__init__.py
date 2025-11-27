# MQTT Configuration
BROKER = "mqtt.flespi.io"
PORT = 1883
TOKEN = "REXKZChIGcRtbVYjdLnbEuzqo3E0mhncce6ejwdNdtxZbqQa7yVjvcquteAPykbK" # Substitua pelo seu token do Flespi
CLIENT_ID = "COORDENADOR"
TOPIC = "central"
dados_mqtt = {}

# Database Configuration
DB_CONFIG = {
    'user': 'rm567944',
    'password': '260299',
    'dsn': 'oracle.fiap.com.br:1521/ORCL'
}

# API Configuration
LAT = -23.55
LONG = -46.64
API_URL = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LONG}&daily=precipitation_probability_max,temperature_2m_min,temperature_2m_max&timezone=America%2FSao_Paulo&forecast_days=1"

# Alert Thresholds
LIMITES_ALERTAS = {
    'temperatura': 35,
    'umidade': 50,
    'ph': 5
}