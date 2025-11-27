#include <Arduino.h>
#include <WiFi.h>

#include "DHTesp.h"

#include "npk/npk.h"
#include "pH/ph.h"
#include "bomba/bomba.h"
#include "dht/dht.h"
#include "mqtt/mqtt.h"

DHTesp dhtSensor;

struct Dados dados;


#define ID "2602"
#define CULTURA "cana-de-acucar"

#define INTERVALO 10000

unsigned long lastUpdate = 0;


void setup() {
  Serial.begin(115200);

  dhtSensor.setup(DHT_PIN, DHTesp :: DHT22);
  init_mqtt();
  init_npk();
  init_bomba();
  init_ph();
  
  delay(1000);
  
}


void loop() {

  if (!client.connected()) {
        reconnect();
    }
    client.loop(); // mantém conexão e recebe mensagens

  // executa tarefas periodicamente sem travar o loop
    unsigned long now = millis();
    if (now - lastUpdate >= INTERVALO) {
        lastUpdate = now;

        
        if(dados.atualizado){
          
          Serial.print("Data: ");
          Serial.println(dados.date);
          Serial.print("Probabalidade de chuva: ");
          Serial.print(dados.probChuva);
          Serial.println("%");
          Serial.print("Temp. Minima: ");
          Serial.print(dados.tempMin);
          Serial.println("°C");
          Serial.print("Temp. Maxima: ");
          Serial.print(dados.tempMax);
          Serial.println("°C");
        }
        
        
        float temperatura = temp_umidade().temperature;
        float umidade = temp_umidade().humidity;
        float ph_solo = medir_ph_solo();
        
        Serial.print("pH: ");
        Serial.print(ph_solo);
        
        Serial.print("\t Temp. Solo: ");
        Serial.print(temperatura);
        
        Serial.print("\t Umidade solo (%): ");
        Serial.println(umidade);
        
        
        // Mediçoes de nivel de NPK retornam o estado de cada sensor
        int nivel_n = medir_N();
        int nivel_p = medir_P();
        int nivel_k = medir_K();
        

        /**
         * Umidade < 50% -> Estresse hidrico, irrigar agora
         * Temperatura > 35°C -> Muitoo quente para cana de açucar
         * 
         * @note: plantação será irrigada para manter umidade entre 50-70% e
         *  temperatura abaixo dos 35°C. As informações foram encontradas na internet.
         */
        char msg[128];
        
        if(umidade < 50.0f || (umidade < 70.0f && temperatura > 35.0f)){
          
          
          if(dados.probChuva < 60.f){

            if (nivel_n == BAIXO_N && nivel_p == BAIXO_P  && nivel_k == BAIXO_K) {
              aciona_bomba("Irrigação com N, P e K");
      
              sprintf(msg, "%s;%s;%.1f;%.1f;%.1f;%s;%s;%s;%d;",  
                ID, CULTURA, temperatura, umidade, ph_solo, nivel_npk.n, nivel_npk.p, nivel_npk.k, TEMPO_BOMBA);

              publica_mqtt(msg);
              // Serial.println(msg);
            }
            // se n p
            else if (nivel_n == BAIXO_N && nivel_p == BAIXO_P) {
              aciona_bomba("Irrigação com N e P");

              sprintf(msg, "%s;%s;%.1f;%.1f;%.1f;%s;%s;%s;%d;",  
                ID, CULTURA, temperatura, umidade, ph_solo, nivel_npk.n, nivel_npk.p, nivel_npk.k, TEMPO_BOMBA);

              publica_mqtt(msg);
              // Serial.println(msg);
            }
            // se n k
            else if (nivel_n == BAIXO_N && nivel_k == BAIXO_K) {
              aciona_bomba("Irrigação com N e K");
              sprintf(msg, "%s;%s;%.1f;%.1f;%.1f;%s;%s;%s;%d;", 
                ID, CULTURA, temperatura, umidade, ph_solo, nivel_npk.n, nivel_npk.p, nivel_npk.k, TEMPO_BOMBA);

              publica_mqtt(msg);
              // Serial.println(msg);
            }
            // se p k
            else if (nivel_p == BAIXO_P && nivel_k == BAIXO_K) {
              aciona_bomba("Irrigação com P e K");
              sprintf(msg, "%s;%s;%.1f;%.1f;%.1f;%s;%s;%s;%d;", 
                ID, CULTURA, temperatura, umidade, ph_solo, nivel_npk.n, nivel_npk.p, nivel_npk.k, TEMPO_BOMBA);

              publica_mqtt(msg);
              // Serial.println(msg);
            }
            // se n
            else if (nivel_n == BAIXO_N) {
              aciona_bomba("Irrigação com N");
              sprintf(msg, "%s;%s;%.1f;%.1f;%.1f;%s;%s;%s;%d;",  
                ID, CULTURA, temperatura, umidade, ph_solo, nivel_npk.n, nivel_npk.p, nivel_npk.k, TEMPO_BOMBA);

              publica_mqtt(msg);
              // Serial.println(msg);
            }
            // se p
            else if (nivel_p == BAIXO_P){ 
              aciona_bomba("Irrigação com P");
              sprintf(msg, "%s;%s;%.1f;%.1f;%.1f;%s;%s;%s;%d;",  
                ID, CULTURA, temperatura, umidade, ph_solo, nivel_npk.n, nivel_npk.p, nivel_npk.k, TEMPO_BOMBA);

              publica_mqtt(msg);
              // Serial.println(msg);
            }
            // se k
            else if (nivel_k == BAIXO_K) {
              aciona_bomba("Irrigação com K");
              sprintf(msg, "%s;%s;%.1f;%.1f;%.1f;%s;%s;%s;%d;",  
                ID, CULTURA, temperatura, umidade, ph_solo, nivel_npk.n, nivel_npk.p, nivel_npk.k, TEMPO_BOMBA);

              publica_mqtt(msg);
              // Serial.println(msg);
            }
       
            else if (ph_solo < 5.5f) {
              aciona_bomba("Irrigação com Cal para elevar pH");
              sprintf(msg, "%s;%s;%.1f;%.1f;%.1f;%s;%s;%s;%d;", 
                ID, CULTURA, temperatura, umidade, ph_solo, nivel_npk.n, nivel_npk.p, nivel_npk.k, TEMPO_BOMBA);

              publica_mqtt(msg);
              // Serial.println(msg);
            }

            else if(umidade < 50.0f || umidade < 70.0f) {
              aciona_bomba("Irrigação apenas com água");
              Serial.println(nivel_npk.n);
              sprintf(msg, "%s;%s;%.1f;%.1f;%.1f;%s;%s;%s;%d;",  
                ID, CULTURA, temperatura, umidade, ph_solo, nivel_npk.n, nivel_npk.p, nivel_npk.k, TEMPO_BOMBA);

              publica_mqtt(msg);
              // Serial.println(msg);
            }
          
          }
          else {
              // Como nao há necessidade de irrigar, TEMPO_BOMBA será 0, pois não havera irrgação
              sprintf(msg, "%s; %s; %.1f; %.1f; %.1f; %s; %s; %s; %d;", 
                ID, CULTURA, temperatura, umidade, ph_solo, nivel_npk.n, nivel_npk.p, nivel_npk.k, 0);

              publica_mqtt(msg);
              // Serial.println(msg);

          }
          
        }
        else {
              // Cenário onde leituras estao boas
              sprintf(msg, "%s;%s;%.1f;%.1f;%.1f;%s;%s;%s;%d;", 
                ID, CULTURA, temperatura, umidade, ph_solo, nivel_npk.n, nivel_npk.p, nivel_npk.k, TEMPO_BOMBA);

              publica_mqtt(msg);
              // Serial.println(msg);

          }
        
      }
}