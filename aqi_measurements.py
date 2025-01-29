# Shrey Rahulkumar Vyas [30460285]

#---- Fetching required data from getdata.py file ----
from getdata import field_1, field_3
#---- Importing all necessary libraries ----
import thingspeak
import time

#Accessing my ThinkSpeak Channel
channel_id = 2644492
write_key = 'VHD37YVI2ZZQESDE'
channel = thingspeak.Channel(id=channel_id, api_key=write_key)

#---- AQI Measurements ----
# For PM2.5
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

# Update the cloud channel with AQI values for PM2.5, PM10, and Maximum AQI
for i in range(99):
    response = channel.update(
        {'field6': aqi_pm2_5[i],
         'field7': aqi_pm_10[i],
         'field8': Max_AQI[i]
         }
    )
    print(f"Data sent to ThingSpeak: {response}")

    time.sleep(60) #<--- Add delay of 60sec to update channel
