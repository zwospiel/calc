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

    def test_that_uneven_parentheses_raise_value_errors(self):
        self.assertRaises(ValueError, call_parse, "(")
        self.assertRaises(ValueError, call_parse, ")")
        self.assertRaises(ValueError, call_parse, "())")
        self.assertRaises(ValueError, call_parse, "(()")
        self.assertRaises(ValueError, call_parse, "(3+4")
        self.assertRaises(ValueError, call_parse, "3+4)")
        self.assertRaises(ValueError, call_parse, "(3+4))")
        self.assertRaises(ValueError, call_parse, "((3+4)")

    def test_that_incorrectly_nested_parentheses_raise_value_errors(self):
        self.assertRaises(ValueError, call_parse, ")3+4(")
        self.assertRaises(ValueError, call_parse, "2*)3+4(*5")


class single_numbers(unittest.TestCase):
    def test_parsing_of_single_digit_integers(self):
        self.assertEqual(call_parse("3"), "3")

    def test_parsing_of_multi_digit_integers(self):
        self.assertEqual(call_parse("12"), "12")

    def test_parsing_of_rational_numbers(self):
        self.assertEqual(call_parse("3.14"), "3.14")

    def test_parsing_of_negative_numbers(self):
        self.assertEqual(call_parse("-1"), "-1")
        self.assertEqual(call_parse("-34"), "-34")
        self.assertEqual(call_parse("-2.72"), "-2.72")


class nesting(unittest.TestCase):
    def test_redudant_parentheses(self):
        self.assertEqual(call_parse("(((34)))"), "34")

    def test_nesting(self):
        self.assertEqual(call_parse("(3+4)*2"), "14.0")

    def test_deep_nesting(self):
        self.assertEqual(call_parse("(2*(3+4))*2"), "28.0")

    def test_parallel_nesting(self):
        self.assertEqual(call_parse("(3+4)*(2+5)"), "49.0")


if __name__ == '__main__':
    unittest.main()