
items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

print("Shopping List Report")
print("--------------------")

number = 1
for item in items:
    print(f"{number}. {item}")
    number += 1

long_names = 0
for item in items:
    if len(item) > 4:
        long_names += 1

print("Items with more than 4 letters:", long_names)

longest = items[0]
for item in items:
    if len(item) > len(longest):
        longest = item

print("Longest item name:", longest)
