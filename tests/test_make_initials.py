from lib.make_initials import *
"""
Given a fullname
It returns a the first letter of the first and last name with a . in between
"""
def test_make_initials_returns_initials():
    # scenario or setup
    name = "Sarah Connor"

    # actual, or what the function actually does
    actual = make_initials(name)

    # expected, or the expectation, what we want as an output
    expected = "S.C"
    expected_first_letter = "S"

    # assertion, comparing the actual with the expected if they're the same
    assert actual == expected
    assert make_initials(name) == "S.C"

def test_make_initials_returns_initials_with_another_name():
    # scenario or setup
    name = "Xiao Minh"

    # actual, or what the function actually does
    actual = make_initials(name)

    # expected, or the expectation, what we want as an output
    expected = "X.M"

    # assertion, comparing the actual with the expected if they're the same
    assert actual == expected