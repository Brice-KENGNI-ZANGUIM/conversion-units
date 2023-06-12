from conversion_units.unit_multiple import *

def second_to_milli_second ( time : float) -> float :
    """
    DESCRIPTION : 
    ------------
            Time conversion from second ( s ) to millisecond ( ms)

    PARAMETERS :
    -----------
        - time : float
            the time in unit second (s)

    USAGES :
    -------
    >>> from conversion_units.time import second_to_milli_second
    >>> second_to_milli_second(time = 1)
    >>> 1000.0
    """

    return time/MILLI

def minutes_to_second ( time : float ) -> float :
    """
    DESCRIPTION : 
    ------------
            Time conversion from minutes ( Mins ) to second (s)

    PARAMETERS :
    -----------
        - time : float
            the time in unit minutes (Mins)

    USAGES :
    -------
    >>> from conversion_units.time import minutes_to_second
    >>> minutes_to_sec(time = 2.)
    >>> 120
    """

    return 60*time

def hours_to_minute ( time : float ) -> float :
    """
    DESCRIPTION : 
    ------------
            Time conversion from hours ( H ) to minutes (Mins)

    PARAMETERS :
    -----------
        - time : float
            the time in unit hours ( H )

    USAGES :
    -------
    >>> from conversion_units.time import hours_to_minute
    >>> hours_to_minute(time = 4.)
    >>> 240.0
    """

    return 60*time