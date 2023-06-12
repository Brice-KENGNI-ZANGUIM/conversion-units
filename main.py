import conversion_units


if __name__ == "__main__" :

    print( f"list of environnement : {dir(conversion_units)}" )
    print( conversion_units.distance.meter_to_kilometer( 2000 ) )
    print( conversion_units.temperature.kelvin_to_rankine( 60 ) )
    print( conversion_units.temperature.kelvin_to_celcius( 0 ) )
    print( conversion_units.temperature.rankine_to_celcius( 27 ) )