from oops1 import User
# user = User()
# user.register()
# user.login()
user1 = User("Athi", "passsssswrd")
user2 = User("name2", "23322wewwfef")

user1.register()
user2.login()
print(user1.username)
print(User.noOfUsers)
print(user2.username)
print(user1.password)
print(User.noOfUsers)