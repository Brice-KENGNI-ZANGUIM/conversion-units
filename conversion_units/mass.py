from conversion_units.unit_multiple import *

# functions collections
def gram_to_kilogram ( mass ) :
    """
    DESCRIPTION : 
    ------------
            Mass conversion from gram (g) to Kilogram (Kg)

    PARAMETERS :
    -----------
        - mass : float
            mass in unit gram (g)

    USAGES :
    -------
    >>> from conversion_units.mass import gram_to_kilogram
    >>> gram_to_kilogram(mass = 1000)
    >>> 1.0
    """

    return mass/KILO