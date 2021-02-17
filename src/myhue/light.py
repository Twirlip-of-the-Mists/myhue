import click

import qhue

from . import validate
from . import cfg

@click.group()
def light():
    """Work with lights"""
  
@light.command('list')
def light_list():
    """List all lights"""
    lights = cfg.bridge.lights()
    for id, light in lights.items():
        print(f'{id}: {light["name"]}')

@light.command('dump')
@click.argument('id', type=int)
def light_dump(id):
    """Dump the raw Hue data for a specific light"""
    cfg.pprint('light', cfg.bridge.lights[id]())
    
alert_list = ['none', 'select', 'lselect']
effect_list = ['none', 'colorloop']

@light.command('set')
@click.argument('id', type=int)
@click.option('--result/--no-result', default=True,
              help='Show the result returned by the bridge')
@click.option('--on/--off', default=None,
              help='Turn on or off',)
@click.option('--bri', type=click.IntRange(1, 254),
              help='Set brightness')
@click.option('--hue', type=click.IntRange(0, 65535),
              help='Set hue')
@click.option('--sat', type=click.IntRange(1, 254),
              help='Set saturation')
@click.option('--xy', type=(float, float), default=(None, None), callback=validate.xy,
              help='Set x,y coordinates of a color in CIE color space')
@click.option('--ct', type=click.IntRange(0, 65535),
              help='Set the Mired color temperature')
@click.option('--alert', type=click.Choice(alert_list),
              help='Set the alert effect')
@click.option('--effect', type=click.Choice(effect_list),
              help='Set the dynamic effect')
@click.option('--transitiontime', type=click.IntRange(0, 65535),
              help='Duration of transition, in tenths of a second')
@click.option('--bri-inc', type=click.IntRange(-254, 254),
              help='Change brightness')
@click.option('--sat-inc', type=click.IntRange(-254, 254),
              help='Change satruration')
@click.option('--hue-inc', type=click.IntRange(-65534, 65534),
              help='Change hue')
@click.option('--ct-inc', type=click.IntRange(-65534, 65534),
              help='Change Mired color temperatur')
@click.option('--xy-inc', type=(float, float), default=(None, None), callback=validate.xy_inc,
              help='Change x,y coordinates of a color in CIE color space')
def light_set(id, result, **kwargs):
  """Set the light's state, such as turn it on and off, or modify the hue and effects."""
  for k in list(kwargs.keys()):
    if kwargs[k] in [None, (None, None)]:
      del kwargs[k]
  if kwargs:
    reply = cfg.bridge.lights[id].state(**kwargs)
    if result:
      cfg.pprint('result', reply)
