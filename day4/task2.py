tasks = ["Update website", "Client meeting", "Code review"]

tasks.append("Write report")
tasks.insert(0, "Fix urgent bug")
print(tasks)

# الاجتماع انتهى
tasks.remove("Client meeting")
print(tasks)

tasks.append("Review Sara's code")
removed = tasks.pop()
print(removed)

print(len(tasks))
print(tasks[0], tasks[-1])
print(tasks.index("Code review") + 1)

new_list = sorted(tasks)
print(new_list)
print(tasks)

# جربت sorted ولاحظت أنها تعطي قائمة جديدة مرتبة
# أما sort فترتب القائمة الأصلية نفسها
tasks.sort()
print(tasks)