'''Fraction Calculator'''

class Fraction:
    def __init__(self, num: float, denom: float) -> None:
        self.num: float = num
        if denom != 0 :
            self.denom: float = denom
        else: 
            # raise ZeroDivisionError
            raise ValueError("Denominator cannot be zero!")
        # self.denom: float = denom
    
    def plus(self, other: "Fraction") -> "Fraction":
        '''calculating adding of two fractions given by user'''
        x: float = (self.num*other.denom) + (other.num*self.denom)
        y: float = self.denom*other.denom
        return Fraction(x,y)
  
    def minus(self, other: "Fraction") -> "Fraction":
        '''calculating substraction of two fractions given by user'''
        x: float = (self.num*other.denom) - (other.num*self.denom)
        y: float = self.denom*other.denom
        return Fraction(x,y)

    def times(self, other: "Fraction") -> "Fraction":
        '''calculating multiplication of two fractions given by user'''
        x: float = self.num*other.num
        y: float = self.denom*other.denom
        return Fraction(x,y)
    
    def divide(self, other: "Fraction") -> "Fraction":
        '''calculating divident of two fractions given by user'''
        x: float = self.num*other.denom
        y: float = self.denom*other.num
        # return set.times(Fraction(other.denom, other.num))
        return Fraction(x,y)
        
    def equal(self, other: "Fraction") -> bool:
        '''comparing two fractions if they are equal or not'''
        frac1: float = self.num/self.denom
        frac2: float = other.num/other.denom
        if(frac1 == frac2):
            return True
        else:
            return False
    
    def __str__(self) -> str:
        return f'{self.num}/{self.denom}'


def main() -> None:

    '''Taking valid input from user for the Fraction Calculator'''
    
    print('This is a Fraction Calculator')

    while True:
        a: str = input("Give us Numerator 1: ")
        try:
            a: float = float(a)
            break
        except ValueError:
            print(f"Error: {a} is not a vaild number. Please try again.")
    
    while True:
        b: str = input("Give us Denominator 1: ")
        try:
            b: float = float(b)
            break
        except ValueError:
            print(f"Error: {b} is not a vaild number. Please try again.")

    fraction_1 = Fraction(a, b)

    while True:
        c: str = input("Give us the operator (+, -, /, *, ==): ")
        if c in ["+", "-", "/", "*", "=="]:
            break
        else:
            print(f"Error: {c} is not a vaild operator. Please try again.")
    
    while True:
        d: str = input("Give us Numerator 2: ")
        try:
            d: float = float(d)
            break
        except ValueError:
            print(f"Error: {d} is not a vaild number. Please try again.")
    
    while True:
        e: str = input("Give us Denominator 2: ")
        try:
            e: float = float(e)
            break
        except ValueError:
            print(f"Error: {e} is not a vaild number. Please try again.")
    
    fraction_2 = Fraction(d, e)

    try:
        fraction_1.plus(fraction_2)
    except ZeroDivisionError as e:
        print(e)


    if(c == '+'):
        print(f"{fraction_1} + {fraction_2} = {fraction_1.plus(fraction_2)}")
    elif (c == '-'):
        print(f"{fraction_1} - {fraction_2} = {fraction_1.minus(fraction_2)}")
    elif (c == '*'):
        print(f"{fraction_1} * {fraction_2} = {fraction_1.times(fraction_2)}")
    elif (c == '/'):
        print(f"{fraction_1} / {fraction_2} = {fraction_1.divide(fraction_2)}")
    elif (c == '=='):
        print(f"{fraction_1} == {fraction_2} = {fraction_1.equal(fraction_2)}")


def test_suite() -> None:
    f12: Fraction = Fraction(1, 2)
    f44: Fraction = Fraction(4, 4)
    f128: Fraction = Fraction(12, 8)
    f32: Fraction = Fraction(3, 2)

    print("****************** here is the output for test cases ******************")
    print(f"{f12} + {f12} = {f12.plus(f12)} [4/4]")
    print(f"{f44} - {f12} = {f44.minus(f12)} [4/8]")
    print(f"{f12} - {f44} = {f44.plus(f12)} [12/8]")
    print(f"{f12} * {f44} = {f44.times(f12)} [4/8]")
    print(f"{f12} / {f44} = {f44.divide(f12)} [8/4]")
    print(f"{f128} == {f32} = {f128.equal(f32)} [True]")
    print(f"{f12} + {f44} + {f32} = {f12.plus(f44).plus(f32)} [48/16]")
    print(f"{f12} + {f44} - {f32} = {f12.plus(f44).minus(f32)} [0/16]")

    
if __name__ == "__main__":
    main()
    test_suite()