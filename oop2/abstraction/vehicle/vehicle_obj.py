from vehicle_subclass import *

#create car obj
c = Car("Mazda",220)
c.year = 2021
c.gear = 7
c.seat = 4
c.maintanance = 2022
c.show_detail()
c.show_maintanance()

#create truck obj
t = Truck("Isuzu",120)
t.capacity = 2
t.wheel = 8
t.show_detail()
t.show_price()

#create motocycle obj
m = Motocycle("Honda",100)
m.cc = 160
m.model = "NEW PCX"
m.show_detail()
