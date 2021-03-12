void setup() {
  Serial.begin(9600);
}

void loop() {
  int voltage = analogRead(A0);
  //float voltage = analogRead(A0)*5.0/1024;
  //float voltage =( -1*(analogRead(A0)*5.0/1024))+3.1;
  //Serial.print("Voltage: ");
  Serial.println(voltage);
  delay(100);
}
