'''Fraction Calculator'''

class Fraction:
    '''Fraction Calculator'''
    
    def __init__(self, num: float, denom: float) -> None:
        self.num: float = num
        if denom != 0 :
            self.denom: float = denom
        else: 
            # raise ZeroDivisionError
            raise ValueError("Denominator cannot be zero!")
        # self.denom: float = denom
    
    def __add__(self, other: "Fraction") -> "Fraction":
        '''calculating adding of two fractions given by user'''
        x: float = (self.num*other.denom) + (other.num*self.denom)
        y: float = self.denom*other.denom
        return Fraction(x,y)
  
    def __sub__(self, other: "Fraction") -> "Fraction":
        '''calculating substraction of two fractions given by user'''
        x: float = (self.num*other.denom) - (other.num*self.denom)
        y: float = self.denom*other.denom
        return Fraction(x,y)

    def __mul__(self, other: "Fraction") -> "Fraction":
        '''calculating multiplication of two fractions given by user'''
        x: float = self.num*other.num
        y: float = self.denom*other.denom
        return Fraction(x,y)
    
    def __truediv__(self, other: "Fraction") -> "Fraction":
        '''calculating divident of two fractions given by user'''
        x: float = self.num*other.denom
        y: float = self.denom*other.num
        # return set.times(Fraction(other.denom, other.num))
        return Fraction(x,y)
        
    def __eq__(self, other: "Fraction") -> bool:
        '''comparing two fractions if they are equal or not'''
        frac1: float = self.num/other.num
        frac2: float = self.denom/other.denom
        if(frac1 == frac2):
            return True
        else:
            return False
    
    def __ne__(self, other: "Fraction") -> bool:
        '''comparing two fractions if they are equal or not'''
        frac1: float = self.num/other.num
        frac2: float = self.denom/other.denom
        if frac1 != frac2:
            return True
        else:
            return False
            
    def __lt__(self, other: "Fraction") -> bool:
        '''checking if first fraction is less than second fraction'''
        frac1: float = self.num/other.num
        frac2: float = self.denom/other.denom
        if frac1 < frac2:
            return True
        else:
            return False 

    def __le__(self, other: "Fraction") -> bool:
        '''checking if first fraction is less than or equal to second fraction'''
        frac1: float = self.num/other.num
        frac2: float = self.denom/other.denom
        if frac1 <= frac2:
            return True
        else:
            return False
    
    def __gt__(self, other: "Fraction") -> bool:
        '''checking if first fraction is greater than second fraction'''
        frac1: float = self.num/other.num
        frac2: float = self.denom/other.denom
        if frac1 > frac2:
            return True
        else:
            return False
     
    def __ge__(self, other: "Fraction") -> bool:
        '''checking if first fraction is greater than or equal to second fraction'''
        frac1: float = self.num/other.num
        frac2: float = self.denom/other.denom
        if frac1 >= frac2:
            return True
        else:
            return False

    def simplify(self) -> "Fraction":
        '''simplifying fraction to the lowest fraction'''
        min_num: float = 1.0
        for i in range(2, min(abs(self.num),abs(self.denom))+1):
            if self.num % i == 0 and self.denom % i == 0:
                min_num: float = i
        
        if min_num == 1.0:
            return Fraction(self.num, self.denom)
        else:
            return Fraction(self.num/min_num, self.denom/min_num)
    
    def __str__(self) -> str:
        if self.num != 0 and self.denom > 0:
            return f'{float(self.num)}/{float(self.denom)}'
        else:
            return f'{float(-self.num)}/{float(-self.denom)}'

# def test():
    # q = Fraction(40,20).simplify()
    # q = Fraction(50,23).simplify()
    # print(q)
    # w = Fraction(-2,1)
    # print(w)
    # if q == w:
    #     print('done')
    # else:
    #     print('not done')

    # z = Fraction(40,20).__truediv__(Fraction(0,20))
    # print(z)

if __name__ == '__main__':
    # test()
    "run main function"