# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

``
As a User 
``

``
So that I can write my shortened name
``

``
I want to be able to get my initials 
when I pass in my fullname
``

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def make_initials(fullname):
    """Extracts the first letters of first and last name and returns it with a . in between

    Parameters: (list all parameters and their types)
        fullname: a string representing a fullname

    Returns: (state the return value and its type)
        a strings, the first letters of the first and last name with a . in between

    Side effects: (state any side effects)
        None
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
make_initials("Sarah Connor") => "S.C"



_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.make_initials import make_initials

"""
Given a fullname
It returns a the first letter of the first and last name with a . in between
"""
def test_make_initials_returns_initials():
    # scenario or setup
    name = "Sarah Connor"

    actual = make_initials(name)

    expected = "S.C"

    assert actual == expected
```

Ensure all test function names are unique, otherwise pytest will ignore them!
