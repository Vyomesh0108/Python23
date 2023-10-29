s1 = {10, 20, 30, "svit", "bit", "ntc", 50, 20, 500, 44, 10, 20, 33, 20}

for x in s1:
    print(x, end=" ")

s1.discard(20)
s1.add(1000)

print("")

for x in s1:
    print(x, end=" ")

print("")
# Union
print("")
DaysA = set(["Mon", "Tue", "Wed"])
DaysB = set(["Wed", "Thu", "Fri", "Sat", "Sun"])
AllDays = DaysA|DaysB
print(AllDays)

print("")
# Intersection
print("")
DaysA = set(["Mon", "Tue", "Wed"])
DaysB = set(["Wed", "Thu", "Fri", "Sat", "Sun"])
AllDays = DaysA & DaysB
print(AllDays)

print("")
# Difference
print("")
DaysA = set(["Mon", "Tue", "Wed"])
DaysB = set(["Wed", "Thu", "Fri", "Sat", "Sun"])
AllDays = DaysA - DaysB
print(AllDays)

print("")
# Subset & Superset
print("")
DaysA = set(["Mon", "Tue", "Wed"])
DaysB = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
SubsetRes = DaysA <= DaysB
SupersetRes = DaysA >= DaysB
print(SubsetRes)
print(SupersetRes)
