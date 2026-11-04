MISSION_DAYS = 75

crew = ("Nora", "Omar", "Lina", "Yousef")

supplies = {
    "oxygen_kg": 840,
    "water_l": 1260,
    "food_kg": 336
}

per_person_daily = {
    "oxygen_kg": 0.84,
    "water_l": 3.5,
    "food_kg": 1.2
}

telescope_a = {
    "Kepler-22b",
    "Proxima b",
    "TRAPPIST-1e",
    "Gliese 667Cc"
}

telescope_b = {
    "Proxima b",
    "TRAPPIST-1e",
    "HD 40307g"
}

# 1
n = len(crew)

days_left = {
    "oxygen_kg": supplies["oxygen_kg"] / (per_person_daily["oxygen_kg"] * n),
    "water_l": supplies["water_l"] / (per_person_daily["water_l"] * n),
    "food_kg": supplies["food_kg"] / (per_person_daily["food_kg"] * n)
}

print(days_left)

# 2
# key=days_left.get يجعل min تقارن بعدد الأيام المتبقية وليس باسم المورد
weakest = min(days_left, key=days_left.get)
print(weakest)

# 3
print(days_left[weakest] >= MISSION_DAYS)
print(MISSION_DAYS - days_left[weakest])

# عند تجربة MISSION_DAYS = 70 تصبح النتيجة True
# لأن الطعام يكفي 70 يوم بالضبط

# 5
print(telescope_a & telescope_b)
print(telescope_a - telescope_b)
print(len(telescope_a | telescope_b))

# 6
mission_log = ["Launch", "Orbit reached", "Engine check"]

print(mission_log[-1], len(mission_log))

# 7
# استخدمنا tuple لأن أسماء الطاقم ثابتة ولا نحتاج لتغييرها.