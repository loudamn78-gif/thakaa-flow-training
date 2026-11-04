| السطر البرمجي | المتوقع | الفعلي | سبب الاختلاف |
| :--- | :--- | :--- | :--- |
| `print(clean.lower())` | sara.ahmed@tfco.sa | sara.ahmed@tfco.sa | متشابهين تماماً |
| `print(email.count("a"), clean.lower().count("a"))` | 4, 4 | 4, 4 | نفس النتيجة |
| `print("tfco" in email, "tfco" in clean.lower())` | False, True | False, True | لأن النص الأصلي فيه حروف كبيرة TFCO |
| `print(clean.startswith("sara"))` | True | True | نفس النتيجة |
| `print(len(email), len(clean))` | 19, 17 | 19, 17 | دالة len تحسب الفراغات قبل ما نحذفها بـ strip |
| `print(clean[:4], clean[-2:])` | sara, sa | sara, sa | نفس النتيجة |
