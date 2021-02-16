import click
import qhue

def user_add(ctx, param, bridge):
    """
    Add a new user to a Philips Hue bridge
    Call as a click eager option callback
    """
    if not bridge or ctx.resilient_parsing:
        return
    try:
        #username = create_new_username(bridge)
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
        click.echo(f'  {CMD_NAME} --bridge {bridge} --usename {username} ...')
        click.echo('')
        click.echo(f'Suggested Clue config file {cfgfile}:')
        click.echo('')
        click.echo(f'  bridge = "{bridge}"')
        click.echo(f'  username =  "{username}"')
    finally:
        ctx.exit()

@click.group()
def user():
    """Work with users (actually the config whitelist)"""
  
@user.command('list', short_help='List all users')
@click.pass_context
def user_list(ctx):
    """List all users.
    
    Users are actually part of the config whitelist, so can also be seen with the config command.
    """
    for id, user in ctx.obj['bridge'].config()['whitelist'].items():
        #print(id, user)
        print(f'{id}: {user["name"]}')

@user.command('dump', short_help='Dump data for one user')
@click.argument('id')
@click.pass_context
def user_dump(ctx, id):
    """Dump the raw Hue data for one specific user.
    
    Users are actually part of the config whitelist, so can also be dumped
    with the config dump command.
    """
    try:
        ctx.obj['pprint']('light', ctx.obj['bridge'].config()['whitelist'][id])
    except KeyError:
        raise click.ClickException(f'No such user "{id}".')
    
@user.command('delete', short_help='Delete a user (depricated).')
@click.argument('id')
@click.pass_context
def user_delete(ctx, id):
    """Delete a user.
  
    No longer supported by Hue bridges -
    you have to use https://account.meethue.com/apps
    """
    #try:
    print(ctx.obj['bridge']('config', 'whitelist', id, http_method='delete'))
    #except qhue.qhue.QhueException:
        #raise click.ClickException(f'No such user "{id}".')
