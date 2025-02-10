from lib.make_initials import *

name = "Sarah Connor"

    # actual, or what the function actually does
actual = make_initials(name)

    # expected, or the expectation, what we want as an output
expected = "S.C"
expected_first_letter = "S"

    # assertion, comparing the actual with the expected if they're the same
print(actual == expected)
print(make_initials(name) == "S.C")