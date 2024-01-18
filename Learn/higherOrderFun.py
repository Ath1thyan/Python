def hello():
    print("Hello World")
    
def hi():
    print("Hi World")
    
print(hello)

fun = hello
fun()

print(fun)

def func(funct):
    funct()
    
func(hi)

add = lambda x:x+10
print(add(5))

num = lambda n : "yes" if n>20 else "no"
print(num(10))