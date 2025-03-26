
/*
 *
 *March 25, 2025
 * by: Sophie Nguyen
 * 
 * using sonar with arduino
 * 
 */

//pin numbers
const int TRIG_PIN = 3;  
const int ECHO_PIN = 2; 
const int LED = 11;
const int SPEED_OF_LIGHT = 0.0343;


//variables
float duration, distance;  

//setup
void setup() {  
   pinMode(TRIG_PIN, OUTPUT);  
   pinMode(ECHO_PIN, INPUT); 
   pinMode(LED, OUTPUT); 
   Serial.begin(9600);  
}  

//loop
void loop() {  
  //clears the trig pin
   digitalWrite(TRIG_PIN, LOW);  
   delayMicroseconds(2);  

   //sets trig pin on high fpr 10 micro seconds
   digitalWrite(TRIG_PIN, HIGH);  
   delayMicroseconds(10);  
   digitalWrite(TRIG_PIN, LOW);  

   //reads the echo pin, returns the sound wave travel time in microseconds
   duration = pulseIn(ECHO_PIN, HIGH);  

   distance = (duration*SPEED_OF_LIGHT)/2;

   if (distance < 10) {
    digitalWrite(LED, HIGH);
   }

   else {
     digitalWrite(LED,LOW);
   }

    Serial.print(distance);

    Serial.println(" cm");

    delay(100);
}