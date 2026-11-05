# دالة إضافة الضريبة
def add_vat(amount, rate=0.15):
    return round(amount + amount * rate, 2)


# دالة تنسيق السعر
def format_price(amount):
    return f"{amount:,.2f} SAR"


# دالة التحقق من رقم الجوال
def is_valid_phone(phone):
    phone = phone.replace(" ", "")
    return phone.isdigit() and phone.startswith("05") and len(phone) == 10


# اختبار الدوال
print("VAT Test:")
print(add_vat(100))
print(add_vat(250, 0.05))
print(add_vat(0))

print("-" * 20)

print("Price Test:")
print(format_price(1234.5))
print(format_price(99))
print(format_price(1000000))

print("-" * 20)

print("Phone Test:")
print(is_valid_phone("0551234567"))
print(is_valid_phone("055 123 4567"))
print(is_valid_phone("05abc12345"))

print("-" * 20)

# استخدام دالتين مع بعض
print(format_price(add_vat(1000)))

print("-" * 20)

# طباعة الأرقام الصحيحة فقط
phones = [
    "0551234567",
    "0661234567",
    "055 123 4567",
    "05512",
    "05abc12345"
]

valid_count = 0

for phone in phones:
    if is_valid_phone(phone):
        print(phone)
        valid_count += 1

print("Valid phones:", valid_count)