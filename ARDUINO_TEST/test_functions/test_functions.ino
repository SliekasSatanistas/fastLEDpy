#include "FastLED.h"

void setup() { 
  Serial.begin(9600);
}

int8_t ttqadd7( int8_t i, int8_t j)
{
    int16_t t = i + j;
    if( t > 127) t = 127;
return t;
}

void loop() { 
  int8_t i; int8_t j;
  i = 200; j=-350;
  int16_t t = i + j;
  int8_t x = t;
  Serial.println(i); Serial.println(j);
  Serial.println(t);
  Serial.println(i+j);
  Serial.println(x);
  Serial.println(qadd7( 200,-350  ));
  Serial.println(ttqadd7( 200,-350  ));
  delay(500);
  Serial.println("---------------------------------------------");
}
