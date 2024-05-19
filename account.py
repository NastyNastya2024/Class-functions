class User:
    def __init__(self, user_id, name, access_level='user'):
        self._user_id = user_id
        self._name = name
        self._access_level = access_level

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')
        self._users_list = []

    def add_user(self, user):
        self._users_list.append(user)

    def remove_user(self, user):
        self._users_list.remove(user)

# Пример использования
user1 = User(1, 'Alice')
user2 = User(2, 'Bob')
admin = Admin(101, 'Admin')

print(f"User ID: {user1.get_user_id()}, Name: {user1.get_name()}, Access Level: {user1.get_access_level()}")
print(f"User ID: {user2.get_user_id()}, Name: {user2.get_name()}, Access Level: {user2.get_access_level()}")

admin.add_user(user1)
admin.add_user(user2)

for user in admin._users_list:
    print(f"Admin's users: User ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")