import time
import pandas as pd
from datetime import datetime
import Adafruit_DHT

# Sensor type and GPIO pin
SENSOR = Adafruit_DHT.DHT11
PIN = 4

# Function to read temperature data
def read_temperature():
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
    return temperature

# Function to collect data for a specified duration and interval
def collect_data(duration_minutes, interval_seconds):
    data = []
    start_time = time.time()
    duration_seconds = duration_minutes * 60

    while time.time() - start_time < duration_seconds:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        temperature = read_temperature()
        data.append([timestamp, temperature])
        print(f"Timestamp: {timestamp}, Temperature: {temperature}°C")
        time.sleep(interval_seconds)

    return data

# Function to export data to Excel
def export_to_excel(data, filename):
    df = pd.DataFrame(data, columns=['Timestamp', 'Temperature'])
    df.to_excel(filename, index=False)
    print(f"Data saved to {filename}")

# Example usage
if __name__ == "__main__":
    duration_minutes = 5  # Set the duration in minutes
    interval_seconds = 10  # Set the interval in seconds
    data = collect_data(duration_minutes, interval_seconds)
    export_to_excel(data, 'temperature_data.xlsx')