class User():
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._level = "user"

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def set_level(self):
       return self._level

    def set_name(self, name):
        self._name = name

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._level = "admin"

    def add_user(self, user_list,user):
        user_list.append(user)
        print("Admin user added")

    def remove_user(self, user_list):
        user_list.remove(user)


users =[]
user1 = User(1, "user1")
admin1 = Admin(1, "admin1")

print(user1.get_user_id())
admin1.add_user(users,admin1)



