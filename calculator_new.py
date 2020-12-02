def parse(formula):
    validate(formula)
    if(is_solvable(formula)):
        return solve(formula)
    start, end = find_partial_formula(formula)
    partial_result = parse(formula[start:end])
    return parse(replace(formula, start, end, partial_result))


def is_solvable(formula):
    return


def solve(formula):
    """Solve the formula respecting operator precedence (dot before line)."""
    return


def find_partial_formula(formula):
    """Return the positions of the parens surrounding the first subformula."""
    return


def replace(string, start, end, replacement):
    """
    Replace a substring of the given string with the replacement.

    Arguments:
    string, replacement:
        The original string and the replacement for the defined substring.
    start, end:
        The positions in the original that define the substring to replace.
        Both are inclusive, that means replace("my_black_tea", 3, 7, "red") 
        will return "my_red_tea".
    """
    return


def validate(formula):
    return