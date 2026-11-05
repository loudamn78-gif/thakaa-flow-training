days = ["Sun", "Mon", "Tue", "Wed", "Thu"]
sales = [1200, 950, 1800, 1430, 2100]

total = 0
best_sale = sales[0]
best_day = days[0]
above_target = 0

for i in range(len(sales)):
    print(days[i] + ":", sales[i], "SAR")

    total += sales[i]

    if sales[i] > best_sale:
        best_sale = sales[i]
        best_day = days[i]

    if sales[i] > 1500:
        above_target += 1

average = total // len(sales)

print()
print("Total:", total, "SAR")
print("Average:", average, "SAR")
print("Best day:", best_day, "(" + str(best_sale) + " SAR)")
print("Days above target:", above_target)

# استخدمت range(len(sales))
# لأنني أحتاج رقم العنصر للوصول إلى اليوم والمبيعات معاً.
# لو استخدمت for s in sales سأحصل على المبيعات فقط.
#استخدمت\\لتطابق شكل المخرجات