# Data Analysis: Air Quality Index of a remote location

## Overview
The **Embedded Air Quality Measurement System** is a Python-based project utilizing the **JoyPI Box** to measure, analyze, and visualize environmental parameters such as particulate matter (PM1.0, PM2.5, and PM10), temperature, and humidity. The system integrates real-time data collection from sensors, cloud-based data management via **ThingSpeak**, and an interactive user interface for seamless data visualization.

## Features
- **Real-time Sensor Data Collection**: Uses **DHT11** for temperature & humidity and **PM sensors** for air quality.
- **ThingSpeak Integration**: Fetches and updates sensor data via cloud storage.
- **Air Quality Index (AQI) Calculation**: Computes AQI levels based on PM values.
- **Interactive User Interface**: Displays real-time data and allows selection of different parameters using a button-controlled UI.
- **Data Visualization**: Uses **Matplotlib** for graphical representation of trends.
- **FIFO Buffer for Data Processing**: Maintains recent data values for accurate calculations.

## System Components
### Hardware
- **JoyPI Box**
- **Raspberry Pi**
- **DHT11 Sensor** (Temperature & Humidity)
- **PM Sensors** (PM1.0, PM2.5, PM10.0)
- **7-Segment Display & LED Matrix**
- **Push Buttons** (For navigation in UI)

### Software
- **Python 3**
- **ThingSpeak API**
- **Matplotlib** (for visualization)
- **RPi.GPIO** (for button input handling)

## Installation & Setup
### 1. Install Dependencies
```bash
pip install requests matplotlib RPi.GPIO Adafruit-LED-Backpack dht11
```

### 3. Configure ThingSpeak API
- Sign up at [ThingSpeak](https://thingspeak.com/).
- Create a new channel and obtain the **Channel ID** & **API keys**.
- Update `get_data.py` with your API credentials.

### 4. Run the Application
```bash
python main.py
```

## System Workflow
### 1. Data Collection
- Sensors collect **temperature, humidity, and PM levels** every 10 seconds.
- Data is stored in a **FIFO buffer** for efficient processing.

### 2. AQI Calculation
- The system computes AQI based on **PM2.5 and PM10 values** using standard AQI formulas.
- The highest AQI value is selected for reporting.

### 3. Cloud & Local Storage
- Sensor data is **pushed to ThingSpeak** every minute.
- The system fetches the latest values for visualization.

### 4. User Interface
- Users can **navigate through different data parameters** using buttons.
- Data is displayed on **7-segment displays and LED matrix**.
- **Matplotlib graphs** show real-time trends.

## Visualization
- **PM1.0, PM2.5, and PM10.0 graphs** with mean values.
- **Temperature & humidity plots**.
- **LED matrix and seven-segment display** for real-time monitoring.

## Future Enhancements
- Implement **MQTT protocol** for better cloud integration.
- Add support for additional **air pollutants (CO, NO2, etc.)**.
- Improve **UI interactivity** using a touchscreen display.

## License
This project is open-source under the **MIT License**.
