import os

import click
import click_config_file
from qhue import Bridge #, create_new_username, qhue

from .light import light
from .group import group
from .dump import dump
from .user import user, user_add
from .formats import formats
from . import cfg

APP_NAME = 'myhue'
CMD_NAME = 'myhue'
CONF_NAME = 'config'

def default_cfgfile():
    """Return the default configuration filename"""
    cfgfile = os.path.join(click.get_app_dir(CMD_NAME), CONF_NAME)
    return cfgfile

def print_defcfg(ctx, param, value):
    """Print the default configuration filename"""
    if not value or ctx.resilient_parsing:
        return
    cfgfile = default_cfgfile()
    click.echo(f'{click.format_filename(cfgfile)}')
    ctx.exit()

# CLick normally only uses '--help' for help. Fix that.
CONTEXT_SETTINGS = dict(help_option_names=['-h', '-?', '--help'])
@click.group(context_settings=CONTEXT_SETTINGS)

@click_config_file.configuration_option(
    '-c', '--config',
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
              default='YAML',
              help='Output format to use for dump commands.')

@click.option('-i', '--indent',
              type=click.IntRange(0, 255),
              metavar='SPACES',
              default=4,
              help='Number of spaces to use for indent.')

@click.option('-t', '--traceback/--no-traceback',
              default=False,
              help='Print tracebacks for Hue errors.')

@click.option('-d', '--defcfg',
              is_flag=True,
              callback=print_defcfg,
              expose_value=False,
              is_eager=True,
              help='Show default configuration filename.')

@click.option('-a', '--adduser',
              metavar='BRIDGE',
              callback=user_add,
              expose_value=False,
              is_eager=True,
              help='Add a new username to your Hue bridge.')

#@click.pass_context
def cli(bridge, username, format, indent, traceback):
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
    
    A typical configuration file will look something like this:
    
     \b
     bridge = "hue.localdomain"
     username = "Random-$tr1ng-0f-L3tt3rs-Num8ers-4nd-Dashes"
    
    You can see the default configuration filename with the "--defcfg"
    option. You can use a different configuration file with the "--config"
    option.
    
    """
    cfg.traceback = traceback
    cfg.bridge = Bridge(bridge, username)
    cfg.pprint = formats[format]
    cfg.indent = indent
    
# Pull in commands from other modules
cli.add_command(light)
cli.add_command(group)
cli.add_command(dump)
cli.add_command(user)

#if __name__ == '__main__':
    #cli()
