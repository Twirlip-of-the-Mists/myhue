import click

from . import cfg

@click.group()
def group():
    """Work with groups"""

room_types = [
    'Luminaire',
    'Lightsource',
    'LightGroup',
    'Room',
    'Entertainment',
    'Zone']

@group.command('list')
@click.option('-t', '--type',
              type=click.Choice(room_types),
              multiple=True,
              help='Restrict the list to rooms of TYPE')
def group_list(type):
  """List groups, in format "ID: name (type)" """
  groups = cfg.bridge.groups()
  for id, group in groups.items():
    if group['type'] in type or not type:
      print(f'{id}: {group["name"]} ({group["type"]})')

@group.command('dump')
@click.argument('id', type=int)
def group_dump(id):
    """Dump the raw Hue data for a specific group"""
    cfg.pprint('group', cfg.bridge.groups[id]())
