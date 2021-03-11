from estate import Apartment, House, Store
from deal import Sell, Rent


class ApartmentSell(Apartment, Sell):

    def sho_detail(self):
        self.show_description()
        self.show_price()


class ApartmentRent(Apartment, Sell):
    pass


class HouseSell(House, Sell):
    pass


class HouseRent(House, Sell):
    pass


class StoreSell(Store, Sell):
    pass


class StoreRent(Store, Sell):
    pass
