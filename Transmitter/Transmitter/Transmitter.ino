
/*
Pin - Ports
1 - VCC
2 - PB0
3 - PB1
4 - PB3
5 - PB2
6 - PA7
7 - PA6
8 - PA5
9 - PA4
10 - PA3
11 - PA2
12 - PA1
13 - PA0
14 - GND
*/

/*
  Message Format:
  Form: .__-#
  .CW-#
  .CC-#
  .FO-#
  .RE-#
  .FL-#
  .FR-#
  .RL-#
  .RR-#
  .FU-#
*/
char BluetoothMessage[4];

void setup()
{
  //initialize pins and interrupts
  InitButtons();
  InitADC();
  InitLEDs();
  InitBluetooth();
  
}

void loop()
{
  // put your main code here, to run repeatedly:

}
