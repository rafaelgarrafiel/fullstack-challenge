import click

from app.plugins.commands import create_db, drop_db, populate_db


def init_app(app):
    """Disponibilizando comandos para o flask"""
    app.cli.add_command(app.cli.command()(create_db))
    app.cli.add_command(app.cli.command()(drop_db))
    app.cli.add_command(app.cli.command()(populate_db))
