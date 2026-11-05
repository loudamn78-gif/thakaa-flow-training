# مثال على while
count = 3

while count > 0:
    print("Attempt", count)
    count -= 1

print("-" * 20)

# مثال على for
students = ["Noura", "Khalid", "Reem"]

for student in students:
    print(student)

print("-" * 20)

# مثال على print
name = "Kholoud"
print(name)

print("-" * 20)

# مثال على return
def square(num):
    return num * num

result = square(4)
print(result)

print("-" * 20)

# مثال يوضح ظهور None
def add(a, b):
    print(a + b)

x = add(2, 3)
print(x)