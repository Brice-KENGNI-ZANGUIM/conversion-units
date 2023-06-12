from conversion_units import distance

def test_distance_meter_to_kilometer() -> None : 
    assert distance.meter_to_kilometer(253214) == 253.214