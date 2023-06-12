import conversion_units

print( f"list of environnement : {dir(conversion_units)}" )

print( conversion_units.distance.meter_to_kilometer( 2000 ) )

print( conversion_units.temperature.kelvin_to_rankine( 60 ) )
