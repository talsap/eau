/*****************************************************************************************************************
 * ADS1115_LM35_01 - Medicao de deformações com o Transdutor Linear e conversor analogico digital ADS1115 (16 bit)
 * ------------------------------------------------------------------------------
 * based on: Haroldo Amaral - agaelema@gmail.com - https://github.com/agaelema/ADS1115_and_LM35
 * modified by: Tarcisio Sapucaia - tarcisiosapucaia27@gmail.com
 * 2019/07/02 - v 1.0
 ****************************************************************************************************************/

/* Import das Bibliotecas */
#include <Wire.h>
#include <Adafruit_ADS1015.h>

/* Variaveis*/
int16_t adc0 = 0;
char conexao = 0, cond = 0;

/* cria instância do conversor analogico digital ADC */
Adafruit_ADS1115 ads(0x48);  /* Use this for the 16-bit version */
//Adafruit_ADS1015 ads;     /* Use thi for the 12-bit version */


void setup(void) {
  /* inicializa a serial */
  Serial.begin(9600);
 
  // The ADC input range (or gain) can be changed via the following
  // functions, but be careful never to exceed VDD +0.3V max, or to
  // exceed the upper and lower limits if you adjust the input range!
  // Setting these values incorrectly may destroy your ADC!
  //                                                           ADS1015       ADS1115
  //                                                           -------       -------
  ads.setGain(GAIN_TWOTHIRDS);   // 2/3x gain +/- 6.144V  1 bit = 3mV      0.1875mV (default)
  // ads.setGain(GAIN_ONE);        // 1x gain   +/- 4.096V  1 bit = 2mV      0.125mV
  // ads.setGain(GAIN_TWO);        // 2x gain   +/- 2.048V  1 bit = 1mV      0.0625mV
  // ads.setGain(GAIN_FOUR);       // 4x gain   +/- 1.024V  1 bit = 0.5mV    0.03125mV
  // ads.setGain(GAIN_EIGHT);      // 8x gain   +/- 0.512V  1 bit = 0.25mV   0.015625mV
  // ads.setGain(GAIN_SIXTEEN);    // 16x gain  +/- 0.256V  1 bit = 0.125mV  0.0078125mV

  /* inicializa o ADC */
  ads.begin();

}

void loop(void) {

  conexao = Serial.read();
  adc0 = ads.readADC_SingleEnded(0);
  if (conexao == 73){
      cond = 73;
      }
  
      
  if  (conexao == 67){            //caso receba C = 67 em decimal (verifica se há conexao com a porta serial)
    Serial.println("conectado");
    Serial.flush();
    cond = 0;
    }
  
  if (conexao == 68){               //caso receba D = 68 em decimal (para caso de desconexao com a porta serial)
    Serial.println("desconectar");
    Serial.flush();
    Serial.end();
    Serial.begin(9600);
    cond = 0;
    }

  if (cond == 73){         //caso receba I = 73 em decimal (para caso de coletar dados com a porta serial)
    adc0 = ads.readADC_SingleEnded(0);
    Serial.println(adc0);
    Serial.flush();
    delay(1000);
    cond = 73;
    
    }
}
