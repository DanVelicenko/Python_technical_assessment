import time
import array
import csv
import matplotlib.pyplot as plt

# User can input start speed
speed = input("Input Your speed (ml/h): ")
print("========== Working ==========")

solarPanel = 0.5
battery = 200
percentage = 100  # Charged battery procents
distance = 0  # Starting distance, with user selected speed
i = 0
timedrive = 0  # Value represents travel duration
dailyTime = 0  # Value used for calculations, represents 12h
deadline = 0  # Starting value for day limitation

# All needed values for research and evaluation are stored in array
timeValue = []
batteryValue = []
distaceValue = []
percentageValue = []

for deadline in range(0, 9, +1):
    # upper battery
    if dailyTime <= 12:     #For mornign time
        if 100 > percentage > 30:
            for i in range(0, 24, +1):  # Loop is set on 24 times, because every acquired data is for 30min travel time
                if battery > 0 and percentage > 0:  # To recheck if after 30 min battery is not empty or negative
                    timedrive += 0.5
                    battery -= (3 / 2)  # car battery consumption for a half a hour
                    battery += (solarPanel / 2)
                    percentage = ((100 * battery) / 200)
                    distance = timedrive * speed
                    time.sleep(0.005)
                    # print(battery, percentage, distance, timedrive)

                #Values such as 'battery', 'timedrive', 'distance', 'percentage' is stored into the array
                batteryValue.append(battery)
                timeValue.append(timedrive)
                distaceValue.append(distance)
                percentageValue.append(percentage)
                dailyTime += 1  #To limit the loop and keep boolean true
    else:
        for i in range(0, 24, +1):  # Loop is set on 24 times, because every acquired data is for 30min travel time
            if battery > 0 and percentage > 0:  # To recheck if after 30 min battery is not empty or negative
                timedrive += 0.5
                battery -= (2 / 2)
                battery += (solarPanel / 2)
                percentage = ((100 * battery) / 200)
                distance = timedrive * speed
                time.sleep(0.005)
                # print(battery, percentage, distance, timedrive)

                # Values such as 'battery', 'timedrive', 'distance', 'percentage' is stored into the array
                batteryValue.append(battery)
                timeValue.append(timedrive)
                distaceValue.append(distance)
                percentageValue.append(percentage)
                dailyTime += 1  #To limit the loop and keep boolean true

    if dailyTime > 12:      #For night time
        for i in range(0, 24, +1):
            if battery > 0 and percentage > 0:
                timedrive += 0.5
                battery -= (3 / 2)
                percentage = ((100 * battery) / 200)
                distance = (timedrive * (speed / 2))
                time.sleep(0.005)
                # print(battery, percentage, distance, timedrive)

                # Values such as 'battery', 'timedrive', 'distance', 'percentage' is stored into the array
                batteryValue.append(battery)
                timeValue.append(timedrive)
                distaceValue.append(distance)
                percentageValue.append(percentage)
                dailyTime += 1  #To limit the loop and keep boolean true
    else:
        for i in range(0, 24, +1):
            if battery > 0 and percentage > 0:
                timedrive += 0.5
                battery -= (2 / 2)
                percentage = ((100 * battery) / 200)
                distance = (timedrive * (speed / 2))
                time.sleep(0.005)
                # print(battery, percentage, distance, timedrive)

                # Values such as 'battery', 'timedrive', 'distance', 'percentage' is stored into the array
                batteryValue.append(battery)
                timeValue.append(timedrive)
                distaceValue.append(distance)
                percentageValue.append(percentage)
                dailyTime += 1  #To limit the loop and keep boolean true

#Prints into the console acquired data only last positive points
print("Last positive battery value (KWh): ")
print(batteryValue[-2])
print("Travel time (h): ")
print(timeValue[-2])
print("Travel distance (mil): ")
print(distaceValue[-2])
print("Percents left (%): ")
print(percentageValue[-2])

print("Data acquired from tests, exports CSV and PNG format files in the same directory of main.py file")

#Acquired data is saved and exported into the CSV file
with open("out.csv", "wb") as file:
    writer = csv.writer(file)

    #Following data was choosen to be saved
    writer.writerow(batteryValue)
    writer.writerow(timeValue)
    writer.writerow(distaceValue)

#MatplotLib exports graph of acquired results
plt.plot(timeValue, distaceValue)
plt.xlabel('Travel time (h)')
plt.ylabel('Distance (mil)')

#Filename used to save graph
plt.savefig('results.png')
