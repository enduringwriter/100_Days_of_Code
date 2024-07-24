import csv
from pathlib import Path
from matplotlib import pyplot as plt
from datetime import datetime

filename = Path("/Users/keithstateson/DS_Py_101/Class_Notes/New_Downloading_Data/sitka_weather_07_2014.csv")

# get file and header row
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # view header row
    # print(header_row) is too messy, see next block of code to clean up header output
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # get dates and high temperatures from file
    dates, highs = [], []
    for row in reader:
        highs.append(int(row[1]))
        
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

print(highs)

# plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')

# format plot
plt.title("Daily High Temperatures, July 2014", fontsize=24)
fig.autofmt_xdate()
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
