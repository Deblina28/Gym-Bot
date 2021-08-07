#define af 0.1

float raw = 0;
boolean edge = true;

void setup() 
{
  pinMode(A0, INPUT_PULLUP);
  pinMode(3, OUTPUT);
  Serial.begin(2000000);

}
int ct = 0;

void loop()
{

  raw = af * raw + (1 - af) * analogRead(A0);

  
  //delay(10);

  if (raw < 800)
  {
    if (edge)
    {
      ct++;
      edge = false;
    }
  }

  else if (raw >= 810)
    edge = true;

Serial.print(raw);
Serial.print("  ");
Serial.println(ct);

}
