class Account:
    def __init__(self) -> None:
        self.type = 'Saving'
        self.accno = ''
        self.balance = 0

    def open_account(self,name:str,type:str,accno,balance:int = 100):
        self.name = name
        self.type = type
        self.accno = accno
        self.balance = balance

    def display_balance(self):
        return f'{self.name} account balance = {self.balance} baht'
