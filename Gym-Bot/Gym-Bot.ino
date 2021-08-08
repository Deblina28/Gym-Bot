#include <Arduino.h>
#include <U8x8lib.h>

#define af 0.1

float raw = 0;
boolean edge = true;
U8X8_SSD1306_128X64_NONAME_SW_I2C u8x8( SCL,  SDA,  U8X8_PIN_NONE);

void setup() {
  pinMode(A0, INPUT_PULLUP);
  pinMode(3, OUTPUT);
  Serial.begin(115200);
  u8x8.begin();

  u8x8.setFont(u8x8_font_px437wyse700b_2x2_r);
  u8x8.drawString(0, 2, "Welcome");
  delay(1000);
  u8x8.drawString(0, 2, "Push Ups");
  delay(1000);

  u8x8.drawString(0, 2, " Counts ");

}
int ct = 0;
char buf[7];
void loop()
{

  raw = af * raw + (1 - af) * analogRead(A0);




  if (raw < 810)
  {
    if (edge)
    {
      ct++;
      edge = false;
      u8x8.drawString(2, 5, itoa(ct-1,buf,10));
    }
  }

  else if (raw >= 815)
    edge = true;

Serial.println(ct-1);
delay(10);
}
