import psycopg2
from models.base import Base


def create_db(user: str, password: str):
    connection = psycopg2.connect(user=user, password=password)
    cursor = connection.cursor()
    sql_create_database = "create database casino_db"
    cursor.execute(sql_create_database)
    connection.commit()


if __name__ == "__main__":
    create_db(user="postgres", password="3657")
    # Creating tables in db
    Base.metadata.create_all(engine)
