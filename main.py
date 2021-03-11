from random import choice

from advertisment import ApartmentSell
from estate import Apartment, House, Store
from regoin import Region
from user import User

FIRST_NAME = ['reza', 'maryam', 'ali']
LAST_NAME = ['rezai', 'maryami', 'aliyari']
MOBILES = ['09876543211', '09876543213', '09876543214', '09876543218', '09876543216']
if __name__ == "__main__":
    for mobile in MOBILES:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)

    for user in User.object_list:
        print(f"{user.id} \t {user.full_name}")

    reg1 = Region(name='shiraz')
    apt1 = Apartment(user=User.object_list[0], area=80,
                     rooms_count=2, built_year=1393,
                     has_elevator=True, has_parking=True,
                     region=reg1, address="some where")
    apt1.show_description()

    house = House(has_yard=True, floor_count=1, user=User.object_list[2],
                  area=400, rooms_count=4, built_year=1370,
                  region=reg1, address="sm T")
    house.show_description()

    store = Store(User.object_list[-1], area=30, rooms_count=0,
                  built_year=1990, region=reg1, address="some Text")
    store.show_description()

    # Create Advertisement
    apartment_sell = ApartmentSell(user=User.object_list[0], area=80,
                                   rooms_count=2, built_year=1393,
                                   has_elevator=True, has_parking=True,
                                   region=reg1, address="some where", price_per_meter=10,
                                   discountable=True, convertible=False)

    apartment_sell.sho_detail()
