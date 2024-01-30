lst = ['volvo', 'bmw', 'benz', 'porsche', 'bently']

count = 0

for i in lst:
    print("{} -> {}".format(count, i))
    count+=1
    
    
for count, name in enumerate(lst):
    print("{} => {}".format(name, count))