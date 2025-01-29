# This program is done by Shrey Rahulkumar Vyas [30460285]

#---- Import Libraries ----
import RPi.GPIO as RPI  #<--- Library for GPIO Usage
import dht11  #<--- Library for accessing sensor data (Temperature and Humidity)
from Adafruit_LED_Backpack import SevenSegment
import thingspeak
import time

#---- Thingspeak Setup ----
channel_id = 2588965
write_key = 'H36HY2IX8WX5SIFG'
read_key = 'BN8ZA1LAM04WC8P0'
my_channel = thingspeak.Channel(id=channel_id, api_key=write_key)

#---- Hardware setup ----
RPI.setmode(RPI.BCM)  #<--- Setting the numbering system for GPIOs
my_dht11 = dht11.DHT11(pin=4)  #<--- Creating an instance for DHT11 usage
my_7SD = SevenSegment.SevenSegment(address=0x70)  #<--- Creating SevenSegment object
my_7SD.begin()  #<--- Initialise Seven Segment Display

#---- Initialize FIFO Buffer for last 100 values ----
BUFFER_SIZE = 100  #<--- Maximum size of the buffer
temperature_buffer = []
humidity_buffer = []
time_buffer = []
start_time = time.time()

#---- Function to manage FIFO buffer ----
def update_fifo_buffer(buffer, new_value):
    if len(buffer) > BUFFER_SIZE:
        buffer.pop(0)  #<--- Remove the oldest value (FIFO behavior)
    buffer.append(new_value)  #<--- Add the new value

#---- Forever Loop ----
while True:
    # Get a single sensor measurement
    temp_humidity_read = my_dht11.read()

    while not temp_humidity_read.is_valid():
        temp_humidity_read = my_dht11.read()

    # Record time
    current_time = time.time() - start_time
    temperature = temp_humidity_read.temperature
    humidity = temp_humidity_read.humidity

    # Print values
    print("Temperature:", temperature)
    print("Humidity:", humidity)

    # Show temperature on 7SD
    my_7SD.print_number_str(str(temperature))
    my_7SD.write_display()

    # Update FIFO buffer
    update_fifo_buffer(temperature_buffer, temperature)
    update_fifo_buffer(humidity_buffer, humidity)
    update_fifo_buffer(time_buffer, current_time)

    # Transfer data to ThingSpeak
    my_channel.update({'field4': temperature, 'field5': humidity})

    time.sleep(10)  #<--- Wait for 10 seconds before the next measurement
