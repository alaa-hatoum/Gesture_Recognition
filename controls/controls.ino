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
        mypinky.write(45); // Turning cw
        delay(300);
        mypinky.write(90);
        pinky_closed = 0;
      } else {
        mypinky.write(90);
      }
    } else {
      if (pinky_closed == 0) {
        mypinky.write(135); // Turning ccw
        delay(300);
        mypinky.write(90);
        pinky_closed = 1;
      } else {
        mypinky.write(90);
      }
    }

    if (data & 8) {
      Serial.println("raise index");
      if (index_closed == 1) {
        myindex.write(135); // Turning ccw
        delay(400);
        myindex.write(90);
        index_closed = 0;
      } else {
        myindex.write(90);
      }
    } else {
      if (index_closed == 0) {
        myindex.write(45); // Turning cw
        delay(350);
        myindex.write(90);
        index_closed = 1;
      } else {
        myindex.write(90);
      }
    }
  }

}
