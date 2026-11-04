registered = [
    "sara@mail.com",
    "omar@mail.com",
    "lina@mail.com",
    "sara@mail.com",
    "yousef@mail.com",
    "nora@mail.com"
]

attended = [
    "omar@mail.com",
    "lina@mail.com",
    "khaled@mail.com",
    "nora@mail.com"
]

tickets = ["VIP", "Regular", "Regular", "Student", "VIP", "Regular"]

prices = {
    "VIP": 450,
    "Regular": 200,
    "Student": 100
}

# 1
dup = len(registered) - len(set(registered))
print(dup)

# 2
reg = set(registered)
att = set(attended)

both = reg & att

print(both)
print(reg - att)
print(att - reg)

# 3
rate = len(both) / len(reg) * 100
print(rate)

# 4
counts = {
    "VIP": tickets.count("VIP"),
    "Regular": tickets.count("Regular"),
    "Student": tickets.count("Student")
}

print(counts)

total = (
    counts["VIP"] * prices["VIP"]
    + counts["Regular"] * prices["Regular"]
    + counts["Student"] * prices["Student"]
)

print(total)

# 5
print("--- تقرير الورشة ---")
print("المسجلون:", sorted(reg))
print("الحاضرون:", sorted(att))
print("سجل وحضر:", sorted(both))
print("سجل وما حضر:", sorted(reg - att))
print("حضر بدون تسجيل:", sorted(att - reg))
print(f"نسبة الحضور: {rate:.1f}%")
print(f"الإيراد: {total} ريال")

# 6
# لأن set لا تحفظ ترتيب العناصر، لذلك قد يختلف ترتيب الطباعة من مرة إلى أخرى.
# وإذا أريد ترتيب ثابت أستخدم sorted().