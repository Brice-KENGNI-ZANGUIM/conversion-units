from conversion_units import time

def test_time_second_to_milli_second() -> None :

    assert time.second_to_milli_second(23.512) == 23512

def test_hours_to_minute() -> None :
    
    assert time.hours_to_minute(2.5) == 150.0

def test_minutes_to_second() -> None :

    assert time.minutes_to_second(1.5) == 90.0