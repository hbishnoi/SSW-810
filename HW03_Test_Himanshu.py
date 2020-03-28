''' testing everything for fraction calculator '''

import unittest
from HW03_Himanshu import Fraction

class TestFraction(unittest.TestCase):
    """ test class Fraction """

    def test_init(self) -> None:
        """ verify that the numerator and denominator are set properly """
        f: Fraction = Fraction(3, 4)
        # f1: Fraction = Fraction('e', 'w')
        self.assertEqual(f.num, 3)
        # self.assertNotEqual(f1.num, 3)
        self.assertEqual(f.denom, 4)
        # self.assertNotEqual(f1.denom, 4)

    def test_init_exception(self) -> None:
        """ verify that ZeroDivisionError is raised when appropriate """
        # f34: Fraction = Fraction(3, 4)
        with self.assertRaises(ValueError):
            Fraction(1,0)
            Fraction(0,0)
            Fraction(0,2)
        
        with self.assertRaises(ValueError):
            Fraction(1,2) / Fraction (0,2)

    def test_add(self) -> None:
        """ verify Fraction addition """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(f12 + f34, Fraction(10, 8))
        self.assertEqual(f12, Fraction(1, 2)) # f12 should not have changed
    
    def test_minus(self) -> None:
        """ verify Fraction substraction """
        f12: Fraction = Fraction(1, 2)
        f14: Fraction = Fraction(1, 4)
        self.assertEqual(f12 - f14, Fraction(2, 8))
        self.assertEqual(f12, Fraction(1, 2)) # f12 should not have changed
        
    def test_times(self) -> None:
        """ verify Fraction multiplication """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(f12 * f34, Fraction(3, 8))
        self.assertEqual(f12, Fraction(1, 2)) # f12 should not have changed
        
    def test_divide(self) -> None:
        """ verify Fraction divident"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f04: Fraction = Fraction(0, 4)
        self.assertEqual(f12 / f34, Fraction(4, 6))
        self.assertNotEqual(f12 / f34, Fraction(4, 8))
        self.assertEqual(f12, Fraction(1, 2)) # f12 should not have changed
        # self.assertEqual(f12 / f04)
        with self.assertRaises(ValueError):
            Fraction.__truediv__(f12, f04)

    def test_equal(self) -> None:
        """ verify Fraction are equal"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertTrue(f12 == f12)
        self.assertFalse(f12 == f34)
        self.assertEqual(f12, Fraction(1, 2)) # f12 should not have changed

    def test_ne(self) -> None:
        """ verify Fraction are not equal to"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertTrue(f12 != f34)
        self.assertFalse(f12 != f12)
        self.assertTrue(f12 - f34 != f34)
        self.assertEqual(f12, Fraction(1, 2)) # f12 should not have changed

    def test_lt(self) -> None:
        """ verify first Fraction is less than second fraction"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f13: Fraction = Fraction(-1, 3)
        f31: Fraction = Fraction(1, -3)
        f23: Fraction = Fraction(2, 3)
        self.assertTrue(f12 < f34)
        self.assertFalse(f34 < f12)
        self.assertTrue(f13 < f23)
        self.assertFalse(f13 > f23)
        self.assertFalse(f31 < f23)
        self.assertTrue(f12 - f34 < f34)
        self.assertEqual(f12, Fraction(1, 2)) # f12 should not have changed

    def test_le(self) -> None:
        """ verify first Fraction is less than or equal to second fraction"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertTrue(f12 <= f34)
        self.assertTrue(f12 <= f12)
        self.assertFalse(f34 <= f12)
        self.assertEqual(f12, Fraction(1, 2)) # f12 should not have changed

    def test_gt(self) -> None:
        """ verify first Fraction is greater than second fraction"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertFalse(f12 > f34)
        self.assertTrue(f34 > f12)
        self.assertEqual(f12, Fraction(1, 2)) # f12 should not have changed

    def test_ge(self) -> None:
        """ verify first Fraction is greater than or equal to second fraction"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertFalse(f12 >= f34)
        self.assertTrue(f12 >= f12)
        self.assertTrue(f34 >= f12)
        self.assertEqual(f12, Fraction(1, 2)) # f12 should not have changed

    def test_3_operands(self) -> None:
        """ verify expressions with more than two operands """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f44: Fraction = Fraction(4, 4)
        self.assertTrue(f12 + f34 + f44 == Fraction(72, 32))

    def test_str(self) -> None:
        """ checking if it gives the right fraction """
        f12: Fraction = Fraction(-1, 2)
        f21: Fraction = Fraction(1, -2)
        f: Fraction = Fraction(-1, -2)
        # f34: Fraction = Fraction(3, 4)
        self.assertNotEqual(str(f12), "3.0/4.0")
        self.assertEqual(str(f12), "-1.0/2.0")
        self.assertTrue(str(f12) == "-1.0/2.0")
        self.assertFalse(str(f12) == "1.0/4.0")
        self.assertEqual(str(f12), "-1.0/2.0")
        self.assertEqual(str(f21), "-1.0/2.0")
        self.assertEqual(str(f), "1.0/2.0")

    def test_simplify(self):
        '''testing simplifying method'''

        '''can simplify the fraction'''
        str1: str = str(Fraction(20,10).simplify())
        str2: str = str(Fraction(2,1))
        self.assertEqual(str1,str2) # checking when both num and denom are positive
    
        str1: str = str(Fraction(-20,10).simplify())
        str2: str = str(Fraction(-2,1))
        self.assertEqual(str1,str2) # checking when num is negative

        str1: str = str(Fraction(20,-10).simplify())
        str2: str = str(Fraction(-2,1))
        self.assertEqual(str1,str2) # checking when denom is negative

        str1: str = str(Fraction(-20,-10).simplify())
        str2: str = str(Fraction(2,1))
        self.assertEqual(str1,str2) # checking when both num and denom are negative

        '''can't simplify the fraction'''
        str1: str = str(Fraction(12,5).simplify())
        str2: str = str(Fraction(12,5))
        self.assertEqual(str1,str2) # checking when both num and denom are poistive

        str1: str = str(Fraction(-12,5).simplify())
        str2: str = str(Fraction(-12,5))
        self.assertEqual(str1,str2) # checking when num is negative

        str1: str = str(Fraction(12,-5).simplify())
        str2: str = str(Fraction(-12,5))
        self.assertEqual(str1,str2) # checking when denom is negative

        str1: str = str(Fraction(-12,-5).simplify())
        str2: str = str(Fraction(12,5))
        self.assertEqual(str1,str2) # checking when both num and denom are negative

        '''some more tests'''
        fraction1: Fraction = Fraction(11, 1331)
        fraction2: Fraction = Fraction(13, 169)
        fraction3: Fraction = Fraction(1, 13)
        fraction4: Fraction = Fraction(-2, 38)
        self.assertNotEqual(fraction1.simplify(), Fraction(1, 3))
        self.assertEqual(str(fraction1.simplify()), "1.0/121.0")
        self.assertTrue(fraction2.simplify() == fraction3)
        self.assertFalse(fraction3 == Fraction(1, 2))
        self.assertTrue(fraction1 == Fraction(-1, -121))
        self.assertTrue(fraction4 == Fraction(1, -19))

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)