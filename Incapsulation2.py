class Test():
    def public_func(self):
        print("Public function called")

    def _protected_func(self):
        print("Protected function called")

    def __private_func(self):
        print("Private function called")

    def test_private(self):
        self.__private_func()

test = Test()
test.public_func()
test._protected_func()
test.test_private()