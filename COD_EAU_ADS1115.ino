/*********************************************************************************************
* Medicao de deformações com o Transdutor Linear e conversor analogico digital ADS1115 (16-bit)
* --------------------------------------------------------------------------------------------
* based on: Haroldo Amaral - https://github.com/agaelema/ADS1115_and_LM35
* modified by: Tarcisio Sapucaia - tarcisiosapucaia27@gmail.com
* Data – 02/07/2019 - v 1.0
*********************************************************************************************/
/* Import das Bibliotecas */
#include <Wire.h>
#include <Adafruit_ADS1015.h>

/* Variaveis*/
int16_t adc0 = 0;
char conexao = 0, cond = 0;
double a = 0.0010290135, b = 1.7844684224, valor;  
//a e b são coeficientes angular e linear da curva de calibração respectivamente

/* cria instância do conversor analogico digital ADC */
Adafruit_ADS1115 ads(0x48);  /* Use esta para a versão de 16-bit */
//Adafruit_ADS1015 ads;     /* Use esta para a versão de 12-bit */

void setup(void) {
  /* inicializa a serial */
  Serial.begin(9600);
 
  // Configura o ganho do PGA interno do ADS1115
  // Sem configuração ele automaticamente na escala de +/- 6.144V
  // Lembre-se de não exceder os limites de tensao nas entradas
  // VDD + 0,3 v ou GND-0,3 v  
  //                                                     ADS1015          ADS1115
  //                                                     -------          -------
  ads.setGain(GAIN_TWOTHIRDS);  // 2/3x gain +/- 6.144V  1 bit = 3mV   0.1875mV (default)
  // ads.setGain(GAIN_ONE);     // 1x gain   +/- 4.096V  1 bit = 2mV      0.125mV
  // ads.setGain(GAIN_TWO);     // 2x gain   +/- 2.048V  1 bit = 1mV      0.0625mV
  // ads.setGain(GAIN_FOUR);    // 4x gain   +/- 1.024V  1 bit = 0.5mV    0.03125mV
  // ads.setGain(GAIN_EIGHT);   // 8x gain   +/- 0.512V  1 bit = 0.25mV   0.015625mV
  // ads.setGain(GAIN_SIXTEEN); // 16x gain  +/- 0.256V  1 bit = 0.125mV  0.0078125mV

  /* inicializa o ADC */
  ads.begin();
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
    adc0 = ads.readADC_SingleEnded(0);
    valor = a*adc0+b;
    Serial.println(valor,3);
    Serial.flush();
    }
}
