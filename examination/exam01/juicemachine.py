class JuiceOrder:
    def __init__(self,menu:str,size:str,price:int) -> None:
        self.menu = menu
        self.size = size
        self.price = price

    def check_menu(self):
        menu_dictionary = {
            'OJ':25,
            'AJ':25,
            'WJ':30,
            'PJ':30
            }
        if self.menu in menu_dictionary:
            self.price = menu_dictionary.get(self.menu)

    def compute_price(self):
        if self.size == 'R':
            self.price += 0
        elif self.size == 'L':
            self.price += 5
        else:
            self.price

        JuiceOrder.total = self.price

    def display_order(self):
        ('รายการที่ 1 ซื้อน้ำแตงโม แก้วใหญ่')
        ('รายการที่ 2 ซื้อน้ำส้ม แก้วปกติ')
        ('รายการที่ 3 ซื้อน้ำสัปปะรด แก้วใหญ่')

    def display_detail(self):
     self.check_menu()
     self.compute_price()
     return f'{self.menu}({self.size} * {self.price}) => {JuiceOrder.total} baht'
       


if __name__ == "__main__":
    order1 = JuiceOrder('wj','L',30)
    order2 = JuiceOrder('oj','R',25)
    order3 = JuiceOrder('pj','L',30)
    
    print(order1.display_detail())
    print(order2.display_detail())
    print(order3.display_detail())

