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


class addition(unittest.TestCase):
    def test_addition_of_two_numbers(self):
        self.assertEqual(call_parse("3+4"), "7.0")

    def test_addition_of_three_numbers(self):
        self.assertEqual(call_parse("3+4+5"), "12.0")

    def test_addition_with_one_negative_number(self):
        self.assertEqual(call_parse("4+-3"), "1.0")
        self.assertEqual(call_parse("-3+4"), "1.0")

    def test_addition_of_two_negative_numbers(self):
        self.assertEqual(call_parse("-3+-4"), "-7.0")

    def test_addition_of_multi_digit_integerns(self):
        self.assertEqual(call_parse("10+101"), "111.0")
        self.assertEqual(call_parse("10+-11"), "-1.0")


class subtraction(unittest.TestCase):
    def test_subtraction_of_two_numbers(self):
        self.assertEqual(call_parse("3-4"), "-1.0")

    def test_subraction_of_three_numbers(self):
        self.assertEqual(call_parse("9-6-3"), "0.0")

    def test_subtraction_with_one_negative_number(self):
        self.assertEqual(call_parse("4--3"), "7.0")
        self.assertEqual(call_parse("-3-4"), "-7.0")

    def test_subtraction_of_two_negative_numbers(self):
        self.assertEqual(call_parse("-3--4"), "1.0")

    def test_subtraction_of_multi_digit_integers(self):
        self.assertEqual(call_parse("101-10"), "91.0")
        self.assertEqual(call_parse("11--10"), "21.0")


class multiplication(unittest.TestCase):
    def test_multiplication_of_two_numbers(self):
        self.assertEqual(call_parse("3*4"), "12.0")

    def test_multiplication_of_three_numbers(self):
        self.assertEqual(call_parse("3*4*5"), "60.0")

    def test_multiplication_with_one_negative_number(self):
        self.assertEqual(call_parse("-3*4"), "-12.0")
        self.assertEqual(call_parse("3*-4"), "-12.0")

    def test_multiplication_of_two_negative_numbers(self):
        self.assertEqual(call_parse("-3*-4"), "12.0")

    def test_multiplication_of_multi_digit_integers(self):
        self.assertEqual(call_parse("100*13"), "1300.0")


class division(unittest.TestCase):
    def test_division_of_two_numbers(self):
        self.assertEqual(call_parse("12/3"), "4.0")

    def test_division_of_three_numbers(self):
        self.assertEqual(call_parse("12/3/2"), "2.0")

    def test_division_with_one_negative_number(self):
        self.assertEqual(call_parse("-12/3"), "-4.0")
        self.assertEqual(call_parse("12/-3"), "-4.0")

    def test_division_of_two_negative_numbers(self):
        self.assertEqual(call_parse("-12/-3"), "4.0")

    def test_division_of_multi_digit_integers(self):
        self.assertEqual(call_parse("100/10"), "10.0")


class operator_precedence(unittest.TestCase):
    def test_that_point_calculation_comes_before_line_calculation(self):
        self.assertEqual(call_parse("2+3*4"), "14.0")
        self.assertEqual(call_parse("2-3*4"), "-10.0")
        self.assertEqual(call_parse("2+12/3"), "6.0")
        self.assertEqual(call_parse("2-12/3"), "-2.0")


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