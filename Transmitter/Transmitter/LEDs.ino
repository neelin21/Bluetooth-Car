//Contains code to initialize and activate the LEDs

int const Connected = 6;
int const Status = 9;

void InitLEDs()
{
  //PA7 - Connected
  //PA4 - Status
  pinMode(Connected, OUTPUT);
  pinMode(Status, OUTPUT);
  return;
}

void TurnOnLED(int led)
{
  digitalWrite(led, HIGH);
  return;
}

void TurnOffLED(int led)
{
  digitalWrite(led, LOW);
  return;
}
