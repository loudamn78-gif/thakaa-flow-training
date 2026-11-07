distance = float(input("Distance (million km): "))
age = float(input("Your age (Earth years): "))
weight = float(input("Your weight on Earth (kg): "))

SPEED_OF_LIGHT = 299792  # km/s

seconds = int(distance * 1_000_000 / SPEED_OF_LIGHT)
minutes = seconds // 60
sec = seconds % 60

round_trip = seconds * 2
rt_hours = round_trip // 3600
rt_minutes = (round_trip % 3600) // 60
rt_sec = round_trip % 60

age_mars = age * 365.25 / 687
weight_mars = weight * 0.38

sol_seconds = 24 * 3600 + 39 * 60 + 35
sols_per_week = 7 * 24 * 3600 / sol_seconds

print("=== MARS MISSION REPORT ===")
print(f"Message travel time: {minutes} min {sec} sec")
print(f"Round trip: {rt_hours} h {rt_minutes} min {rt_sec} sec")
print(f"Your age on Mars: {age_mars:.2f} years")
print(f"Your weight on Mars: {weight_mars:.2f} kg")
print(f"One Earth week = {sols_per_week:.2f} Mars sols")

# 8) الإشارة تأخذ دقائق طويلة ذهابًا، وأكثر منها ذهابًا وإيابًا،
# فالرد يتأخر كثير، والمكالمة الفيديو المباشرة تحتاج تأخير بالثواني فقط.