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

print("--------     -----------  ----------  ----------  ---------   ---------   -----------")

items3 = [(3456, "shoe", 350), (3566, "mobile", 890), (2878, "laptop", 430), (2689, "mac", 560)]
lessthan_500 = lambda item : item[2]<500
filtered = list(filter(lessthan_500, items3))
print(filtered)
filtered = list(filter(lambda item : item[1][0] =='m', items3))
print(filtered)


import functools
value = [5,4.5,89,9,6,4]
sum = functools.reduce(lambda x,y : x+y, value)
print(sum)

char = ['a','t','h','i']
name = functools.reduce(lambda x,y : x+y, char)
print(name)

temp = [54, 78, 45, 89, 75, 25, 93, 68]
temp_less_50 = [i for i in temp if i<50]
print(temp_less_50)

temp1 = [54, 78, 45, 89, 75, 25, 93, 68]
temp_less = [i if i<50 else 0 for i in temp]
print(temp_less)

print("--------     -----------  ----------  ----------  ---------   ---------   -----------")

cart = {"phone":25000.00 , "lamp":750.95 , "table":2500.63 , "pen":120.00 , "kettle":1000.35}
cart_rounded = {k : round(values) for (k,values) in cart.items()}
print(cart_rounded)

print("--------     -----------  ----------  ----------  ---------   ---------   -----------")

car = ['volvo' , 'bmw', 'benz', 'porsche']
model = ['xc90', 'x7', 'amg', 'cayenne']
zipped_list = list(zip(car,model))
print(zipped_list)
zipped_tuple = tuple(zip(car,model))
print(zipped_tuple)
zipped_set = set(zip(car,model))
print(zipped_set)