const int analogPin = A0;
int sensorValue = 0;

void setup() {
  Serial.begin(9600);
  // No need for pinMode for analog input, but note external pull-down resistor is required
}

void loop() {
  // Read the value from A0
  sensorValue = analogRead(analogPin);
  
  // Convert it to a voltage (assuming 5V reference)
  float voltage = sensorValue * (5.0 / 1023.0);
  
  // Print the raw sensor value and voltage to the serial monitor
  Serial.print("Analog Value: ");
  Serial.print(sensorValue);
  Serial.print(" | Voltage: ");
  Serial.println(voltage);
  
  delay(100);  // Short delay before reading again
}
