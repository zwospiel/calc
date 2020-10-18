from calc import calc
import unittest

class invalid_inputs(unittest.TestCase):
  def test_that_non_string_inputs_raise_type_errors(self):
    for input in [True, 0, -1, 1.2]:
      self.assertRaises(TypeError, calc, input)

  def test_that_empty_strings_raise_value_errors(self):
    self.assertRaises(ValueError, calc, "")

  def test_that_commas_raise_value_errors(self):
    self.assertRaises(ValueError, calc, "3,14")

  def test_that_incorrect_parenthesis_raise_value_errors(self):
    incorrect_parenthesis = [
      "(", ")", "())", "(()",
      "(3+4", "3+4)", "(3+4))", "((3+4)",
      "3(+)4", "(3+)4", "(3+)4"
    ]

    for input in incorrect_parenthesis:
      self.assertRaises(ValueError, calc, input)

class single_number_inputs(unittest.TestCase):
  def test_that_single_digit_integers_return_themselves(self):
    self.assertEquals(calc("3"), "3")

  def test_that_multi_digit_integers_return_themselves(self):
    self.assertEquals(calc("12"), "12")

  def test_that_rational_numbers_return_themselves(self):
    self.assertEquals(calc("3.14"), "3.14")

  def test_that_negative_numbers_return_themselves(self):
    self.assertEquals(calc("-1"), "-1")
    self.assertEquals(calc("-34"), "-34")
    self.assertEquals(calc("-2.72"), "-2.72")

class redundant_parenthesis(unittest.TestCase):
  def test_that_single_redudant_parenthesis_get_resolved(self):
    self.assertEquals(calc("(34)"), "34")

  def test_that_multiple_redudant_parenthesis_get_resolved(self):
    self.assertEquals(calc("(((34)))"), "34")

if __name__ == '__main__':
    unittest.main()