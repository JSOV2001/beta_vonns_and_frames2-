#include <Servo.h>

Servo base_servomotor;

void setup() {
  Serial.begin(9600);
  delay(1000);
  
  base_servomotor.attach(11);
  base_servomotor.write(5);
  delay(500);
  
  for(int i = 0; i < 45; i++){
    base_servomotor.write(i);
    Serial.print(i);
    delay(2000);
  }
} 


void loop() {
 }
