from lib.door import Door
from lib.person import Person

def test_door_doesnt_open_if_person_less_than_3_yo():
    person = Person('Harry', 2)
    door = Door('blue')

    actual = door.open(person)
    expected = False

    assert actual == expected

def test_door_opens_if_person_is_more_or_equal_to_3_yo():
    person = Person('Sarah', 4)
    door = Door('blue')

    actual = door.open(person)
    expected = True

    assert actual == expected