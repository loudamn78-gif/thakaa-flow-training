profile = {
    "name": "Kholoud",
    "city": "Riyadh",
    "age": 29,
    "skills": ["Python", "NLP", "Data Analysis"],
    "courses": {
        "Python": "in progress",
        "Data Structures": "in progress"
    }
}

# اضفت مهارة جديدة
profile["skills"].append("Git")

# حدثت حالة كورس واضفت كورس جاي
profile["courses"]["Python"] = "done"
profile["courses"]["Machine Learning"] = "planned"

# اضفت github وحذفت city
profile["github"] = "loudamn78"
del profile["city"]

print(list(profile.keys()))
print(len(profile["skills"]))
print("SQL" in profile["skills"])
print("Python" in profile["courses"])
print(profile["courses"].get("Java", "not found"))

print(f"{profile['name']} · {len(profile['skills'])} skills · {len(profile['courses'])} courses · github.com/{profile['github']}")