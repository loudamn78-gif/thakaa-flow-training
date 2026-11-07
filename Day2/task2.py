name = "Khouloud Al-Saadi"
city = "Riyadh"
major = "Artificial Intelligence"
age = 29
coded_before = True
study_hours = 3.5

# 1) بالدمج +
print("=== " + name + " ===")
print("City: " + city)
print("Major: " + major)
print("Age: " + str(age))
print("Coded before: " + str(coded_before))
print("Study hours: " + str(study_hours))

# 2) بالـ f-string
print(f"=== {name} ===")
print(f"City: {city}")
print(f"Major: {major}")
print(f"Age: {age}")
print(f"Coded before: {coded_before}")
print(f"Study hours: {study_hours}")

# 3) بأمر print واحد
print(f"=== {name} ===\nCity: {city}\nMajor: {major}\nAge: {age}\nCoded before: {coded_before}\nStudy hours: {study_hours}")

# 4) أنواع المتغيرات
print(type(name), type(city), type(major), type(age), type(coded_before), type(study_hours))

# 5) الأسهل في القراءة: f-string، لأنها ما تحتاج str() ولا علامات + كثيرة.