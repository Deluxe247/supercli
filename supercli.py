import click

@click.command()
@click.option('--name', '-n', help="Name of person", required=True, prompt="Enter name, please")
@click.argument('number')
def supercli(name, number):
    '''
    This prints "Hello {name}!"

    '''
    for _ in range(int(number)):
        print("Hello, " + name + "!")
