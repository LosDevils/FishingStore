import psycopg2

from inventory.infrastructure.database.models.base import Base


def create_db(engine):
    connection = psycopg2.connect(user="postgres", password="postgres")
    connection.autocommit = True
    cursor = connection.cursor()
    sql_create_database = "create database inventory"
    cursor.execute(sql_create_database)
    connection.commit()
    Base.metadata.create_all(bind=engine)
