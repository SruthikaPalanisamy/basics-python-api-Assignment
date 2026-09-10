import click
@click.command('hello-bench')
def hello_bench():
    print("Hello this is custom CLI")
commands=[hello_bench]