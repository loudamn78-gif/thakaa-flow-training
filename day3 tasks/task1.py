email = " Sara.Ahmed@TFCO.SA "
clean = email.strip()
print(clean.lower())
print(email.count("a"), clean.lower().count("a"))
print("tfco" in email, "tfco" in clean.lower())
print(clean.startswith("sara"))
print(len(email), len(clean))
print(clean[:4], clean[-2:])
