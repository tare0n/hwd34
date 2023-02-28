class Vehicle:

    def __init__(self, position: tuple):
        self.position = position

    def travel(self, destination):
        route = self.calculate_route(source=self.position, to=destination)
        self.move_along(route)

    @staticmethod
    def calculate_route(source, to):
        return 0  # to be realized

    def move_along(self, route):
        print("moving")


class RadioMixIn:

    @staticmethod
    def turn_on_radio(radio_name):
        print(f"playing {radio_name}")


class Car(RadioMixIn, Vehicle):
    pass


class Airplane(Vehicle):
    pass
