

class Swift:
    def start(self):
        print("swifyt car starts")

    def accelerate(self):
        print("swift accelerate")

    def stop(self):
        print("swift stop")


class Creta:
    def start(self):
        print("creta car starts")

    def accelerate(self):
        print("ctra accelerate")

    def stop(self):
        print("creta stop")



class Perspon:
    def drive(self,car):
        car.start()
        car.accelerate()
        car.stop()

sw=Creta()
p=Perspon()
p.drive(sw)