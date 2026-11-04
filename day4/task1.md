# المهمة ١: اختر الهيكل المناسب

## ١. الجدول

| الهيكل | مرتب؟ | قابل للتعديل؟ | يسمح بالتكرار؟ | كيف أصل للعنصر؟ | مثال |
|---|---|---|---|---|---|
| list | نعم | نعم | نعم | بالفهرس x[0] | ["Ahmed", "Sara", "Mona"] |
| tuple | نعم | لا | نعم | بالفهرس x[0] | ("black", "white", "green") |
| set | لا | نعم | لا | باستخدام in | {"Math", "Physics", "English"} |
| dict | نعم | نعم | المفاتيح لا تتكرر | بالمفتاح x["name"] | {"name": "Kholoud", "major": "AI"} |

## ٢. توقع الناتج

```python
skills = ["Python", "Git", "SQL"]
skills.append("Pandas")
skills.insert(1, "Excel")
print(skills, len(skills))
```

الناتج:

```python
['Python', 'Excel', 'Git', 'SQL', 'Pandas'] 5
```

```python
print(skills[1], skills[-1], skills[1:3])
```

الناتج:

```python
Excel Pandas ['Excel', 'Git']
```

```python
ids = {101, 102, 101, 103}
print(len(ids), 104 in ids)
```

الناتج:

```python
3 False
```

السبب: لأن set لا تسمح بالتكرار.

```python
emp = {"name": "Sara", "role": "AI Engineer"}
print(emp.get("team", "Not set"))
emp["team"] = "R&D"
print(len(emp), list(emp.keys()))
```

الناتج:

```python
Not set
3 ['name', 'role', 'team']
```

السبب: لم يكن هناك مفتاح باسم team ثم تمت إضافته.

## ٣. فخ شائع

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)

c = a.copy()
c.append(5)
print(a, c)
```

الناتج:

```python
[1, 2, 3, 4]
[1, 2, 3, 4] [1, 2, 3, 4, 5]
```

- يشير b لنفس القائمة a لذلك تغيرت a.
- تنشئ copy() قائمة جديدة لذلك لم تتغير a عند تعديل c.
- التشبيه: b = a مثل ملف مشترك على Google Drive، أي تعديل يظهر للطرفين. أما copy() فمثل ما أحفظ نسخة على جهازي وأعدل عليها بدون ما يتغير الملف الأصلي.

## ٤. أي هيكل أستخدم؟

- إحداثيات موقع: tuple لأن الإحداثيات ثابتة.
- قائمة مهام: list لأن أقدر أضيف وأحذف منها.
- أسماء بدون تكرار: set لأنها تمنع التكرار.
- بيانات شخص: dict لأن كل معلومة لها مفتاح خاص.

## أمثلة من حياتي

- list: أسماء الطلاب.
- tuple: الألوان المفضلة.
- set: المواد الدراسية.
- dict: بياناتي الشخصية.

```python
students = ["Ahmed", "Sara", "Mona"]
colors = ("black", "white", "green")
subjects = {"Math", "Physics", "English"}
person = {"name": "Kholoud", "major": "AI"}
```