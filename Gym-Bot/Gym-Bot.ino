void setup() {
  pinMode(A0,INPUT_PULLUP);
  pinMode(3,OUTPUT);
  Serial.begin(115200);
  
}

void loop() {
  analogWrite(3, 200);
  Serial.println(analogRead(A0));
 
}
