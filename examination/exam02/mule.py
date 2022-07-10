from horse import Horse
from donkey import Donkey

class Mule(Horse,Donkey):
    def run(self):
        print(f'{self.name} is running')

    def show_info(self):
        print('***** Mumu Info *****')
        print(f'Name:{self.name}')
        print(f'Color:{self.color}')
        print(f'Max Height:{self.max_height}')
        print(f'Age:{self.age}')
        print(f'Weight:{self.weight}')

        print('***** Meme Info *****')
        Donkey.sound()
        print(f'Name:{self.name}')
        print(f'Color:{self.color}')
        print(f'Max Height:{self.max_height}')
        print(f'Age:{self.age}')
        print(f'Weight:{self.weight}')

        

        

