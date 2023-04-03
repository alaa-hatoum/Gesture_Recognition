void setup() {
  Serial.begin(9600);
}

char data;

void loop() {
  if (Serial.available() > 0) {
    data = Serial.read();
    Serial.print("Received: ");
    Serial.println(data, BIN);


    if (data & 16) {
      Serial.println("raise thumb");
    }
    if (data & 8) {
      Serial.println("raise index");
    }
    if (data & 4) {
      Serial.println("raise middl");
    }
    if (data & 2) {
      Serial.println("raise ring_");
    }
    if (data & 1) {
      Serial.println("raise pinky");
    }
  }
}
