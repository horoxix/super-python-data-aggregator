import click
from lib.insert import import_from_csv_file as pcsv
from lib.insert import import_from_blazemeter as blaze
from lib.helper import get_db_type
from migration import mysql_run_changelog, psql_run_changelog
from lib.setup import mysql_create_spyda_database, psql_create_spyda_database
import lib.display.display_suite_run_history as dsrh
import lib.display.display_call_statistics as dcs


@click.group()
@click.version_option(version=1.0)
def cli():
    pass


@cli.command()
@click.argument('display_table', required=1)
@click.option('--db_type', default=get_db_type.MySQL, help='type of DB inserting into (MySQL is default)')
def display(display_table, db_type):
    click.echo('generating data set...')
    if display_table == 'call_statistics':
        dcs.get_display_latest_call_statistics(db_type)
    elif display_table == 'suite_run_history':
        dsrh.get_display_suite_run_history(db_type)


@cli.command()
@click.argument('data_loc', default='none')
@click.option('--data_type', default='online', help='what type of data you are inserting.')
@click.option('--table', default='call_statistics', help='table to insert information into.')
@click.option('--db_type', default=get_db_type.MySQL, help='type of Database you are inserting into.')
def insert(data_loc, data_type, table, db_type):
    click.echo('Attempting to insert data...')
    if data_type == 'online':
        click.echo('Session ID : ' + str(data_loc))
        click.echo('Inserting data...')
        blaze.insert_results_from_blazemeter_v4(data_loc, db_type, table)
    elif data_type == 'csv':
        click.echo('CSV File : ' + str(data_loc))
        click.echo('Inserting data...')
        pcsv.insert_data_from_csv(data_loc, db_type, table)
    click.echo('Data inserted!')


@cli.command()
@click.argument('db_type', required=1, default=get_db_type.MySQL.db_type)
@click.option('--new', default='false', help='creates the spyda database for the first time.')
@click.option('--clear', default='false', help='clear database before setup (default=false)')
def setup(db_type, new, clear):
    click.echo('Setting up spyda database...')
    if get_db_type.get_database_type(db_type) == get_db_type.MySQL:
        if new:
            click.echo("Creating new spyda database...")
            mysql_create_spyda_database.create_database()
        if clear:
            click.echo("Dropping previous spyda database...")
            mysql_create_spyda_database.drop_database()
            click.echo("Creating new spyda database...")
            mysql_create_spyda_database.create_database()
        click.echo("Running liquibase changesets...")
        mysql_run_changelog.run_liquibase_setup()
    elif get_db_type.get_database_type(db_type) == get_db_type.PostgreSQL:
        if new:
            click.echo("Running liquibase changesets...")
            psql_run_changelog.run_liquibase_setup()
        if clear:
            click.echo("Dropping previous spyda database...")
            psql_create_spyda_database.drop_database()
            click.echo("Creating new spyda database...")
            psql_create_spyda_database.create_database()
        click.echo("Running liquibase changesets...")
        psql_run_changelog.run_liquibase_setup()
    click.echo("Database setup complete!")


@cli.command()
def config():
    click.echo("config")


if __name__ == '__main__':
    cli()
