#import build_car
#car = build_car.custom('toyota', 'rav4', color='silver', tow_package=True)
#print(car)

# from build_car import custom
# car = custom('toyota', 'rav4', color='silver', tow_package=True)
# print(car)

# from build_car import custom as c
# car = c('toyota', 'rav4', color='silver', tow_package=True)
# print(car)

# import build_car as bc
# car = bc.custom('toyota', 'rav4', color='silver', tow_package=True)
# print(car)

from build_car import *
car = custom('toyota', 'rav4', color='silver', tow_package=True)
print(car)