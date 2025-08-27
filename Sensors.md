# All Sensors
    Capacitive Touch
    PIR Motion
    Linear Temperature
    Collision Sensor
    Soil Moisture
    Photocell
    Water Level
    Analog Rotation
    Analog Temperature
    Flame Alarm
    Knock Sensor
    IR Obstacle Avoidance
    Analog Ceramic Vibration
    Ultrasound
    Rotary Encoder
    Temperature and Humidity Display
    Steam Moisture
    Analog Sound
    Joystick
    4-digit LED Digital Tube
    White LED
    Passive Buzzer
    Active Buzzer
    Digital IR Receiver
    Digital IR Transmitter
    Button
    Reed Switch
    Line Tracking
    Traffic Light
    Hall Sensor
    Motor Module
    Pulse Rate Monitor
    Single Relay
    Analog Sound
    Digital Tilt 
    Voltage Detection
    RGB LED


## Sample scripts

### Temperature Sensor
**Model**: DHT11

**Setup**:
1. Connect the VCC pin of the DHT11 sensor to the 3.3V pin on the Raspberry Pi.  
2. Connect the GND pin of the DHT11 sensor to a GND pin on the Raspberry Pi.  
3. Connect the DATA pin of the DHT11 sensor to GPIO pin 4 on the Raspberry Pi.

**Python Script**:  
- [`temperature_sensor.py`](python%20files/temperature_sensor.py): Reads temperature data from the DHT11 sensor.

**Usage**:
1. Ensure the Python requirements are installed (see `INSTALL.md`):
    ```sh
    pip3 install -r requirements-pip.txt
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
- [`pir_motion_sensor.py`](python%20files/pir_motion_sensor.py): Reads motion data from the PIR sensor.

**Usage**:
1. Ensure the Python requirements are installed (see `INSTALL.md`):
    ```sh
    pip3 install -r requirements-pip.txt
    ```
2. Run:
    ```sh
    python3 pir_motion_sensor.py
    ```
**Output**:
- Saves data to `motion_data.xlsx` with timestamps.

### Camera Capture
**Python Script**:  
- [`capture_images.py`](python%20files/capture_images.py): Uses `libcamera-still` to capture images on the Pi Camera.

**Usage**:
1. Ensure `libcamera-apps` is installed (see `INSTALL.md`).
2. Run:
    ```sh
    python3 "python files/capture_images.py"
    ```

**Output**:
- Images saved to the `captured_images/` folder by default.
