class User:
    # user_name = None
    # pwd = None
    noOfUsers = 0

    def __init__(self, uname, pwd):
        self.username = uname
        self.password = pwd
        User.noOfUsers +=1

    def register(self):
        print("registering..." + self.username)

    def login(self):
        print("logging in..." + self.username)
     