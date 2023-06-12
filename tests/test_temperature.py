from conversion_units import temperature


def test_temperature_celcius_to_kelvin() -> None :

    assert temperature.celcius_to_kelvin(0) == 273.15

    assert temperature.celcius_to_kelvin(-273.15) == 0.0


def test_kelvin_to_celcius() -> None :

    assert temperature.kelvin_to_celcius(2.0) == -271.15


def test_celcius_to_fahrenheit() -> None :
    
    assert temperature.celcius_to_fahrenheit(0.0) == 32.0

    assert temperature.celcius_to_fahrenheit(5.0) == 41.0


def test_fahrenheit_to_celcius() -> None :

    assert temperature.fahrenheit_to_celcius(32.0) == 0.0

    assert temperature.fahrenheit_to_celcius(41.0) == 5.0


def test_rankine_to_celcius() -> None : 

    assert temperature.rankine_to_celcius( 0.0 ) == -273.15

    assert temperature.rankine_to_celcius( 18.0 ) == -263.15

def test_celcius_to_rankine ( ) -> None :

    assert temperature.celcius_to_rankine( -263.15) == 18.0

    assert temperature.celcius_to_rankine( -273.15) == 0.0

def test_kelvin_to_rankine ( ) -> None :

    assert temperature.kelvin_to_rankine ( 30.0) == 54.0

    assert temperature.kelvin_to_rankine ( 5.0) == 9.0

def test_rankine_to_kelvin( ) -> None :

    assert temperature.rankine_to_kelvin( 54.0) == 30.0

    assert temperature.rankine_to_kelvin( 9.0) == 5.0