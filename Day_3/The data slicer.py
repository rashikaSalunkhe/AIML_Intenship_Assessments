temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]

# First and last readings
first_reading = temperatures[0]
last_reading = temperatures[-1]

# Afternoon Peak (4th, 5th, 6th items)
afternoon_peak = temperatures[3:6]

# Last 3 hours
last_three_hours = temperatures[-3:]

# Output with clear labels
print("Temperature Readings:", temperatures)
print("First Reading:", first_reading)
print("Last Reading:", last_reading)
print("Afternoon Peak Readings:", afternoon_peak)
print("Last 3 Hours Readings:", last_three_hours)