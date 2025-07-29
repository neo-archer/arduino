#include <iarduino_RTC.h>
iarduino_RTC time(RTC_DS1302, 2,4,3); //rst,clk,dat
void setup() {
  pinMode (5, OUTPUT);
  Serial.begin(9600);
  time.begin();
  //time.settime(0,29,21,29,06,19,6); //секунды, минуты, часы, день, месяц, год, день недели
}

void loop() {
 if(millis()%1000==0){
  Serial.println(time.gettime("d-m-Y, H:i:s, D"));
  
  if(time.Hours==8 && time.minutes==00 && time.seconds==0)
  {digitalWrite (5, HIGH);
   //delay(10000);
   //digitalWrite (5, LOW);
  }

 /*if(time.Hours==18 && time.minutes==00 && time.seconds==0)
  {digitalWrite (5, HIGH);
   delay(10000);
   digitalWrite (5, LOW);
   
  }*/
  
  delay(2);
 }

}
