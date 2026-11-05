trainees = [
    {"name": "Sara", "checkin": "09:40", "on_time": 5, "report_on_time": False, "scores": [8, 8, 8, 8, 8]},
    {"name": "Omar", "checkin": "10:15", "on_time": 4, "report_on_time": True, "scores": [9, 9, 9, 9, 0]},
    {"name": "Lina", "checkin": "08:55", "on_time": 5, "report_on_time": True, "scores": [10, 9, 9, 10, 8]},
    {"name": "Kholoud", "checkin": "09:00", "on_time": 5, "report_on_time": True, "scores": [10, 10, 10, 10, 8]}
]

total_tasks = 5


def to_minutes(time_text):
    hours, minutes = time_text.split(":")
    return int(hours) * 60 + int(minutes)


def daily_points(checkin, on_time, total_tasks, report_on_time, scores):
    points = 0

    if to_minutes(checkin) < to_minutes("10:00"):
        points += 5

    if total_tasks > 0:
        points += (on_time / total_tasks) * 10

    if report_on_time:
        points += 5

    if total_tasks > 0:
        points += (sum(scores) / (10 * total_tasks)) * 10

    return round(points, 1)


total_points = 0
best_name = ""
best_points = 0

for trainee in trainees:
    trainee["points"] = daily_points(
        trainee["checkin"],
        trainee["on_time"],
        total_tasks,
        trainee["report_on_time"],
        trainee["scores"]
    )

    print(trainee["name"], ":", trainee["points"])

    total_points += trainee["points"]

    if trainee["points"] > best_points:
        best_points = trainee["points"]
        best_name = trainee["name"]

average = round(total_points / len(trainees), 1)

print("-" * 20)
print("Total Points:", total_points)
print("Average:", average)
print("Best of the Day:", best_name, "(" + str(best_points) + " points)")

raw_difference = trainees[3]["points"] - trainees[2]["points"]

print("Difference:", raw_difference)
print("Difference rounded:", round(raw_difference, 1))

print("-" * 20)
print("No Tasks Test:")
print(daily_points("09:00", 0, 0, True, []))

# Lina:
# حضور مبكر = 5
# المهام = 10
# التقرير = 5
# الجودة = 9.2
# المجموع = 29.2

# Kholoud:
# حضور مبكر = 5
# المهام = 10
# التقرير = 5
# الجودة = 9.6
# المجموع = 29.6

# اخترت الدرجات [10, 10, 10, 10, 8]
# لأن مجموعها 48، وبالتالي جودة العمل = 48 ÷ 50 × 10 = 9.6
# وهذا جعل نتيجتي أعلى من Lina بمقدار 0.4 نقطة.

# لاحظت أن الفرق ظهر كرقم طويل:
# 0.40000000000000213
# وبعد استخدام round أصبح 0.4
# لأن الكمبيوتر يخزن بعض الأعداد العشرية بشكل تقريبي.