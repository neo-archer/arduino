int PhotosensorPin = A0; Указываем пин к которому подклюен Фоторезистор

unsigned int sensorValue = 0; Объявляем переменную для хранения значений.

void setup() {

pinMode(13, OUTPUT);

Serial.begin(9600);

}

void loop() {

sensorValue = analogRead(PhotosensorPin); Считываем значения с фоторезистора

if(sensorValue50) digitalWrite(13, HIGH); Включаем

else digitalWrite(13, LOW);  Выключаем

Serial.print(sensorValue, DEC); Вывод данных с фоторезистора (0-1024)

Serial.println();

delay(500);

}