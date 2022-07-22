#include<stdio.h>
#include<wiringPi.h>
#define GAS_PIN 25
int main(void)
{
wiringPiSetupGpio();
pinMode(GAS_PIN,INPUT);

while(1==1)
{
if(digitalRead(GAS_PIN)==LOW)
{
printf("Gas Present! Gas Present! Gas Present! \n");
}

else
{
printf("NO GAS \n");
}
delay(2000);
}
return 0;
}


