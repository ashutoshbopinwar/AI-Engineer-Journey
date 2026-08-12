import numpy as np

# -----------------------------
# Weather Data Analyzer
# -----------------------------

days = np.array([
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
])

# Temperature (°C), Humidity (%), Rainfall (mm)
weather = np.array([
    [32, 70, 2],
    [34, 65, 0],
    [31, 80, 5],
    [29, 85, 10],
    [35, 60, 0],
    [36, 55, 0],
    [33, 68, 1]
])

temperature = weather[:,0]
humidity = weather[:,1]
rainfall = weather[:,2]

print("-"*60)
print("           WEATHER ANALYZER")
print("-"*60)

print("\n Daily Weather Report \n")

for i in range(len(days)):
    
    if rainfall[i] > 5:
        status = "Heavy Rain"
    elif rainfall[i] > 0 :
        status = "Rainy"
    elif temperature[i] >= 35 :
        status = "Sunny"
    elif humidity[i] >= 75 :
        status = "Cloudy"
    else:
        status = "Pleasant"
        
    print("_"*60)

    print(f"Day               : {days[i]}")
    print(f"Temperature       : {temperature[i]}")
    print(f"Humidity          : {humidity[i]}")
    print(f"Rainfall          : {rainfall[i]}")
    print(f"Weather           : {status}")

print("\n" + "=" * 60)
print("              WEEKLY WEATHER REPORT")
print("=" * 60)

highest_temp = np.max(temperature)
lowest_temp = np.min(temperature)
average_temp = np.mean(temperature)


highest_humidity = np.max(humidity)
lowest_humidity = np.min(humidity)
average_humidity = np.mean(humidity)

total_rainfall = np.sum(rainfall)
average_rainfall = np.mean(rainfall)

hottest_day = days[np.argmax(temperature)]
coldest_day = days[np.argmin(temperature)]
rainiest_day = days[np.argmax(rainfall)]

print(f"\nHighest Temperature : {highest_temp} °C")
print(f"Lowest Temperature  : {lowest_temp} °C")
print(f"Average Temperature : {average_temp:.2f} °C")

print(f"\nHighest Humidity    : {highest_humidity} %")
print(f"Lowest Humidity     : {lowest_humidity} %")
print(f"Average Humidity    : {average_humidity:.2f} %")

print(f"\nTotal Rainfall      : {total_rainfall} mm")
print(f"Average Rainfall    : {average_rainfall:.2f} mm")

print(f"\nHottest Day         : {hottest_day}")
print(f"Coldest Day         : {coldest_day}")
print(f"Rainiest Day        : {rainiest_day}")

print("\nDays With No Rain")

no_rain = np.where(rainfall == 0)

for index in no_rain[0]:
    print(days[index])

print("\n Days Above 33°C")

hot_days = np.where(temperature > 33)

for index in hot_days[0]:
    print(days[index], "-" , temperature[index], "°C")
    
humid_days = np.where(humidity > 75)

for index in humid_days[0]:
    print(days[index], "-", humidity[index], "%")
    
print("\n" + "=" * 60)
print("               END OF REPORT")
print("=" * 60)