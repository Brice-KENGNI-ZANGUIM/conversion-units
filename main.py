import conversion_units

print( f"list of environnement : {dir(conversion_units)}" )

print( conversion_units.distance.meter_to_kilometer( 2000 ) )

print( conversion_units.temperature.rankine_to_kelvin( 0 ) )
