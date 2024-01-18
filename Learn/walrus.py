# name = "Athi"
# print(name)

print(name := "Athi")



# print("enter list of nums. Enter 'z' to quit")
# num_list = []

# while True:
#     inp = input()
#     if inp == 'z':
#         break
#     num_list.append(int(inp))
# print(num_list)

print("enter list of nums. Enter 'z' to quit")
num_list = list()
while (inp := input()) != 'z':
    num_list.append(int(inp))
print(num_list)

