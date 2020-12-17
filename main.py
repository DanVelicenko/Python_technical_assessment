import time
# import array not needed
import csv
import matplotlib.pyplot as plt

if __name__ == '__main__':  # THIS IS A MAIN METHOD SO YOU HAVE TO SPECIFY IT
    # User can input start speed
    speed = float(input("Input Your speed (ml/h): "))  # Conversion of string to float
    print("========== Working ==========")

    solarPanel = 0.5  # kW/h
    battery = 200
    percentage = 100  # Charged battery percents
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
        print(dailyTime)
        if dailyTime <= 12:  # For morning time and full battery
            if 100 > percentage > 30:  # Once is int he loop, it wont get out even if the battery is lower than 30%. The if should go after the loop
                for i in range(0, 24,
                               +1):  # Loop is set on 24 times, because every acquired data is for 30min travel time
                    if battery > 0 and percentage > 0:  # To recheck if after 30 min battery is not empty or negative
                        timedrive += 0.5
                        battery -= (((speed * 1) / 3) / 2)  # day, battery > 30%, 30 min
                        distance += ((speed * 30) / 60)  # distance, day, 30min
                        battery += (solarPanel / 2)
                        percentage = ((100 * battery) / 200)
                        time.sleep(0.005)
                        print(battery, percentage, distance, timedrive)

                # Values such as 'battery', 'timedrive', 'distance', 'percentage' is stored into the array
                        batteryValue.append(battery)
                        timeValue.append(timedrive)
                        distaceValue.append(distance)
                        percentageValue.append(percentage)
                        dailyTime += 1  # To limit the loop and keep boolean true
            # THIS ELSE I THINK IS ONE LEVEL DOWN AND IT SHOULD BE FOR if 100 > percentage > 30:

        else:  # morning, battery < 30%
            for i in range(0, 24, +1):  # Loop is set on 24 times, because every acquired data is for 30min travel time
                if battery > 0 and percentage > 0:  # To recheck if after 30 min battery is not empty or negative
                    timedrive += 0.5
                    distance += ((speed * 30) / 60)  # distance, day, 30min
                    battery -= ((speed * 1) / (2 / 2))  # at day, if battery < 30%, 30 min
                    battery += (solarPanel / 2)
                    percentage = ((100 * battery) / 200)
                    time.sleep(0.005)
                    print(battery, percentage, distance, timedrive)

                    # Values such as 'battery', 'timedrive', 'distance', 'percentage' is stored into the array
                    batteryValue.append(battery)
                    timeValue.append(timedrive)
                    distaceValue.append(distance)
                    percentageValue.append(percentage)
                    dailyTime += 1  # To limit the loop and keep boolean true

        if dailyTime > 12:  # For night time # AFTER 24h this will stop working because you dont reset dailyTime to 0
            for i in range(0, 24, +1):
                if battery > 0 and percentage > 0:
                    timedrive += 0.5
                    distance += (((speed / 2) * 30) / 60)  # distance, night, 30min, 50% less speed
                    battery -= ((((speed / 2) * 1) / 3) / 2)  # night, battery > 30%, 30 min
                    percentage = ((100 * battery) / 200)
                    time.sleep(0.005)
                    print(battery, percentage, distance, timedrive)

                    # Values such as 'battery', 'timedrive', 'distance', 'percentage' is stored into the array
                    batteryValue.append(battery)
                    timeValue.append(timedrive)
                    distaceValue.append(distance)
                    percentageValue.append(percentage)
                    dailyTime += 1  # To limit the loop and keep boolean true
                    if dailyTime == 24:
                        break
        else:
            for i in range(0, 24, +1):
                if battery > 0 and percentage > 0:
                    timedrive += 0.5
                    distance += (((speed / 2) * 30) / 60)  # distance, night, 30min, 50% less speed
                    battery -= ((((speed / 2) * 1) / 2) / 2)  # at night, if battery under 30%, 30 min
                    percentage = ((100 * battery) / 200)
                    time.sleep(0.005)
                    print(battery, percentage, distance, timedrive)

                    # Values such as 'battery', 'timedrive', 'distance', 'percentage' is stored into the array
                    batteryValue.append(battery)
                    timeValue.append(timedrive)
                    distaceValue.append(distance)
                    percentageValue.append(percentage)
                    dailyTime += 1  # To limit the loop and keep boolean true
                    if dailyTime == 24:
                        break

    # Prints into the console acquired data only last positive points
    print("Last positive battery value (KWh): ")
    print(batteryValue[-2])
    print("Travel time (h): ")
    print(timeValue[-2])
    print("Travel distance (mil): ")
    print(distaceValue[-2])
    print("Percents left (%): ")
    print(percentageValue[-2])

    print("Data acquired from tests, exports CSV and PNG format files in the same directory of main.py file")

    # Acquired data is saved and exported into the CSV file
    with open("out.csv", "wb") as file:
        writer = csv.writer(file)

        # Following data was chosen to be saved
        print(batteryValue)
        print(timeValue)
        print(distaceValue)
        # writer.writerow(batteryValue) # IM NOT SURE WHATS WRONG HERE, I THINK IS ASKING FOR A DIFFERENT FORMAT
        # writer.writerow(timeValue)
        # writer.writerow(distaceValue)

    # MatplotLib exports graph of acquired results
    plt.plot(timeValue, distaceValue)
    plt.xlabel('Travel time (h)')
    plt.ylabel('Distance (mil)')

    # Filename used to save graph
    plt.savefig('results.png')

