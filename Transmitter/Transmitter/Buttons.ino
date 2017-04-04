//This file contain code to handle the button interrupts

int const Button_1 = 2;
int const Button_2 = 3;
int const Button_3 = 5;
int const Button_4 = 4;

int Button = 0;

void InitButtons()
{
  //PB0 - Button 1
  //PB1 - Button 2
  //PB2 - Button 3
  //PB3 - Button 4

  //Set to inputs
  pinMode(Button_1, INPUT);
  pinMode(Button_2, INPUT);
  pinMode(Button_3, INPUT);
  pinMode(Button_4, INPUT);

  //Activate interrupts

  GIMSK |= _BV(PCIE0);   // Enable Pin Change Interrupts
  PCMSK0 |= _BV(PCINT8); // Use PB0 as interrupt pin
  PCMSK0 |= _BV(PCINT9); // Use PB1 as interrupt pin
  PCMSK0 |= _BV(PCINT10); // Use PB2 as interrupt pin
  PCMSK0 |= _BV(PCINT11); // Use PB3 as interrupt pin
 
  sei(); //Enable interrupts

  return;
}

ISR(PCINT0_vect) 
{
  if(digitalRead(Button_1))
  {
    BluetoothMessage[0] = 'F';
    BluetoothMessage[1] = 'U';
    BluetoothMessage[2] = '-';
    BluetoothMessage[3] = '1';
  }
  else if(digitalRead(Button_2))
  {
    BluetoothMessage[0] = 'F';
    BluetoothMessage[1] = 'U';
    BluetoothMessage[2] = '-';
    BluetoothMessage[3] = '2';
  }
  else if(digitalRead(Button_3))
  {
    BluetoothMessage[0] = 'F';
    BluetoothMessage[1] = 'U';
    BluetoothMessage[2] = '-';
    BluetoothMessage[3] = '3'; 
  }
  else if(digitalRead(Button_4))
  {
    BluetoothMessage[0] = 'F';
    BluetoothMessage[1] = 'U';
    BluetoothMessage[2] = '-';
    BluetoothMessage[3] = '4'; 
  }  
}

