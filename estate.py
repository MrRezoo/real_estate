from abc import abstractmethod
from base import BaseClass


class EstateAbstract(BaseClass):
    def __init__(self, user, area, rooms_count, built_year, region, address, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.area = area
        self.rooms_count = rooms_count
        self.built_year = built_year
        self.region = region
        self.address = address

    @abstractmethod
    def show_description(self):
        pass


class Apartment(EstateAbstract):
    def __init__(self, has_elevator, has_parking, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.has_elevator = has_elevator
        self.has_parking = has_parking

    def show_description(self):
        print(f"Apartment {self.id}\t area:{self.area}")


class House(EstateAbstract):
    def __init__(self, has_yard, floor_count, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.has_yard = has_yard
        self.floor_count = floor_count

    def show_description(self):
        print(f"House {self.id}")


class Store(EstateAbstract):

    def show_description(self):
        print(f"store {self.id}")
