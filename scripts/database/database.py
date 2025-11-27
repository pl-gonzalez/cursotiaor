import oracledb  
import pandas as pd
import os

from config import DB_CONFIG

def cadastrar_dispositivo(mqtt_data: dict) -> bool:
    try:
        # Efetua a conexão com o Usuário no servidor
        conn = oracledb.connect(
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'], 
            dsn=DB_CONFIG['dsn']
        )
        
        # Cria as instruções para cada módulo
        inst_cadastro = conn.cursor()

        # Nomes precisam ser identicos
        sql = f"""INSERT INTO T_FT_DEVICE (
            ID_DEVICE,
            NM_CULTURA)
                  VALUES({mqtt_data["id"]}, {mqtt_data["cultura"]})"""
        
        inst_cadastro.execute(sql)
        conn.commit()

    except Exception as e:
        # Informa o erro
        print("Erro: ", e)
        conexao = False

        inst_cadastro.close()
        conn.close()

        return conexao
    else:
        conexao = True

        inst_cadastro.close()
        conn.close()

        return conexao

def leituras() -> pd.DataFrame:
    try:
        conn = oracledb.connect(
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'], 
            dsn=DB_CONFIG['dsn']
        )
        
        cursor = conn.cursor()
        sql = """SELECT f.ID_DEVICE, d.NM_CULTURA, DT_REGISTRO, VL_TEMPERATURA, VL_UMIDADE_SOLO, ST_NITROGENIO, ST_FOSFORO, ST_POTASSIO, VL_PH, VL_IRRIGACAO
                FROM T_FT_DEVICE d
                JOIN T_FT_FIELD f
                ON d.ID_DEVICE = f.ID_DEVICE
                ORDER BY DT_REGISTRO DESC"""
        
        cursor.execute(sql)
        
        data = cursor.fetchall()

        dados_df = pd.DataFrame.from_records(data)
        
        cursor.close()
        conn.close()
        
        return dados_df
    
    except Exception as e:
        print("Erro: ", e)
        try:
            cursor.close()
            conn.close()
        except:
            pass
        return pd.DataFrame()  # Retorna DataFrame vazio

def dispositivos_cadastrados() -> list:
    try:
        conn = oracledb.connect(
           user=DB_CONFIG['user'],
            password=DB_CONFIG['password'], 
            dsn=DB_CONFIG['dsn']
        )
        
        cursor = conn.cursor()
        sql = """SELECT * 
                FROM T_FT_DEVICE"""
        
        cursor.execute(sql)
        
        data = cursor.fetchall()

        dados_df = pd.DataFrame.from_records(data)
        
        cursor.close()
        conn.close()
        
        return dados_df
    
    except Exception as e:
        print("Erro: ", e)
        try:
            cursor.close()
            conn.close()
        except:
            pass
        return []
    
def gravar_leitura(mqtt_data: dict) -> bool:
    
    try:
        # Efetua a conexão com o Usuário no servidor
        conn = oracledb.connect(
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'], 
            dsn=DB_CONFIG['dsn']
        )
        
        # Cria as instruções para cada módulo
        inst_cadastro = conn.cursor()

        # -------- verifica se ID informado esta em T_FT_DEVICE em ID_DEVICE

        # ------- Atualizar insert para tabela field, se dispositivo estiver cadastrado

        leitura_campo = {
            "id": mqtt_data['id'],
            # "data": datetime.now(), ---> Nao é necessário pois horario sera dado pelo banco
            "temperatura": mqtt_data['temperatura'],
            "umidade": mqtt_data['umidade'],
            "n": mqtt_data['n'],
            "p": mqtt_data['p'],
            "k": mqtt_data['k'],
            "ph": mqtt_data['ph'],
            "irrigacao": mqtt_data['irrigacao']
        }
        # Nomes precisam ser identicos
        sql = """INSERT INTO T_FT_FIELD (
            ID_DEVICE,
            VL_TEMPERATURA, 
            VL_UMIDADE_SOLO, 
            ST_NITROGENIO, 
            ST_FOSFORO, 
            ST_POTASSIO, 
            VL_PH, 
            VL_IRRIGACAO
        ) 
        VALUES(
            :id,
            :temperatura,
            :umidade,
            :n,
            :p,
            :k,
            :ph,
            :irrigacao
        )"""
        # VALUES(
        # 2602,
        # 32.4,
        # 48.5,
        # 'baixo',
        # 'alto',
        # 'medio',
        # 6.0, 
        # 30
        # )
        inst_cadastro.execute(sql, leitura_campo)
        conn.commit()

    except Exception as e:
        # Informa o erro
        print("Erro: ", e)
        conexao = False

        inst_cadastro.close()
        conn.close()

        return conexao
    else:
        conexao = True

        inst_cadastro.close()
        conn.close()

        return conexao
   