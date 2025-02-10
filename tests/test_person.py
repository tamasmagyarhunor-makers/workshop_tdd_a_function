from lib.person import Person

def test_person_instantiates():
    person = Person('Xiao', 25)

    assert person.name == 'Xiao'
    assert person.age == 25

def test_person_open_door_if_more_than_3_yo():
    person = person = Person('Xiao', 25)

    assert person.open_door() == True

def test_person_cant_open_door_if_less_than_3_yo():
    person = person = Person('Sarah', 2)

    assert person.open_door() == False

