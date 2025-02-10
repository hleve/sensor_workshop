# Environmental Data Collection Device

The goal of this project is on making the entire process as user-friendly and accessible as possible.

## Navigation
For first time setup: [Directions for First Time Setup](#directions-for-first-time-setup)  
For information on Modules: [Sensors and Modules](#sensors-and-modules)  
For 3D printable enclosures: [3D Files](#) as well as in a collection on [Printables.com](https://www.printables.com/@HenryLevesque/collections/1649941)

## Sensors

### Temperature Sensor
**Model**: DHT11

**Setup**:
1. Connect the VCC pin of the DHT11 sensor to the 3.3V pin on the Raspberry Pi.  
2. Connect the GND pin of the DHT11 sensor to a GND pin on the Raspberry Pi.  
3. Connect the DATA pin of the DHT11 sensor to GPIO pin 4 on the Raspberry Pi.

**Python Script**:  
- `temperature_sensor.py`: Reads temperature data from the DHT11 sensor.

**Usage**:
1. Ensure the `requirements.txt` are installed:
    ```sh
    pip install -r requirements.txt
    ```
2. Run:
    ```sh
    python3 temperature_sensor.py
    ```
**Output**:
- Saves data to `temperature_data.xlsx` with timestamps.

### PIR Motion Sensor
**Model**: HC-SR501

**Setup**:
1. Connect the VCC pin of the PIR sensor to the 5V pin on the Raspberry Pi.  
2. Connect the GND pin of the PIR sensor to a GND pin on the Raspberry Pi.  
3. Connect the OUT pin of the PIR sensor to GPIO pin 17 on the Raspberry Pi.

**Python Script**:  
- `pir_motion_sensor.py`: Reads motion data from the PIR sensor.

**Usage**:
1. Ensure the `requirements.txt` are installed:
    ```sh
    pip install -r requirements.txt
    ```
2. Run:
    ```sh
    python3 pir_motion_sensor.py
    ```
**Output**:
- Saves data to `motion_data.xlsx` with timestamps.