import time
import pandas as pd
from datetime import datetime
import RPi.GPIO as GPIO

# GPIO pin
PIN = 17

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)

# Function to read PIR motion sensor data
def read_motion():
    return GPIO.input(PIN)

# Function to collect data for a specified duration and interval
def collect_data(duration_minutes, interval_seconds):
    data = []
    start_time = time.time()
    duration_seconds = duration_minutes * 60

    while time.time() - start_time < duration_seconds:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        motion = read_motion()
        data.append([timestamp, motion])
        print(f"Timestamp: {timestamp}, Motion Detected: {motion}")
        time.sleep(interval_seconds)

    return data

# Function to export data to Excel
def export_to_excel(data, filename):
    df = pd.DataFrame(data, columns=['Timestamp', 'Motion'])
    df.to_excel(filename, index=False)
    print(f"Data saved to {filename}")

# Example usage
if __name__ == "__main__":
    duration_minutes = 5  # Set the duration in minutes
    interval_seconds = 10  # Set the interval in seconds
    data = collect_data(duration_minutes, interval_seconds)
    export_to_excel(data, 'motion_data.xlsx')