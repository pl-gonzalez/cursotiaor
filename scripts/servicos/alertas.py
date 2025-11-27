def alertas(alerta_temperatura: float, alerta_umidade: float, alerta_ph: float, alerta_npk: str) -> None:
    print("\n")
    #'data_hora_gravacao','id_dispositivo', 'cultura', 'temp_solo', 'umidade_solo', 'ph_solo', 'npk'

    if(alerta_temperatura > 35): print("[    ATENÇÃO    ] --> Temperatura do solo Alta!")
    if(alerta_umidade < 50): print("[    ATENÇÃO    ] --> Solo em escassez hidrica. Umidade abaixo de 50%!")
    if(alerta_ph < 5): print("[    ATENÇÃO    ] --> pH do solo está muito baixo")
    
    match alerta_npk:
        case 'NPK':
            print("[    ATENÇÃO    ] --> Repor macronutrientes NPK")
            return
        case 'NP':
            print("[    ATENÇÃO    ] --> Repor macronutrientes NP")
            return
        case 'NK':
            print("[    ATENÇÃO    ] --> Repor macronutrientes NK")
            return
        case 'PK':
            print("[    ATENÇÃO    ] --> Repor macronutrientes PK")
            return
        case 'N':
            print("[    ATENÇÃO    ] --> Repor macronutriente N")
            return
        case 'P':
            print("[    ATENÇÃO    ] --> Repor macronutriente P")
            return
        case 'K':
            print("[    ATENÇÃO    ] --> Repor macronutriente K")
            return
        

