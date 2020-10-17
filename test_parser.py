from calc import calc
import unittest

class invalid_inputs(unittest.TestCase):
  def test_that_empty_string_raises_a_value_error(self):
    self.assertRaises(ValueError, calc, "")

  def test_that_input_containing_a_comma_raises_a_value_error(self):
    self.assertRaises(ValueError, calc, "3,14")

class single_number_inputs(unittest.TestCase):
  def test_that_a_single_digit_integer_returns_itself(self):
    self.assertEquals(calc("3"), "3")

  def test_that_a_multi_digit_integer_returns_itself(self):
    self.assertEquals(calc("12"), "12")

  def test_that_a_rational_number_returns_iteself(self):
    self.assertEquals(calc("3.14"), "3.14")

  def test_that_a_negative_single_digit_integer_returns_itself(self):
    self.assertEquals(calc("-1"), "-1")

  def test_that_a_negative_multi_digit_integer_returns_itself(self):
    self.assertEquals(calc("-34"), "-34")

  def test_that_a_negative_rational_number_returns_itself(self):
    self.assertEquals(calc("-2.72"), "-2.72")

class redundant_parenthesis(unittest.TestCase):
  def test_that_single_redudant_parenthesis_get_resolved(self):
    self.assertEquals(calc("(34)"), "34")

  def test_that_multiple_redudant_parenthesis_get_resolved(self):
    self.assertEquals(calc("(((34)))"), "34")

if __name__ == '__main__':
    unittest.main()