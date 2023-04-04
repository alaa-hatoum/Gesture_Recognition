#include <Servo.h>

Servo mythumb;
Servo myindex;
Servo mymiddle;
Servo myring;
Servo mypinky;

void setup() {
  Serial.begin(9600);
  mythumb.attach(8);
  mythumb.write(30);

  myindex.attach(9);
  myindex.write(90); // make sure the motor is stopped 

  mymiddle.attach(10);
  mymiddle.write(0);

  myring.attach(11);
  myring.write(0);

  mypinky.attach(12);
  mypinky.write(90);
}

char data;
char index_closed = 0;
char pinky_closed = 0;

char index_turning = 0; // 0 if not doing anything, 1 if closed -> raised, 2 if raised -> closed
char pinky_turning = 0; // 0 if not doing anything, 1 if closed -> raised, 2 if raised -> closed

unsigned long index_rot_start = 0;
unsigned long pinky_rot_start = 0;

void loop() {
  if (index_turning == 1 && millis() - index_rot_start >= 400) {
    myindex.write(90);
    index_turning = 0;
  } else if (index_turning == 2 && millis() - index_rot_start >= 420) { // raised -> closed
    myindex.write(90);
    index_turning = 0;
  }

  if (pinky_turning == 1 && millis() - pinky_rot_start >= 300) { // closed -> raised
    mypinky.write(90);
    pinky_turning = 0;
  } else if (pinky_turning == 2 && millis() - pinky_rot_start >= 310) { // raised -> closed
    mypinky.write(90);
    pinky_turning = 0;
  }

  
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
      if (pinky_closed == 1) {
        pinky_rot_start = millis();
        pinky_turning = 1;
        mypinky.write(135); // Turning cw
        //delay(300);
        //mypinky.write(90);
        pinky_closed = 0;
      } else {
        mypinky.write(90);
      }
    } else {
      if (pinky_closed == 0) {
        pinky_rot_start = millis();
        pinky_turning = 2;
        mypinky.write(45); // Turning ccw
        //delay(300);
        //mypinky.write(90);
        pinky_closed = 1;
      } else {
        mypinky.write(90);
      }
    }


    if (data & 8) {
      Serial.println("raise index");
      if (index_closed == 1) {
        index_rot_start = millis();
        index_turning = 1; 
        myindex.write(135); // Turning ccw
        //delay(400);
        //myindex.write(90);
        index_closed = 0;
      } else {
        myindex.write(90);
      }
    } else {
      if (index_closed == 0) {
        index_rot_start = millis();
        index_turning = 2;
        myindex.write(45); // Turning cw
        //delay(350);
        //myindex.write(90);
        index_closed = 1;
      } else {
        myindex.write(90);
      }
    }
  }

}
