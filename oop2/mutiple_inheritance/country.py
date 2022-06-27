from geographic import Geographic
from temperature import Temperature

class Country(Geographic,Temperature):
    def __init__(self,name,area,pop) -> None:
        self.name = name
        self.area = area
        self.population = pop

    def getpopulationdensity(self):
       return self.population / self.area

    def showdetail(self):
        #ชื่อประเทศ
        print(f'Country: {self.name}')

        #สถานที่ตั้ง 
        print(f'Location: {self.getcordinate()}')

        #แสดงขนาดพื้นที่ ประชากร ความหนาแน่น
        print(f'Population: {self.population:,d}')
        print(f'Area: {self.area:,.2f}')
        print(f'Density: {self.getpopulationdensity():,.2f}')

        #timezone climate temperture weather
        print(f'Time Zone: {self.gettimezone()}')
        print(f'Climate: {self.getclimate()}')
        print(f'Temperture(C): {self.getcelcisu():.2f}')
        print(f'Temperture(F): {self.getfahrenheit():.2f}')
        print(f'Weather: {self.getweather()}')

        print(f'**************************')
