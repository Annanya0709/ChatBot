
class Calculation:

    def __init__(self, number):
        self.number = number
        self.num1 = number[0]
        self.num2 = number[1]
    
    def add(self, number):
        print(sum(number))
        return sum(number)
    
    def sub(self):
        print(abs(self.num1 - self.num2))

    def mul(self):
        print( self.num1*self.num2 )






