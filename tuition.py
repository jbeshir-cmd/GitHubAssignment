import argparse
import sys

def calculate_tuition(credits = 12, resident = True, dt = False):
    """ Calculates tuition and mandatory fees for one semester at UMD.

    Takes into consideration the number of credits the student is taking,
    whether they are a resident of Maryland, and whether they pay
    differential tuition.

    Args:
        credits (integer): the number of credits the student is taking
            (default: 12).
        resident (boolean): whether the student is considered a
            Maryland state resident for tuition purposes (default: True).
        dt (boolean): whether or not the student pays
            differential tuition (default: False).

    Raises:
        ValueError: credits must be non-negative.

    Returns:
        float: the student's combined tuition and mandatory fees.
    """
    if credits < 0:
        raise ValueError
    if credits == 0:
        return 0.0
    if credits >= 12:
        tuition = 4412.00 if resident else 17468.00
    else:
        tuition = 367 * credits if resident else 1456.00 * credits 
    
    if dt:
        if credits >= 12:
            tuition += 1428.00
        else: 
            tuition += 118.00 * credits
    if credits >= 9:
        tuition += 977.50
    else:
        tuition += 455.00

    return tuition
def parse_args(arglist):
    """ Parses command-line arguments.

    The following optional command-line arguments are defined:

    -c / --credits: the number of credits the student is taking
        (type: int, default: 12)
    -nr / --nonresident: indicates the student is not a Maryland
        resident (action: 'store_true')
    -dt / --differentialtuition: indicates the student pays differential
        tuition (action: 'store_true')

    Args:
        arglist (list of str): a list of command-line arguments.

    Returns:
        namespace: a namespace with variables credits, nonresident, and
        differentialtuition.
    """
    parser = argparse.ArgumentParser() 
    parser.add_argument('-c','--credit', type = int, default = 12)
    parser.add_argument('-nr', '--nonresident', action= 'store_true')
    parser.add_argument('-dt', '--differentialtuition', action='store_true')
    return namespace == parser.parse_args(arglist)
    return namespace

    