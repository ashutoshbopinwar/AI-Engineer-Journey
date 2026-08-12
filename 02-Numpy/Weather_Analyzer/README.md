# 🌤️ Weather Data Analyzer

This is my second NumPy project as part of my AI Engineering learning journey.

I built this project to practice working with weather data using NumPy. The program takes temperature, humidity, and rainfall data for a week and performs different calculations and analysis on it.

## What does this project do?

The program can:

- Show the weather information for each day
- Find the highest and lowest temperature
- Calculate the average temperature
- Find the hottest and coldest day
- Find the day with the most rainfall
- Calculate total and average rainfall
- Find the highest and lowest humidity
- Find days with no rainfall
- Find days where the temperature is above 33°C
- Find days where humidity is above 75%
- Give a simple weather status such as Sunny, Rainy, Cloudy, etc.

## Data Used

I used sample data for 7 days:

| Day | Temperature | Humidity | Rainfall |
|---|---:|---:|---:|
| Monday | 32°C | 70% | 2 mm |
| Tuesday | 34°C | 65% | 0 mm |
| Wednesday | 31°C | 80% | 5 mm |
| Thursday | 29°C | 85% | 10 mm |
| Friday | 35°C | 60% | 0 mm |
| Saturday | 36°C | 55% | 0 mm |
| Sunday | 33°C | 68% | 1 mm |

## Technologies

- Python
- NumPy
- VS Code
- Git & GitHub

## NumPy Concepts I Practiced

While building this project, I practiced:

- NumPy arrays
- 2D arrays
- Array slicing
- Indexing
- `np.max()`
- `np.min()`
- `np.mean()`
- `np.sum()`
- `np.argmax()`
- `np.argmin()`
- `np.where()`

I also got more comfortable with Python `for` loops and `if-elif-else` conditions.

## Sample Output

The program generates a daily weather report and a weekly summary.

```text
============================================================
              WEEKLY WEATHER REPORT
============================================================

Highest Temperature : 36 °C
Lowest Temperature  : 29 °C
Average Temperature : 32.86 °C

Highest Humidity    : 85 %
Lowest Humidity     : 55 %
Average Humidity    : 69.00 %

Total Rainfall      : 18 mm
Average Rainfall    : 2.57 mm

Hottest Day         : Saturday
Coldest Day         : Thursday
Rainiest Day        : Thursday