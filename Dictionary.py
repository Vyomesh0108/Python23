import json

emp = {
    "id": 101,
    "name": "vyomesh",
    "age": 20
}

"""

print(emp, end=" ")

print("")

for key, value in emp.items():
    print(key, " : ",value)
    
for key, value in emp.items():
    print(value)
    
print(emp["name"])

if "name" in emp:
    print("Yes, we have name key")
else:
    print("No, we don't have name key")        
"""
std = {
    "s1": {"sid": 1, "sna": "vyomesh", "per": 75},
    "s2": {"sid": 2, "sna": "dhyeya", "per": 60},
    "s3": {"sid": 3, "sna": "darsh", "per": 90},
    "s4": {"sid": 4, "sna": "karan", "per": 80}
}

print(std, end="")
print(" ")
print(" ")

for key, value in std.items():
    print(key, ":", value)

print("")

for key, value in std.items():
    for k, v in value.items():
        print(k, ":", v)

    print("")

print("")
print("\n JSON Format: ")
print(json.dumps(std))