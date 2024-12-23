#include <Servo.h> 
const int Button_B = 3; // 버튼 B가 레이저의 ON/OFF 상태 설정 역할 
int laser = 0; // 레이저 초기 상태 
Servo xServo, yServo; 

void setup() { 
   xServo.attach(9); // X축 좌우 서보 모터 
   yServo.attach(10); // Y축 상하 서보 모터 
   pinMode(11, OUTPUT); // 레이저 
   pinMode(Button_B, INPUT_PULLUP); 
   Serial.begin(9600); 
   } 

void loop() { 
   int x_pos = analogRead(A0); // 조이스틱 X축 0~507~1023 
   int y_pos = analogRead(A1); // 조이스틱 Y축 0~505~1023 
   int b_state = digitalRead(Button_B); // 조이스틱 B 버튼 눌렀을 때 LOW

   if(b_state == LOW){ 
      laser = 1; 
      }
   else{ 
      laser = 0; 
      } 

   int x = map(x_pos, 0, 1023, 120, 0); // 좌우 
   int y = map(y_pos, 0, 1023, 0, 120); // 상하 
   xServo.write(x); 
   delay(1); 
   yServo.write(y); 
   delay(1); 
   digitalWrite(11, laser); 
   }
