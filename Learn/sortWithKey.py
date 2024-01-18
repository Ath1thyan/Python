items = [(3456, "shoe", 75), (3566, "dress", 89), (2878, "laptop", 63), (2689, "mac", 56)]
print(items)
items.sort()
print(items)
items.sort(key = lambda i : i[1])
print(items)
items.sort(key = lambda i : i[1], reverse=True)
print(items)
items.sort(key = lambda i : i[2])
print(items)

print("--------     -----------  ----------  ----------  ---------   ---------   -----------")

items1 = ((3456, "shoe", 75), (3566, "dress", 89), (2878, "laptop", 63), (2689, "mac", 56))
print(items1)
print(sorted(items1))
print(sorted(items1, key = lambda i : i[1]))

print("--------     -----------  ----------  ----------  ---------   ---------   -----------")

items2 = [(3456, "shoe", 750), (3566, "dress", 890), (2878, "laptop", 630), (2689, "mac", 560)]
print(items2)
# inr_usd = lambda i : (i[0], i[1], i[2]/80)
inr_usd = lambda i : (i[0], i[1], float("{:.2f}".format(i[2]/80)))
items2_usd = list(map(inr_usd, items2))
print(items2_usd)

print("--------     -----------  ----------  ----------  ---------   ---------   -----------")

val = [4,8,5,6,2]
val_sq = list(map(lambda num : num*num, val))
print(val_sq)

print("--------     -----------  ----------  ----------  ---------   ---------   -----------")

def sq(num):
    return num*num
val_sq1 = list(map(sq, val))
print(val_sq1)
