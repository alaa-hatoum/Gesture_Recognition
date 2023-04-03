#include <Servo.h>

Servo mythumb;
Servo mymiddle;
Servo myring; 


void setup() {
  Serial.begin(9600);
  mythumb.attach(8);
  mymiddle.attach(10);
  myring.attach(11);  
}

char data;

void loop() {
  if (Serial.available() > 0) {
    data = Serial.read();
    Serial.print("Received: ");
    Serial.println(data, BIN);
    
      if (data & 16) {
        Serial.println("raise thumb");
        mythumb.write(30);
      } else {
        mythumb.write(140);
      }
      
      
      if (data & 8) {
        Serial.println("raise index");
      }

      
      if (data & 4) {
        Serial.println("raise middle");
        mymiddle.write(0);
      } else {
        mymiddle.write(180);
      }

      
      if (data & 2) {
        Serial.println("raise ring");
        myring.write(0);
      } else {
        myring.write(180);
      }

      
      if (data & 1) {
        Serial.println("raise pinky");
      }
    }
  
}
