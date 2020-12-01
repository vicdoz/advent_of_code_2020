from builtins import int

with open('input') as f:
    items = f.read().splitlines()


for item in items:
    for item2 in items:
        for item3 in items:
            if int(item) + int(item2) + int(item3) == 2020:
                result = int(item) * int(item2) * int(item3)
                break
    items.remove(item)
print(result)