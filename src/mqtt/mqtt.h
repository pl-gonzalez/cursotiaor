#ifndef MQTT_H
#define MQTT_H

#include <PubSubClient.h>


struct Dados{
    String date;
    float tempMin;
    float tempMax;
    int probChuva;
    bool atualizado;
};

extern WiFiClient espClient;
extern PubSubClient client;

extern struct Dados dados;



void init_mqtt();
void mqtt_loop();
void publica_mqtt(const char* msg);
void reconnect();


#endif