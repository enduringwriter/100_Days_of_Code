import csv
from matplotlib import pyplot as plt
from datetime import datetime

# import file
filename = "sitka_weather_07-2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # get high temperatures from file
    highs, lows = [], []
    for row in reader:
        high = int(row[1])
        low = int(row[3])
        highs.append(high)
        lows.append(low)

# plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')
plt.plot(lows, c='blue')

# format plot
plt.title("Daily high/low temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
