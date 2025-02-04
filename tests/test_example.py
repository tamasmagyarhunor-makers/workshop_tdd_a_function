from lib.example import example

def test_example():
    example_called = example()

    actual = example_called
    expected = 'hello'
    assert actual == expected

