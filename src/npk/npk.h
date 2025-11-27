#ifndef NPK_H
#define NPK_H

#define N_ALTO_PIN 23
#define N_MEDIO_PIN 22
#define N_BAIXO_PIN 21

#define P_ALTO_PIN 19
#define P_MEDIO_PIN 18
#define P_BAIXO_PIN 5

#define K_ALTO_PIN 17
#define K_MEDIO_PIN 16
#define K_BAIXO_PIN 4

enum NivelNPK {
  N_OK,
  P_OK,
  K_OK,
  BAIXO_N,
  ALTO_N,
  BAIXO_P,
  ALTO_P,
  BAIXO_K,
  ALTO_K
};

enum Irrigar {
    IRRIGAR_AGUA,
    IRRIGAR_N,
    IRRIGAR_P,
    IRRIGAR_K,
    IRRIGAR_NPK,
    IRRIGAR_NP,
    IRRIGAR_NK,
    IRRIGAR_PK
};

struct nivel_npk{
    char n[10];
    char p[10];
    char k[10];
};

extern struct nivel_npk nivel_npk;


int medir_N();
int medir_P();
int medir_K();

void init_npk();


#endif
