# Task 1

| السطر | توقعي قبل التشغيل | الناتج الفعلي | سبب الاختلاف |
|---|---|---|---|
| `print(type(a), type(b))` | str int | `<class 'str'> <class 'int'>` | بايثون يطبع النوع بصيغة class |
| `print(a * b)` | 21 | `777` | a نص، فضرب النص في 3 يكرره 3 مرات |
| `print(int(a) * b)` | 21 | `21` | ما في اختلاف، حولت "7" لرقم وضربته |
| `print(a + str(b))` | 10 | `73` | حولت 3 لنص، فصار دمج نصين مو جمع أرقام |
| `print(int(a) / b)` | 2.33 | `2.3333333333333335` | القسمة العادية ترجع كسر، وبايثون يطبع الكسر بأرقام طويلة |
| `print(int(a) // b, int(a) % b)` | 2 1 | `2 1` | ما في اختلاف، // للخارج و % للباقي |

## المهمة 2

المتغير مثل علبة عليها اسم، نحط فيها شي ونطلعه وقت ما نبي.
مثل علبة السكر بالمطبخ، الاسم ثابت واللي داخلها يتغير.
في البرمجة نسمي العلبة `age` ونحط فيها رقم، وبعدين نبدله.

## المهمة 3

```python
name = input("Your name: ")
age = input("Your age: ")
print("Hello " + name + ", in 5 years you will be " + age + 5)
```

**(أ) رسالة الخطأ:**
`TypeError: can only concatenate str (not "int") to str`

**(ب) السبب:** `age` جاي من `input()` فهو نص، و`5` رقم، وما أقدر أدمج نص مع رقم بـ `+`.

**(ج) الإصلاح:**

بالدمج `+`:
```python
print("Hello " + name + ", in 5 years you will be " + str(int(age) + 5))
```

بالـ f-string:
```python
print(f"Hello {name}, in 5 years you will be {int(age) + 5}")
```

## المهمة 4

لما جربت `int(input("Your age: "))` وكتبت `twenty` طلعت الرسالة:
`ValueError: invalid literal for int() with base 10: 'twenty'`

**معناها:** `int()` ما تقدر تحول الكلمة `twenty` لرقم لأنها حروف مو أرقام.

**ليش `input()` ترجع نص دائمًا؟** لأنها تستقبل اللي يكتبه المستخدم كما هو، وما تعرف هل هو رقم أو كلمة، فأنا اللي أحوله بـ `int()` أو `float()`.