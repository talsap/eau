/*****************************************************************
* Medicao de deformações com o Transdutor Linear e Arduino somente
* ----------------------------------------------------------------
* created by: Tarcisio Sapucaia - tarcisiosapucaia27@gmail.com
* Data – 02/07/2019 - v 1.0
******************************************************************/
/* Import das Bibliotecas */
#include <Wire.h>

/* Variaveis*/
Int ad0 = 0, PINO = 0;
char conexao = 0, cond = 0;
double a = 0.0010290135, b = 1.7844684224, valor;  
//a e b são coeficientes angular e linear da curva de calibração respectivamente

void setup(void) {
  /* inicializa a serial */
  Serial.begin(9600);
}

void loop(void) {

  conexao = Serial.read();
   
  if  (conexao == 67){  
    //caso receba C = 67 em decimal (verifica se há conexao com a porta serial)
    Serial.begin(9600);
    Serial.println("conectado");
    Serial.flush();
    cond = 1;
    }
  
  if (conexao == 68){               
    //caso receba D = 68 em decimal (implica na desconexao com a porta serial)
    Serial.println("desconectado");
    Serial.flush();
    Serial.end();
    cond = 0;    
    }

  if (conexao == 73 && cond == 1){         
    //caso receba I = 73 em decimal (envia o dado do transdutor para porta serial)
    ad0 = analogRead(PINO);
    valor = a*ad0+b;
    Serial.println(valor,3);
    Serial.flush();
    }
}
