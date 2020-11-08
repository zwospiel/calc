import unittest
from calculator import parse

def call_parse(formula):
    return parse(formula)


class invalid_inputs(unittest.TestCase):
    def test_that_non_string_inputs_raise_type_errors(self):
        for input in [True, 0, -1, 1.2]:
            self.assertRaises(TypeError, call_parse, input)

    def test_that_empty_strings_raise_value_errors(self):
        self.assertRaises(ValueError, call_parse, "")

    def test_that_commas_raise_value_errors(self):
        self.assertRaises(ValueError, call_parse, "3,14")

    def test_that_incorrect_parenthesis_raise_value_errors(self):
        self.assertRaises(ValueError, call_parse, "(")
        self.assertRaises(ValueError, call_parse, ")")
        self.assertRaises(ValueError, call_parse, "())")
        self.assertRaises(ValueError, call_parse, "(()")
        self.assertRaises(ValueError, call_parse, "(3+4")
        self.assertRaises(ValueError, call_parse, "3+4)")
        self.assertRaises(ValueError, call_parse, "(3+4))")
        self.assertRaises(ValueError, call_parse, "((3+4)")


class single_number_inputs(unittest.TestCase):
    def test_that_single_digit_integers_return_themselves(self):
        self.assertEqual(call_parse("3"), "3")

    def test_that_multi_digit_integers_return_themselves(self):
        self.assertEqual(call_parse("12"), "12")

    def test_that_rational_numbers_return_themselves(self):
        self.assertEqual(call_parse("3.14"), "3.14")

    def test_that_negative_numbers_return_themselves(self):
        self.assertEqual(call_parse("-1"), "-1")
        self.assertEqual(call_parse("-34"), "-34")
        self.assertEqual(call_parse("-2.72"), "-2.72")


class redundant_parenthesis(unittest.TestCase):
    def test_that_single_redudant_parenthesis_get_resolved(self):
        self.assertEqual(call_parse("(34)"), "34")

    def test_that_multiple_redudant_parenthesis_get_resolved(self):
        self.assertEqual(call_parse("(((34)))"), "34")


if __name__ == '__main__':
    unittest.main()