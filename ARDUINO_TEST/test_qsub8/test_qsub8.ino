#include "FastLED.h"

void setup() { 
  Serial.begin(9600);
}


void loop() { 
  long a, b, c;
  
  a=-10; b=-23;
  Serial.print("a="); Serial.print(a); Serial.print(" b= "); Serial.print(b); 
  Serial.print(" qadd8=");Serial.println(qadd8(a,b));
  a=-1; b=-2;
  Serial.print("a="); Serial.print(a); Serial.print(" b= "); Serial.print(b); 
  Serial.print(" qadd8=");Serial.println(qadd8(a,b));
  a=-1; b=0;
  Serial.print("a="); Serial.print(a); Serial.print(" b= "); Serial.print(b); 
  Serial.print(" qadd8=");Serial.println(qadd8(a,b));
  a=0; b=0;
  Serial.print("a="); Serial.print(a); Serial.print(" b= "); Serial.print(b); 
  Serial.print(" qadd8=");Serial.println(qadd8(a,b));
  a=3; b=4;
  Serial.print("a="); Serial.print(a); Serial.print(" b= "); Serial.print(b); 
  Serial.print(" qadd8=");Serial.println(qadd8(a,b));
  a=3; b=-4;
  Serial.print("a="); Serial.print(a); Serial.print(" b= "); Serial.print(b); 
  Serial.print(" qadd8=");Serial.println(qadd8(a,b));
  a=254; b=1;
  Serial.print("a="); Serial.print(a); Serial.print(" b= "); Serial.print(b); 
  Serial.print(" qadd8=");Serial.println(qadd8(a,b)); 
  a=255; b=0;
  Serial.print("a="); Serial.print(a); Serial.print(" b= "); Serial.print(b); 
  Serial.print(" qadd8=");Serial.println(qadd8(a,b)); 
  a=255; b=1;
  Serial.print("a="); Serial.print(a); Serial.print(" b= "); Serial.print(b); 
  Serial.print(" qadd8=");Serial.println(qadd8(a,b)); 
  a=200; b=60;
  Serial.print("a="); Serial.print(a); Serial.print(" b= "); Serial.print(b); 
  Serial.print(" qadd8=");Serial.println(qadd8(a,b));
  a=260; b=-50;
  Serial.print("a="); Serial.print(a); Serial.print(" b= "); Serial.print(b); 
  Serial.print(" qadd8=");Serial.println(qadd8(a,b));
  a=-260; b=50;
  Serial.print("a="); Serial.print(a); Serial.print(" b= "); Serial.print(b); 
  Serial.print(" qadd8=");Serial.println(qadd8(a,b));
  a=260; b=300;
  Serial.print("a="); Serial.print(a); Serial.print(" b= "); Serial.print(b); 
  Serial.print(" qadd8=");Serial.println(qadd8(a,b));
  Serial.println("---------------------------------------------");
}
