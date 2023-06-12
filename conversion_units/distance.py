from conversion_units.unit_multiple import *

def meter_to_kilometer ( d ) :
    """
    DESCRIPTION : 
    ------------
            distance conversion from meter (m) to Kilometer (Km) unit

    PARAMETERS :
    -----------
        - d : float
            distance in unit meter (m)

    USAGES :
    -------
    >>> from conversion_units.distance import meter_to_kilometer
    >>> meter_to_kilometer( d = 12000.0 )
    >>> 12.0
    """
    
    return d/KILO