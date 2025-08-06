import csv

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {}
    for row in reader:
        favorite = row["language"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1


for favorite in counts:
    print(f"{favorite}: {counts[favorite]}")

print("Sorted Alphabetically")

for favorite in sorted(counts):
    print(f"{favorite}: {counts[favorite]}")

print("to sort the keys based on their corresponding values reverse=True sorts the keys in descending order")

for favorite in sorted(counts, key=counts.get, reverse=True):
    print(f"{favorite}: {counts[favorite]}")



#    Simple way to do the things 
#     scratch, c, python = 0, 0, 0
#     for row in reader:
#         favorite = row["language"]
#         if favorite == "Scratch":
#             scratch += 1
#         elif favorite == "C":
#             c +=1
#         elif favorite == "Python":
#             python +=1


# advanced way to do the things 


# print(f"Scratch: {scratch}")
# print(f"C: {c}")
# print(f"Python: {python}")