# This program is jointly done by Shrey Vyas, Vandan Deria, and Dhyanam Pandya
# Shrey Rahulkumar Vyas [30460285]

#---- Importing all necessary pakages ----
import requests
import matplotlib.pyplot as plt
import numpy as np
import time
import json
import random
import thingspeak

#---- Conversion of string message to a JSON message object ----
cloud_data = requests.get('https://thingspeak.com/channels/343018/feed.json')
cloud_data = str(cloud_data.text)
cloud_data_json = json.loads(cloud_data)

#---- Getting the feeds from the selected channel ----
feeds = cloud_data_json['feeds']

#---- Creating field arrays to store the accessed value ----
field_1 = []
field_2 = []
field_3 = []
field_4 = []
field_5 = []
field_6 = []
field_7 = []

#---- Extracting data for the first 100 entries ----
for i in range(100):
    field_1.append(feeds[i]['field1'])
    field_3.append(feeds[i]['field3'])
    field_5.append(feeds[i]['field5'])

#---- Randomize Local Temperature (15-16°C) and Local Humidity (25-27%) ----
field_6 = [round(random.uniform(15, 16), 2) for _ in range(100)]
field_7 = [round(random.uniform(25, 27), 2) for _ in range(100)]

# Printing all the accessed values ----
print("The values in field1 (PM10.0) are: \n",field_1)
print("The values in field3 (PM2.5) are: \n",field_3)
print("The values in field5 (PM1.0) are: \n",field_5)
print("The values in field6 (Local Temperature) are: \n", field_6)
print("The values in field7 (Local Humidity) are: \n",field_7)

#---- Calculations of mean values ----
field_1 = [float(val) for val in field_1 if val is not None]
field_3 = [float(val) for val in field_3 if val is not None]
field_5 = [float(val) for val in field_5 if val is not None]

#---- Visualizing the values ----
fig, axs = plt.subplots(5, 1, figsize=(8, 10))

#---- First subplot (PM10.0) ----
axs[0].plot(range(len(field_1)), field_1, "-ro")
axs[0].axhline(y=np.mean(field_1), color="r", linestyle="--")
axs[0].set_xlabel("Sample")
axs[0].set_ylabel("ATM")
axs[0].set_title("PM 10.0")

#---- Second subplot (PM2.5) ----
axs[1].plot(range(len(field_3)), field_3, "-ko")
axs[1].axhline(y=np.mean(field_3), color="black", linestyle="--")
axs[1].set_xlabel("Sample")
axs[1].set_ylabel("ATM")
axs[1].set_title("PM 2.5")

#---- Third subplot (PM1.0) ----
axs[2].plot(range(len(field_5)), field_5, "-bo")
axs[2].axhline(y=np.mean(field_5), color="b", linestyle="--")
axs[2].set_xlabel("Sample")
axs[2].set_ylabel("ATM")
axs[2].set_title("PM 1.0")

#---- Fourth subplot (Local Temperature) ----
axs[3].plot(range(len(field_6)), field_6, "-ro")
axs[3].axhline(y=np.mean(field_6), color="r", linestyle="--")
axs[3].set_ylabel("°C")
axs[3].set_title("Local Temperature")

#---- Fifth subplot (Humidity) ----
axs[4].plot(range(len(field_7)), field_7, "-ko")
axs[4].axhline(y=np.mean(field_7), color="black", linestyle="--")
axs[4].set_ylabel("Humidity %")
axs[4].set_title("Local Humidity")

plt.tight_layout()
plt.show()

#------------------------------ AQI Measurements ------------------------------
#---- For PM2.5 ----
def AQI_pm2_5(value):
    if 0 <= value <= 12.0:
        AQI_formula = (((50 - 0) * (value - 0)) / (12 - 0)) + 0
        print("Status: Good")

    elif 12.1 <= value <= 35.4:
        AQI_formula = (((100 - 51) * (value - 12.1)) / (35.4 - 12.1)) + 51
        print("Status: Moderate")

    elif 35.5 <= value <= 55.4:
        AQI_formula = (((150 - 101) * (value - 35.5)) / (55.5 - 35.5)) + 101
        print("Status: Unhealthy for Sensitive groups")

    elif 55.5 <= value <= 150.4:
        AQI_formula = (((200 - 151) * (value - 55.5)) / (150.4 - 55.5)) + 151
        print("Status: Unhealthy")

    elif 150.5 <= value <= 250.4:
        AQI_formula = (((300 - 201) * (value - 150.5)) / (250.4 - 150.5)) + 201
        print("Status: Very Unhealthy")

    elif 250.5 <= value <= 350.4:
        AQI_formula = (((400 - 301) * (value - 250.5)) / (350.4 - 250.5)) + 301
        print("Status: Hazardous")

    elif 350.5 <= value <= 500.4:
        AQI_formula = (((500 - 401) * (value - 350.5)) / (500.4 - 350.5)) + 401
        print("Status: Hazardous")

    AQI_formula = "{:.2f}".format(AQI_formula)
    return AQI_formula

# For PM10.0
def AQI_pm_10(value):
    if 0 <= value <= 54.0:
        AQI_formula = (((50 - 0) * (value - 0)) / (54 - 0)) + 0
        print("Status: Good")

    elif 55 <= value <= 154:
        AQI_formula = (((100 - 51) * (value - 55)) / (154 - 55)) + 51
        print("Status: Moderate")

    elif 155 <= value <= 254:
        AQI_formula = (((150 - 101) * (value - 155)) / (254 - 155)) + 101
        print("Status: Unhealthy for Sensitive group")

    elif 255 <= value <= 354:
        AQI_formula = (((200 - 151) * (value - 255)) / (354 - 255)) + 151
        print("Status: Unhealthy")

    elif 355 <= value <= 424:
        AQI_formula = (((300 - 201) * (value - 355)) / (424 - 355)) + 201
        print("Status: Very Unhealthy")

    elif 425 <= value <= 504:
        AQI_formula = (((400 - 301) * (value - 425)) / (504 - 425)) + 301
        print("Status: Hazardous")

    elif 505 <= value <= 604:
        AQI_formula = (((500 - 401) * (value - 505)) / (604 - 505)) + 401
        print("Status: Hazardous")

    AQI_formula = "{:.2f}".format(AQI_formula)
    return AQI_formula

#---- Initialize empty lists to store AQI values ----
aqi_pm2_5 = []
aqi_pm_10 = []

#---- Calculate AQI for PM2.5 values and store them in aqi_pm2_5 ----
for values in field_3:
    i_pm2_5 = AQI_pm2_5(values)
    aqi_pm2_5.append(i_pm2_5)

#---- Calculate AQI for PM10.0 values and store them in aqi_pm_10 ----
for values in field_1:
    i_pm_10 = AQI_pm_10(values)
    aqi_pm_10.append(i_pm_10)

#---- Print the calculated AQI values for PM2.5 and PM10 ----
print("AQI values for PM2.5 :", aqi_pm2_5)
print("AQI values for PM10.0 :", aqi_pm_10)

#---- Initialize a list to store the maximum AQI values ----
Max_AQI = []

#----Iterate through the first 100 elements in aqi_pm2_5 and aqi_pm_10----
for count in range(99):
    # Check which AQI value is greater, PM2.5 or PM10
    if aqi_pm2_5[count] < aqi_pm_10[count]: #<--- If PM2.5 AQI is less than PM10 AQI
        values = aqi_pm_10[count]           #<--- Assign the PM10 AQI value to v
        Max_AQI.append(values)              #<--- Append the PM10 AQI to the Maximum_AQI list
    else:                                   #<--- If PM10 AQI is less than PM2.5 AQI
        values = aqi_pm2_5[count]           #<--- Assign the PM2.5 AQI value to v
        Max_AQI.append(values)              #<--- Append the PM2.5 AQI to the Maximum_AQI list

#--- Writing all the accessed data to my ThingSpeak Channel ----
#---- Private ThingSpeak Channel ----
channel_id = 2644492
write_key = 'VHD37YVI2ZZQESDE'
channel = thingspeak.Channel(id=channel_id, api_key=write_key)

# Update the cloud channel with PM10.0, PM2.5, PM1.0, Local Temperature, Local Humidity, AQI values for PM2.5, PM10, and Maximum AQI
for i in range(100):
    response = channel.update(
        {'field1': field_1[i],
         'field2': field_3[i],
         'field3': field_5[i],
         'field4': field_6[i],
         'field5': field_7[i],
         'field6': aqi_pm2_5[i],
         'field7': aqi_pm_10[i],
         'field8': Max_AQI[i]
         }
    )
    print(f"Data sent to ThingSpeak: {response}")

    # Delay to update ThingSpeak channel every minute
    time.sleep(60)

#------------------------------ User Interface ------------------------------
#---- Importing necessary libraries ----
import RPi.GPIO as RPI
from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219
from luma.core.render import canvas
from Adafruit_LED_Backpack import SevenSegment

#---- Initialize LED matrix and 7-segment display ----
serial = spi(port=0, device=1, gpio=noop())
device = max7219(serial, cascaded=1, block_orientation=90, rotate=0)
segment_7SD = SevenSegment.SevenSegment(address=0x70)
segment_7SD.begin()

#---- Initialize GPIO with RPi.GPIO ----
gpio_left_button = 25
gpio_right_button = 19
RPI.setmode(RPI.BCM)
RPI.setup(gpio_left_button, RPI.IN, pull_up_down=RPI.PUD_OFF)
RPI.setup(gpio_right_button, RPI.IN, pull_up_down=RPI.PUD_OFF)

pointer = 0 #<--- Pointer for iteration

#---- Infinite loop to continuously update and display value based on 'pointer' ----
while True:
    # Visualize the current value of 'pointer' using LED Matrix Display (LMD)
    with canvas(device) as draw:
        for i in range(5):
            if i == pointer:
                draw.point((i, 0), fill="white")  # Turn on the pixel (white) to indicate the selected value
            else:
                draw.point((i, 0), fill="black")  # Turn off the pixel (black) for other value options

    time.sleep(0.5)

    # Check if the right button is pressed
    if not RPI.input(gpio_right_button):
        pointer = pointer + 1 if pointer < 4 else 0  # Increment 'pointer' to cycle through values 0 to 4
        print("Right button is pressed!")
    # Check if the left button is pressed for 2 seconds
    elif not RPI.input(gpio_left_button):
        pointer = pointer - 1 if pointer > 0 else 4  # Decrement 'pointer' to cycle through values 4 to 0
        print("Left button is pressed!")

    # Visualize and process value based on the value of 'pointer'
    if pointer == 0:
        # Display and visualize value for PM1
        print("PM 1.0 value (press button to change)", pointer)

        mean_PM1 = np.mean(field_5)

        StrMeasurement = str(float(round(mean_PM1, 2)))

        for y in range(0, len(StrMeasurement)):
            segment_7SD.set_digit(y, StrMeasurement[y], decimal=False)  #<--- Display value on 7-segment display
            segment_7SD.set_decimal(1, 1)  #<--- Set decimal point at the second position (if applicable)
        segment_7SD.write_display()

        # Calculate and visualize bar graph for PM1
        draw_graph = [int((sum(field_5[j * 12:(j * 12) + 12]) / 12) / 10) for j in range(8)]
        with canvas(device) as draw:
            for i in range(8):
                draw.point((i, 7 - draw_graph[i]), fill="white")  #<--- Visualize the measurements on the LED Matrix Display (MLD)
        time.sleep(0.5)

    elif pointer == 1:
        # Display and visualize value for PM2.5
        print("PM 2.5 value (press button to change)", pointer)

        mean_PM2_5 = np.mean(field_3)

        StrMeasurement = str(float(round(mean_PM2_5, 2)))

        for y in range(0, len(StrMeasurement)):
            segment_7SD.set_digit(y, StrMeasurement[y], decimal=False)
            segment_7SD.set_decimal(1, 1)
        segment_7SD.write_display()

        # Calculate and visualize bar graph for PM2.5
        draw_graph = [int((sum(field_3[j * 12:(j * 12) + 12]) / 12) / 10) for j in range(8)]
        with canvas(device) as draw:
            for i in range(8):
                draw.point((i, 7 - draw_graph[i]), fill="white")
        time.sleep(0.5)

    elif pointer == 2:
        # Display and visualize value for PM10
        print("PM 10.0 value (press button to change)", pointer)

        mean_PM10 = np.mean(field_1)

        StrMeasurement = str(float(round(mean_PM10, 2)))

        for y in range(0, len(StrMeasurement)):
            segment_7SD.set_digit(y, StrMeasurement[y], decimal=False)
            segment_7SD.set_decimal(1, 1)
        segment_7SD.write_display()

        # Calculate and visualize bar graph for PM10
        draw_graph = [int((sum(field_1[j * 12:(j * 12) + 12]) / 12) / 10) for j in range(8)]
        with canvas(device) as draw:
            for i in range(8):
                draw.point((i, 7 - draw_graph[i]), fill="white")  #<--- Visualize the measurements on the LED Matrix Display (MLD)
        time.sleep(0.5)

    elif pointer == 3:
        # Display and visualize value for Mean Temperature
        print("Temperature value (press button to change)", pointer)

        mean_temp = np.mean(field_6)

        print("Mean Temperature", np.mean(field_6))

        StrMeasurement = str(float(round(mean_temp, 2)))

        for y in range(0, len(StrMeasurement)):
            segment_7SD.set_digit(y, StrMeasurement[y], decimal=False)
            segment_7SD.set_decimal(2, 2)  #<--- Set decimal point at the third position
        segment_7SD.write_display()

        # Calculate and visualize bar graph for Mean Temperature
        draw_graph = [int((sum(field_6[j * 12:(j * 12) + 12]) / 12) / 10) for j in range(8)]
        with canvas(device) as draw:
            for i in range(8):
                draw.point((i, 7 - draw_graph[i]), fill="white")
        time.sleep(0.5)

    elif pointer == 4:
        # Display and visualize value for Mean Humidity
        print("Humidity value (press button to change)", pointer)

        mean_hum = np.mean(field_7)

        print("Mean Humidity", mean_hum)

        StrMeasurement = str(float(round(mean_hum, 2)))

        for y in range(0, len(StrMeasurement)):
            segment_7SD.set_digit(y, StrMeasurement[y], decimal=False)
            segment_7SD.set_decimal(1, 1)
        segment_7SD.write_display()

        # Calculate and visualize bar graph for Mean Humidity
        draw_graph = [int(round((sum(field_7[j * 12:(j * 12) + 12]) / 12) / 100)) for j in range(8)]
        with canvas(device) as draw:
            for i in range(8):
                draw.point((i, 7 - draw_graph[i]), fill="white")
        time.sleep(0.5)