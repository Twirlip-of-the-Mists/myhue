import click

@click.group()
def light():
    """Work with lights"""
  
@light.command('list')
@click.pass_context
def light_list(ctx):
    """List all lights"""
    lights = ctx.obj['bridge'].lights()
    for id, light in lights.items():
        print(f'{id}: {light["name"]}')

@light.command('dump')
@click.argument('id')
@click.pass_context
def light_dump(ctx, id):
  """Show the raw Hue data for a specific light"""
  ctx.obj['pprint']('light', ctx.obj['bridge'].lights[id]())
