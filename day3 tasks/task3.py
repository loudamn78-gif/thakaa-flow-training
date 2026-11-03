name = input("Name: ")
email = input("Email: ")
phone = input("Phone: ")

# تنظيف الاسم
clean_name = name.strip().title()

# تنظيف البريد
clean_email = email.strip().lower()
is_valid_email = ("@" in clean_email) and (not clean_email.startswith("@"))

# تنظيف ورقم الجوال
clean_phone = phone.replace(" ", "")
is_valid_phone = clean_phone.isdigit() and clean_phone.startswith("05") and len(clean_phone) == 10

# التاكد من صحة الحقول
errors = []
if not clean_name:
    errors.append("Invalid Name")
if not is_valid_email:
    errors.append("Invalid Email")
if not is_valid_phone:
    errors.append("Invalid Phone")

if errors:
    for err in errors:
        print(err)
else:
    # استخراج اسم المستخدم (الاسم الأول بحروف صغيرة + نقطة + آخر رقمين من الجوال) بدون استخدام split
    first_name_end = clean_name.find(" ")
    if first_name_end != -1:
        first_name = clean_name[:first_name_end].lower()
    else:
        first_name = clean_name.lower()
    
    username = first_name + "." + clean_phone[-2:]
    
    print(f"{clean_name} | {clean_email} | {clean_phone} OK")
    print(f"Suggested username: {username}")
