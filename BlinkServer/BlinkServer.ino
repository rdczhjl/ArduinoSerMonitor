/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.

  Most Arduinos have an on-board LED you can control. On the Uno and
  Leonardo, it is attached to digital pin 13. If you're unsure what
  pin the on-board LED is connected to on your Arduino model, check
  the documentation at http://arduino.cc

  This example code is in the public domain.

  modified 8 May 2014
  by Scott Fitzgerald
 */


// the setup function runs once when you press reset or power the board
byte   cmd[20];
byte   value[20];
int    onInterval=1;
int    offInterval=5;

void setup() {
  // initialize digital pin 13 as an output.
  Serial.println("Now start ...");
  Serial.begin(9600);
  Serial.setTimeout(0);
  
  pinMode(13, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  int num1;
  int num2;
  
  Serial.print("please input (current onInterval/offInterval value)...");
  Serial.print(onInterval,DEC); Serial.print("/"); Serial.println(offInterval,DEC);

  num1=Serial.readBytes(cmd,4);  
  num2=Serial.readBytes(value,1);
  
  if ( num1 ==4 && num2 == 1){
    
      cmd[4]=0;
      value[1]=0;
  
      Serial.print("got cmd ");
      Serial.println((char*)cmd);
      Serial.print(" and value ");
      Serial.println(value[0]-'0',DEC);
  
      if (strcmp("seOn",(char*)cmd)==0){
          onInterval=value[0]-'0';
          Serial.println("On Interval is set");
      }
  
      if (strcmp("seOf",(char*)cmd)==0){
          offInterval=value[0]-'0';
          Serial.println("Off Interval is set");  
       }
  
  }//num1 or num2 not meet criteria
  
  
  digitalWrite(13, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(onInterval*1000);              // wait for a second
  digitalWrite(13, LOW);    // turn the LED off by making the voltage LOW
  delay(offInterval*1000);              // wait for a second
  
  
}
