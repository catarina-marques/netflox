import db_handlers.db_connect as con


def checkifadmin(id):
    querystring = "SELECT EXISTS(SELECT 1 FROM admin WHERE user_id = '{}')".format(id)
    return con.execute_selectonequery(querystring)