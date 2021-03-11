from abc import ABC, abstractmethod


class Apartment:
    def __init__(self, floor, elevator, *args, **kwargs):
        self.floor = floor
        self.elevator = elevator
        super().__init__(*args, **kwargs)


class House:
    def __init__(self, age, address, *args, **kwargs):
        self.age = age
        self.address = address
        super().__init__(*args, **kwargs)


class Rent(ABC):
    def __init__(self, fixed_amount, monthly_amount):
        self.fixed_amount = fixed_amount
        self.monthly_amount = monthly_amount

    @abstractmethod
    def show_banner(self):
        pass


class Sale(ABC):
    def __init__(self, fee):
        self.fee = fee

    @abstractmethod
    def show_banner(self):
        pass


class ApartmentRent(Apartment, Rent):

    def __str__(self):
        return f"{self.floor},{self.fixed_amount},{self.monthly_amount}"

    def show_banner(self):
        return "show banner"


class ApartmentSale(Apartment, Sale):
    def __str__(self):
        return f"{self.floor},{self.fee}"

    def show_banner(self):
        return "show banner"


class HouseRent(House, Rent):
    def __str__(self):
        return f"{self.address},{self.fixed_amount}"

    def show_banner(self):
        return "show banner"


class HouseSale(House, Sale):
    def show_banner(self):
        return "show banner"


if __name__ == "__main__":
    apartment_rent = ApartmentRent(floor=2, elevator=True, fixed_amount=120000000, monthly_amount=10000)
    apartment_sale = ApartmentSale(floor=2, elevator=True, fee=130000000)
    print(ApartmentRent.mro())
    print(apartment_sale)
    house_rent = HouseRent(age=20, address='shiraz fars', fixed_amount=12000000, monthly_amount=1000000)
    print(house_rent)

