class Money:
    def __init__(self,value,type):
        self.__amount = value
        self.__currency = type

    @property
    def amount(self):
        return self.__amount
    
    @property
    def currency(self):
        return self.__currency

    def __add__(self,other):
        if self.__currency == other.__currency:
            return Money(self.__amount+other.__amount,self.__currency)
        else:
            raise RuntimeError("Mimatched currencies")

    def __sub__(self,other):
        if self.__currency == other.__currency:
            return Money(self.__amount-other.__amount,self.__currency)
        else:
            raise RuntimeError("Mimatched currencies")
        
    def __mul__(self, num):
        return Money(self.__amount*num,self.__currency)