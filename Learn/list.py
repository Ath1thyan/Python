print ("Hello World")
l = ["apple", "banana", "banana", True, "apple", 0, 7, bool, [1,2,3], int, "banana", "banana", {"key" : "value"}, "a " + "b"]
l2 = ["items", "from", "list2"]
t = ("kiwi", "melon")
s = {"set", "elements"}
d = {"dict" : "value"}
print (type(l))
print (len(l))
print (l)
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(l[2:6])
if True in l:
    print ("if statement executed, True is present inside thr list \"l\"")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
l[-4] = "Blackcurrent"
print (l)
print("---------------------------------------------------------------------------------------------------------------------------------------------")
l[1:3] = ["blackcurrant", "watermelon"]
print (l)
print("---------------------------------------------------------------------------------------------------------------------------------------------")
l.insert(2, "banana")
print(l)
print("---------------------------------------------------------------------------------------------------------------------------------------------")
l.append("orange")
print(l)
print("---------------------------------------------------------------------------------------------------------------------------------------------")
l.extend(l2)
print(l)
print("---------------------------------------------------------------------------------------------------------------------------------------------")
l.extend(t)
print(l)
print("---------------------------------------------------------------------------------------------------------------------------------------------")
l.extend(s)
print(l)
print("---------------------------------------------------------------------------------------------------------------------------------------------")
l.extend(d)
print(l)
print("---------------------------------------------------------------------------------------------------------------------------------------------")
l.remove("banana")
print(l)
print("---------------------------------------------------------------------------------------------------------------------------------------------")
l.pop(1)
print(l)
print("---------------------------------------------------------------------------------------------------------------------------------------------")
l.pop()
print(l)
print("---------------------------------------------------------------------------------------------------------------------------------------------")
del l[0]
print(l)
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print("for loop")
print("=== ====")
for x in l:
    print(x)
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print ("for - range \t")
print("===   =====")
for i in range(len(l)):
    print(l[i])
print("---------------------------------------------------------------------------------------------------------------------------------------------")
#del l
#print(l)
#l.clear()
#print(l)
#print("---------------------------------------------------------------------------------------------------------------------------------------------")
c = 0
while c < len(l):
    print(l[c])
    c = c + 1
print("---------------------------------------------------------------------------------------------------------------------------------------------")
[print(x) for x in l]
print("---------------------------------------------------------------------------------------------------------------------------------------------")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)
print("---------------------------------------------------------------------------------------------------------------------------------------------")
l3 = [x for x in fruits if "a" in x]
print (l3)
print("---------------------------------------------------------------------------------------------------------------------------------------------")
newlist = [x for x in fruits if x != "apple"]
print (newlist)
print("---------------------------------------------------------------------------------------------------------------------------------------------")
newlist = [x for x in range(10)]
print (newlist)
print("---------------------------------------------------------------------------------------------------------------------------------------------")
list1 = [x for x in range(10) if x < 5]
print (list1)
print("---------------------------------------------------------------------------------------------------------------------------------------------")
newlist = [x.upper() for x in fruits]
print(newlist)
print("---------------------------------------------------------------------------------------------------------------------------------------------")
newlist = ['hello' for x in fruits]
print(newlist)
print("---------------------------------------------------------------------------------------------------------------------------------------------")
nl = [x if x != "banana" else "orange" for x in l]
print (nl)
print("---------------------------------------------------------------------------------------------------------------------------------------------")
fruits.sort()
print (fruits)
print("---------------------------------------------------------------------------------------------------------------------------------------------")
fruits.sort(reverse=True)
print(fruits)
print("---------------------------------------------------------------------------------------------------------------------------------------------")
