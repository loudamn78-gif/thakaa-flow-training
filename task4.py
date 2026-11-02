customer = input("Customer name: ")
service = input("Service: ")
date = input("Date: ")
time = input("Time: ")
price = float(input("Service price: "))
booking_no = int(input("Booking number: "))
minutes = int(input("Session length (minutes): "))

# غيّرت سطر deposit فقط لأن العربون محسوب في مكان واحد، وباقي الأسطر (remaining والرسالة) تعتمد عليه تلقائيًا.
deposit = price * 0.25
remaining = price - deposit

hours = minutes // 60
mins = minutes % 60

code = f"TF-2026-{booking_no:04d}"

message = f"""Hello {customer},
Your booking for "{service}" is confirmed.
Date: {date} at {time}
Session length: {hours} h {mins} min
Booking code: {code}
Deposit due: {deposit:.2f} SAR
Remaining on delivery: {remaining:.2f} SAR
Thank you for choosing Thakaa Flow!"""

print(message)