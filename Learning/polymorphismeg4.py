class vehicle:
    def start(self):
        print("The Vehicle is starting...")

class car(vehicle):
    def start(self):
        super().start()
        print("The Car is starting...")

vw=car()
vw.start()