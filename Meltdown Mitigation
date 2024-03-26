"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """

    return True if temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000 else False

def reactor_efficiency(voltage, current, theoretical_max_power):
    value = ( ( voltage * current ) / theoretical_max_power ) * 100
    
    if   value >= 80:                return 'green'
    elif value < 80 and value >= 60: return 'orange'
    elif value < 60 and value >= 30: return 'red'
    else:                            return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    
    value = temperature * neutrons_produced_per_second
    
    if value < threshold * 0.9:
        return 'LOW'
    elif threshold * 0.9 <= value <= threshold * 1.1:
        return 'NORMAL'
    else:
        return 'DANGER'
