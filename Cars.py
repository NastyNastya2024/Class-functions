class Engine():
    def start (self):
        print("Engine.start")

    def stop (self):
        print("Engine.stop")

class Car():
    def __init__(self, name, engine):
        self.engine = Engine()

    def start(self):
        self.engine.start ()

    def stop(self):
        self.engine.stop ()


my_car = Car('Tesla', Engine())
my_car.start ()
my_car.stop ()

