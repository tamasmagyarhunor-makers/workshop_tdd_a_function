from lib.hows_the_weather import hows_the_weather
from unittest.mock import patch

def test_go_out_if_weather_is_sunny():
    with patch('random.choice', return_value='sunny'):
        actual = hows_the_weather()
        expected = 'Go out, its sunny'

        assert actual == expected

def test_stay_home_if_weather_is_rainy():
    with patch('random.choice', return_value='rainy'):
        actual = hows_the_weather()
        expected = 'Stay home, its raining'

        assert actual == expected