import numpy as np
import pandas as pd
import streamlit as st

@st.cache_data(show_spinner=True) 
## usando cache
def generate_data(n_samples=1000):
    """Gera um dataset simulado de produção agrícola.Args:n_samples  (int):  Número  de  amostras  a  serem geradas.Returns:pd.DataFrame:   DataFrame   contendo   o   dataset simulado."""
    inicio = '2025-11-09 00:00:00'
    np.random.seed(42)
    #  Gerando  variáveis  climáticas  com  distribuições realistas

    # Temperatura média de 22°C
    temperatura   =   np.random.normal(loc=22,   scale=3, size=n_samples)  
    
    # Precipitação em mm
    # precipitacao  =  np.random.gamma(shape=2,  scale=30, size=n_samples)  
    
    # Umidade relativa em %
    umidade    =    np.random.uniform(low=50,    high=80, size=n_samples)  

    # nivel pH
    ph = np.random.uniform(low=4,    high=10, size=n_samples)
    
    # Variáveis categóricas
    # fertilizante     =     np.random.choice(['Orgânico', 'Sintético'], size=n_samples, p=[0.4, 0.6])
    nivel_n = np.random.choice(['baixo', 'medio', 'alto'], size=n_samples, p=[0.3, 0.5, 0.2])
    nivel_p = np.random.choice(['baixo', 'medio', 'alto'], size=n_samples, p=[0.3, 0.5, 0.2])
    nivel_k = np.random.choice(['baixo', 'medio', 'alto'], size=n_samples, p=[0.3, 0.5, 0.2])

    # Gerando id de dispositivos
    id_device = np.random.choice(['2602', '5409', '2111', '1366'], size=n_samples)

    # Mapear categorias para valores numéricos (efeitos)

    # npk ideal (basico) --> 20 - 00 - 20 (fases de crescimento desconsideradas)

    mapa_n  =  {'baixo': 0.55, 'medio': 1.15, 'alto': 0.9}
    mapa_p  =  {'baixo': 1.15, 'medio': 0.3, 'alto': 0.1}
    mapa_k  =  {'baixo': 0.55, 'medio': 1.15, 'alto': 0.9}
    # efeito_fertilizante = np.vectorize(mapa_fertilizante.get)(fertilizante)
    n = np.vectorize(mapa_n.get)(nivel_n)
    p = np.vectorize(mapa_p.get)(nivel_p)
    k = np.vectorize(mapa_k.get)(nivel_k)
    # Calculando a produção com interações mais realistas
    producao = ((temperatura -20) * 2 +  # Aumento de produção por temperatura acima de 20°C
                (umidade -50) * 0.3 + # Aumento por umidade acima de 50%
                (ph - 6) * 0.2 # Aumento por pH acima de 6
                ) * (n * p * k) # Aumento pela combinação dos niveis de npk
    
    # Adicionando variabilidade aleatória
    producao += np.random.normal(loc=5,    scale=5, size=n_samples)
    # Garantindo que a produção não seja negativa
    producao = np.clip(producao, a_min=0, a_max=None)
    # Criando o DataFrame final
    df = pd.DataFrame({'Dispositivo': id_device,'data_hora': pd.date_range(start=inicio, periods=1000, freq='H'), 'Temperatura': temperatura,'Umidade': umidade, 'N': nivel_n, 'P': nivel_p, 'K': nivel_k, 'pH': ph, 'Produção': producao})
    
    return df