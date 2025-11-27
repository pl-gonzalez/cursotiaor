#include <Arduino.h>
#include "npk.h"


struct nivel_npk nivel_npk;
/**
 * Mede nivel de NPK
 */

int medir_N() {
    int nAlto = digitalRead(N_ALTO_PIN);
    int nMedio = digitalRead(N_MEDIO_PIN);
    int nBaixo = digitalRead(N_BAIXO_PIN);

    int nivel = 0;
    
    if (nAlto == 0){
        // strcpy(nivel_npk.n, "alto");
        strcpy(nivel_npk.n, "alto"); 

        return N_ALTO_PIN;
    }
    
    if (nMedio == 0){
        strcpy(nivel_npk.n, "medio");

        return N_OK;
    }
    
    if (nBaixo == 0){
        strcpy(nivel_npk.n, "baixo");

        return BAIXO_N;
    }
    
    return nivel;
}

int medir_P() {
  int pAlto = digitalRead(P_ALTO_PIN);
  int pMedio = digitalRead(P_MEDIO_PIN);
  int pBaixo = digitalRead(P_BAIXO_PIN);
  
  int nivel = 0;

  if (pAlto == 0){
    Serial.print("Nivel P Alto\t");
    strcpy(nivel_npk.p, "alto");

    return P_ALTO_PIN;
  }

  if (pMedio == 0){
    Serial.print("Nivel P Medio\t");
    strcpy(nivel_npk.p, "medio");

    return P_OK;
  }

  if (pBaixo == 0 ){
    Serial.print("Nivel P Baixo\t");
    strcpy(nivel_npk.p, "baixo");

    return BAIXO_P;
  }
  return nivel;

  
}
void init_npk(){
  pinMode(N_ALTO_PIN, INPUT_PULLUP);
  pinMode(N_MEDIO_PIN, INPUT_PULLUP);
  pinMode(N_BAIXO_PIN, INPUT_PULLUP);

  pinMode(P_ALTO_PIN, INPUT_PULLUP);
  pinMode(P_MEDIO_PIN, INPUT_PULLUP);
  pinMode(P_BAIXO_PIN, INPUT_PULLUP);

  pinMode(K_ALTO_PIN, INPUT_PULLUP);
  pinMode(K_MEDIO_PIN, INPUT_PULLUP);
  pinMode(K_BAIXO_PIN, INPUT_PULLUP);

}
int medir_K() {
    int kAlto = digitalRead(K_ALTO_PIN);
    int kMedio = digitalRead(K_MEDIO_PIN);
    int kBaixo = digitalRead(K_BAIXO_PIN);

    int nivel = 0;

    if (kAlto == 0){
        Serial.println("Nivel K Alto");
        strcpy(nivel_npk.k, "alto");

        return K_ALTO_PIN;
    }
    
    if (kMedio == 0){
        Serial.println("Nivel K Medio");
        strcpy(nivel_npk.k, "medio");

        return K_OK;
    }
    
    if (kBaixo == 0){
        Serial.println("Nivel K Baixo");
        strcpy(nivel_npk.k, "baixo");

        return BAIXO_K;
    }

    return nivel;
    
}


