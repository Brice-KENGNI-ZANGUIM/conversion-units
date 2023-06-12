from conversion_units import mass

def test_mass_gram_to_kilogram() -> None :
    assert mass.gram_to_kilogram(235864) == 235.864