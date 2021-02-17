import click

def xy(cts, param, value):
    """Validate x,y coordinates of a color in CIE color space"""
    (x, y) = value
    if x is not None and not 0.0 <= x <= 1.0:
        raise click.BadParameter(f'x value {x} not in range 0.0 to 1.0')
    if y is not None and not 0.0 <= y <= 1.0:
        raise click.BadParameter(f'y value {y} not in range 0.0 to 1.0')
    return (x, y)

def xy_inc(cts, param, value):
    """Validate increment to x,y coordinates of a color in CIE color space"""
    (x, y) = value
    if x is not None and not -0.5 <= x <= 0.5:
        raise click.BadParameter(f'x value {x} not in range -0.5 to 0.5')
    if y is not None and not -0.5 <= y <= 0.5:
        raise click.BadParameter(f'y value {y} not in range -0.5 to 0.5')
    return (x, y)
