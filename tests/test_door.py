from lib.door import Door
from unittest.mock import Mock

def test_door_instantiates_with_color():
    door = Door('blue')

    actual = door.colour
    expected = 'blue'

    assert actual == expected

def test_door_opens():
    person = Mock()
    person.open_door.return_value = True
    door = Door('blue')

    actual = door.open(person)
    expected = True

    assert actual == expected