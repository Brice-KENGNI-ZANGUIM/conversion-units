from conversion_units import temperature

def test_temperature_celcius_to_kelvin() -> None :

    assert temperature.celcius_to_kelvin(0) == 273.15
    
    assert temperature.celcius_to_kelvin(-273.15) == 0.0
