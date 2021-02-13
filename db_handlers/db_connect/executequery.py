# executequery.py
import psycopg2


def create_connection():
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database="netflox")
    return connection


def execute_insertquery(pgquery):
    connection = None
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(pgquery)
        connection.commit()
        if cursor.rowcount == 1:
            return True

        print("Customer added successfully in PostgreSQL ")
    except (Exception, psycopg2.IntegrityError):
        return False
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return False
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            # print("PostgreSQL connection is closed")


def execute_selectonequery(pgquery):
    connection = None
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(pgquery)
        test = cursor.fetchone()[0]
        connection.commit()
        return test
    except (Exception, psycopg2.IntegrityError):
        return False
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return False
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            # print("PostgreSQL connection is closed")


def execute_insertandreturnquery(pgquery):
    connection = None
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(pgquery)
        connection.commit()
        return cursor.fetchone()[0]


    except (Exception, psycopg2.IntegrityError) as error:
        return False
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return False
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            # print("PostgreSQL connection is closed")



def execute_insertandreturnonequery(pgquery):
    connection = None
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(pgquery)
        connection.commit()
        return cursor.fetchone()

    except (Exception, psycopg2.IntegrityError) as error:
        return False
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return False
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            # print("PostgreSQL connection is closed")


def execute_insertandreturnallquery(pgquery):
    connection = None
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(pgquery)
        connection.commit()
        return cursor.fetchall()

    except (Exception, psycopg2.IntegrityError) as error:
        return False
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return False
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            # print("PostgreSQL connection is closed")

