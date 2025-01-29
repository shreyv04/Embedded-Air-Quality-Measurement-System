# This program is jointly done by Shrey Vyas, Vandan Deria, and Dhyanam Pandya
# Shrey Rahulkumar Vyas [30460285]

#---- Importing all necessary libraries ----
import requests
import json
import random

# Conversion of string message to a JSON message object
cloud_data = requests.get('https://thingspeak.com/channels/343018/feed.json')
cloud_data = str(cloud_data.text)
cloud_data_json = json.loads(cloud_data)

# Getting the feeds from the selected channel
feeds = cloud_data_json['feeds']

# Initialize lists for fields
field_1 = []
field_2 = []
field_3 = []
field_4 = []
field_5 = []
field_6 = []
field_7 = []

# Extracting data for the first 100 entries
for i in range(100):
    field_1.append(feeds[i]['field1'])
    field_3.append(feeds[i]['field3'])
    field_5.append(feeds[i]['field5'])

# Randomize temperature (15-16°C) and humidity (25-27%)
field_6 = [round(random.uniform(15, 16), 2) for _ in range(100)]
field_7 = [round(random.uniform(25, 27), 2) for _ in range(100)]


# Print extracted fields for verification
print("The values in field1 (PM10.0) are\n", field_1)
print("The values in field3 (PM2.5) are\n", field_3)
print("The values in field5 (PM1.0) are\n", field_5)
print("The Local Temperature values are\n", field_6)
print("The Local Humidity values are\n", field_7)

# Calculations of mean values
field_1 = [float(val) for val in field_1 if val is not None]
field_3 = [float(val) for val in field_3 if val is not None]
field_5 = [float(val) for val in field_5 if val is not None]