import os
import pprint

import click
import click_config_file
from qhue import Bridge #, create_new_username, qhue

from .light import light
from .xml_print import XMLPrint

APP_NAME = 'myhue'
CMD_NAME = 'myhue'
CONF_NAME = 'config'

def default_cfgfile():
    """Return the default configuration filename"""
    cfgfile = os.path.join(click.get_app_dir(CMD_NAME), CONF_NAME)
    return cfgfile

def print_cfgfile(ctx, param, value):
    """Print the default configuration filename"""
    if not value or ctx.resilient_parsing:
        return
    cfgfile = default_cfgfile()
    click.echo(f'{click.format_filename(cfgfile)}')
    ctx.exit()

def add_user(ctx, param, value):
    """Add a new user to a Philips Hue bridge"""
    if not value or ctx.resilient_parsing:
        return
    try:
        #username = create_new_username(value)
        username = 'Feature-currently-disabled'
    except (requests.exceptions.ConnectionError, qhue.QhueException) as e:
        print(e)
    else:
        cfgfile = default_cfgfile()
        click.echo('')
        click.echo(f'Created Hue username: "{username}"')
        click.echo('')
        click.echo(f'Use this on the command line like this:')
        click.echo('')
        click.echo(f'  {CMD_NAME} --bridge {value} --usename {username} ...')
        click.echo('')
        click.echo(f'Suggested Clue config file {cfgfile}:')
        click.echo('')
        click.echo(f'  bridge = "{value}"')
        click.echo(f'  username =  "{username}"')
    finally:
        ctx.exit()

def python_print(name, data):
  pprint.pprint(data, indent=2)
  #pprint.PrettyPrinter(indent=2).pprint(data)

def json_print(name, data):
  print(json.dumps(data, indent=2))

xml_print = XMLPrint()
xml_print.listitems['events'] = 'event'
xml_print.listitems['repeatintervals'] = 'repeatinterval'
xml_print.listitems['inputs'] = 'input'
xml_print.listitems['colorgamut'] = 'xy'
xml_print.listitems['xy'] = 'coord'
xml_print.listitems['conditions'] = 'condition'
xml_print.listitems['actions'] = 'action'
xml_print.listitems['lights'] = 'light'
xml_print.listitems['sensors'] = 'sensor'
xml_print.listitems['links'] = 'link'

formats = {'XML':xml_print.pprint, 'Python':python_print, 'JSON':json_print}

@click.group()

@click_config_file.configuration_option(
    cmd_name=CMD_NAME,
    config_file_name=CONF_NAME
    )

@click.option('-b', '--bridge',
              metavar='BRIDGE',
              required=True,
              help='Bridge\'s hostname or IP address.')

@click.option('-u', '--username',
              metavar='USERNAME',
              required=True,
              help='Bridge\'s REST API username.')

@click.option('-f', '--format',
              type=click.Choice(formats.keys()),
              default='Python',
              help='Format to use for dump commands.')

@click.option('-c', '--cfgfile',
              is_flag=True,
              callback=print_cfgfile,
              expose_value=False,
              is_eager=True,
              help='Show default configuration file and exit.')

@click.option('-a', '--adduser',
              metavar='BRIDGE',
              callback=add_user,
              expose_value=False,
              is_eager=True,
              help='Add a new username to your Hue bridge.')

@click.pass_context
def cli(ctx, bridge, username, format):
  """Examine details of a Philips Hue bridge
  
  The bridge's hostname (or IP address) and a valid REST API username are
  required for this utility to work.
  
  You can find your bridge's IP address from the Hue app, under
  Settings->Hue Bridges->Info
  
  You can generate a new username with the "--adduser" option. This will
  prompt you to press the link button on your bridge to authorize creation
  of a new user.
  
  You can either supply the bridge hostname and username on the command
  line, or in a configuration file.
  
  A typical configuration file will look something like:
  
    \b
    bridge = "hue.localdomain"
    username = "Random-$tr1ng-0f-L3tt3rs-Num8ers-4nd-Dashes"
 
  You can see the default configuration filename with the "--defaults"
  option. You can use a different configuration file with the "--config"
  option.
  
  Note: The "--cfgfile" and "--adduser" options do NOT require any other
  options, despite w
  
  """
  
  ctx.obj = {'bridge': Bridge(bridge, username), 'pprint':formats[format]}

cli.add_command(light)

#if __name__ == '__main__':
    #cli()
