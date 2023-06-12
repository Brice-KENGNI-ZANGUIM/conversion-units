from conversion_units.unit_multiple import *

# functions collections

def kelvin_to_celcius ( temperature : float ) -> float :
    """
    DESCRIPTION : 
    ------------
            Temperature conversion from Kelvin (K) to Celcius (°C) unit  :  °C = K - 273.15

    PARAMETERS :
    -----------
        - temperature : float
            Temperature in unit Kelvin (K)

    USAGES :
    -------
    >>> from conversion_units.temperature import kelvin_to_celcius
    >>> kelvin_to_celcius( temperature = 0 )
    >>> -237.15
    """
    
    return temperature - 273.15

def celcius_to_kelvin ( temperature : float ) -> float :
    """
    DESCRIPTION : 
    ------------
            Temperature conversion from Celcius (°C) to Kelvin (K) unit  :  K = °C + 273.15

    PARAMETERS :
    -----------
        - temperature : float
            Temperature in unit Celcius (°C)

    USAGES :
    -------
    >>> from conversion_units.temperature import celcius_to_kelvin
    >>> celcius_to_kelvin( temperature = 0 )
    >>> 237.15
    """
    
    return temperature + 273.15

def celcius_to_fahrenheit ( temperature : float ) -> float :
    """
    DESCRIPTION : 
    ------------
            Temperature conversion from Celcius (°C) to Fahrenheit (°F) unit : °F =  9/5 x°C + 32.

    PARAMETERS :
    -----------
        - temperature : float
            Temperature in unit Celcius (°C)

    USAGES :
    -------
    >>> from conversion_units.temperature import celcius_to_fahrenheit
    >>> celcius_to_fahrenheit( temperature = 0 )
    >>> 32.
    """
    
    return temperature*1.8 + 32.0

def fahrenheit_to_celcius ( temperature : float ) -> float :
    """
    DESCRIPTION : 
    ------------
            Temperature conversion from Fahrenheit (°F) to Celcius (°C) unit : °C =  (°F - 32.)x5/9

    PARAMETERS :
    -----------
        - temperature : float
            Temperature in unit Fahrenheit (°F)

    USAGES :
    -------
    >>> from conversion_units.temperature import fahrenheit_to_celcius
    >>> fahrenheit_to_celcius( temperature = 41 )
    >>> 5.0
    """
    
    return 5/9*(temperature -32.0)

def rankine_to_celcius ( temperature : float ) -> float :
    """
    DESCRIPTION : 
    ------------
            Temperature conversion from Rankine (°R) to Celcius (°C) unit : Rankine : °C = 5/9 x °R - 273.15

    PARAMETERS :
    -----------
        - temperature : float
            Temperature in unit Rankine (°R)

    USAGES :
    -------
    >>> from conversion_units.temperature import rankine_to_celcius
    >>> rankine_to_celcius( temperature = 18. )
    >>> -263.15
    """
    
    return 5/9*temperature - 273.15

def celcius_to_rankine ( temperature : float ) -> float :
    """
    DESCRIPTION : 
    ------------
            Temperature conversion from Celcius (°C) to Rankine (°R) unit : Rankine : °R = 9/5x (°C + 273.15)

    PARAMETERS :
    -----------
        - temperature : float
            Temperature in unit Celcius (°C)

    USAGES :
    -------
    >>> from conversion_units.temperature import celcius_to_rankine
    >>> celcius_to_rankine( temperature = -263.15 )
    >>> 18.0
    """
    
    return 1.8*(celcius_to_kelvin(temperature=temperature))

def kelvin_to_rankine ( temperature : float ) -> float :
    """
    DESCRIPTION : 
    ------------
            Temperature conversion from Kelvin (K) to Rankine (°R) unit : Rankine : °R = 9/5x (K)

    PARAMETERS :
    -----------
        - temperature : float
            Temperature in unit Kelvin (K)

    USAGES :
    -------
    >>> from conversion_units.temperature import kelvin_to_rankine
    >>> kelvin_to_rankine( temperature = 30.0 )
    >>> 54.0
    """
    
    return celcius_to_rankine(kelvin_to_celcius(temperature=temperature) )

def rankine_to_kelvin ( temperature : float ) -> float :
    """
    DESCRIPTION : 
    ------------
            Temperature conversion from Rankine (°R) to Kelvin (K) unit : Rankine : K = 5/9x (°R)

    PARAMETERS :
    -----------
        - temperature : float
            Temperature in unit Rankine (°R)

    USAGES :
    -------
    >>> from conversion_units.temperature import rankine_to_kelvin
    >>> rankine_to_kelvin( temperature = 54. )
    >>> 30.0
    """
    
    return celcius_to_kelvin(rankine_to_celcius(temperature=temperature) )