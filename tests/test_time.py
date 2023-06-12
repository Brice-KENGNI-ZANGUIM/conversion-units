from conversion_units import time

def test_time_second_to_milli_second() :
    assert time.second_to_milli_second(23.512) == 23512