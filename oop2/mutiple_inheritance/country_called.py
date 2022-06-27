from country import Country

#create countries
#Thailand 13.7649136,100.5360959
#pop = 70,078,203
#areaa = 513,120
#temp = 32C

c1 = Country('Thailand',513120,70078203)
c1.setcordinate(13.7649136,100.5360959)
c1.setcelsius(32)
c1.showdetail()

#create 2 countries

c2 = Country('Japan',377975,125711253)
c2.setcordinate(36.2048,138.2529)
c2.setcelsius(34)
c2.showdetail()

c3 = Country('Singapore',7286,5941307)
c3.setcordinate(1.290270,103.851959)
c3.setcelsius(31)
c3.showdetail()
