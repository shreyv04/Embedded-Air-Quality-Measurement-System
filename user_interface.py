# Shrey Rahulkumar Vyas

#---- Importing all necessary libraries ----
import RPi.GPIO as GPIO
from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219
from luma.core.render import canvas
from time import sleep
from Adafruit_LED_Backpack import SevenSegment
from getdata import field_1, field_3, field_5, field_6, field_7
import numpy as np

# Initialize LED matrix and 7-segment display
serial = spi(port=0, device=1, gpio=noop())
device = max7219(serial, cascaded=1, block_orientation=90, rotate=0)
segment_7SD = SevenSegment.SevenSegment(address=0x70)
segment_7SD.begin()

# Initialize GPIO with RPi.GPIO
gpio_left_button = 26
gpio_right_button = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_left_button, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
GPIO.setup(gpio_right_button, GPIO.IN, pull_up_down=GPIO.PUD_OFF)

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

    sleep(0.5)

    # Check if the right button is pressed
    if not GPIO.input(gpio_right_button):
        pointer = pointer + 1 if pointer < 4 else 0  # Increment 'pointer' to cycle through values 0 to 4
        print("Right button is pressed!")
    # Check if the left button is pressed for 2 seconds
    elif not GPIO.input(gpio_left_button):
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
        sleep(0.5)

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
        sleep(0.5)

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
        sleep(0.5)

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
        sleep(0.5)

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
        sleep(0.5)
