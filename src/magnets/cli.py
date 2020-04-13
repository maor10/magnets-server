import os

import click

from magnets.consts import UPLOAD_FOLDER
from magnets.orm.db import connect_to_db


@click.group()
@click.pass_context
def cli(ctx):
    pass


@cli.command()
def test_conn():
    connect_to_db()


@cli.command()
def setup():
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.chmod(UPLOAD_FOLDER, 777)
    print("successfully setup")


if __name__ == '__main__':
    cli()
