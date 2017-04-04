//This file will contain code to initialize and analyze the ADC values

int const MidBot_X = 13;
int const MidBot_Y = 12;
int const LeftCenter_X = 11;
int const LeftCenter_Y = 10;

int Movement_X;
int Movement_Y;
int Bottom_X;
int Bottom_Y;

void InitADC()
{
  //PA0 - X Mid Bot
  //PA1 - Y Mid Bot

  //PA2 - X Left Center
  //PA3 - Y Left Center

  pinMode(MidBot_X, INPUT);
  pinMode(MidBot_Y, INPUT);
  pinMode(LeftCenter_X, INPUT);
  pinMode(LeftCenter_Y, INPUT);

  Movement_X = analogRead(MidBot_X);
  Movement_Y = analogRead(MidBot_Y);
  Bottom_X = analogRead(LeftCenter_X);
  Bottom_Y = analogRead(LeftCenter_Y);

  return;
}

void ReadADCs()
{
  Movement_X = analogRead(MidBot_X);
  Movement_Y = analogRead(MidBot_Y);
  Bottom_X = analogRead(LeftCenter_X);
  Bottom_Y = analogRead(LeftCenter_Y);
  return;
}

void RotationJS(int X, int Y)
{
  if(X > 500)
  {
    //CW
    BluetoothMessage[0] = 'C';
    BluetoothMessage[0] = 'W';
    BluetoothMessage[0] = '-';
    BluetoothMessage[3] = X/100;
  }
  else if(X < 400)
  {
    //CCW
    BluetoothMessage[0] = 'C';
    BluetoothMessage[0] = 'C';
    BluetoothMessage[0] = '-';
    BluetoothMessage[3] = X/100;
  }
  return;
}

void MovementJS(int X, int Y)
{
  int ShortX = X/100;
  int ShortY = Y/100;

  
  return;
}

