import click

from . import cfg

@click.group()
def dump():
    """Dump the raw Hue data for a specific type of object"""

@dump.command('lights')
def dump_lights():
    cfg.pprint('lights', cfg.bridge.lights())

@dump.command('groups')
def dump_groups():
    cfg.pprint('groups', cfg.bridge.groups())
