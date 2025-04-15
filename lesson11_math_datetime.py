# Math & DateTime Module Example
import math
import datetime
import calendar

# Math Module
print("Square root of 16:", math.sqrt(16))
print("Value of Pi:", math.pi)
print("Sin(90 degrees):", math.sin(math.radians(90)))

print("\n--- Date & Time ---")
# DateTime Module
now = datetime.datetime.now()
print("Current Date & Time:", now)

# Creating specific date
birthday = datetime.date(2025, 5, 25)
print("My Birthday:", birthday)

print("\n--- Calendar ---")
# Calendar Module
print(calendar.month(2025, 5))
