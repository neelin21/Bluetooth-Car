//This file contain code to handle the button interrupts

int const Button_1 = 2;
int const Button_2 = 3;
int const Button_3 = 5;
int const Button_4 = 4;

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
  
  return;
}

void ButtonRead(int button)
{
  switch(button)
  {
    case Button_1:
      //Run function

    break;

    case Button_2:
      //Run function

    break;

    case Button_3:
      //Run function

    break;

    case Button_4:
      //Run function

    break;

    default:
      //Default

    break;
  }
  return;
}
