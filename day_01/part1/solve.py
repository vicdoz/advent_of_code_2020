from builtins import int

with open('input') as f:
    items = f.read().splitlines()

for item in items:
    for item2 in items:
        if int(item) + int(item2) == 2020:
            result = int(item) * int(item2)
            break
print(result)
# result = 1013211