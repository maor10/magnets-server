import click

from magnets.orm.db import connect_to_db


@click.command()
def test_db():
    connect_to_db()


if __name__ == '__main__':
    test_db()