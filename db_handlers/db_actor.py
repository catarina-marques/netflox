import db_handlers.db_connect as con


def add_actor(name):
    querystring = "INSERT INTO actor(name) VALUES('" + name + "')"

    if con.execute_insertquery(querystring):
        return True
    else:
        return False


def check_if_actor_exists(name):
    querystring = "SELECT EXISTS(SELECT 1 FROM actor WHERE name = '" + name + "')"

    if con.execute_selectonequery(querystring):
        return True
    else:
        return False


def get_article(id):
    querystring = "SELECT * FROM actor WHERE id = {} LIMIT 1".format(id)
    return con.execute_selectonequery(querystring)
