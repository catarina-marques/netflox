import db_handlers.db_connect as con

def create_balance(id):
    querystring = "INSERT INTO public.client (user_id , balance)  VALUES('" + str(id[0]) + "', '20') "

    if con.execute_insertquery(querystring):
        return True
    else:
        return False
def add_balance(id, bal):
    querystring = "UPDATE public.client SET balance = balance + '" + bal + "' WHERE user_id = '" + id + "'"
    return con.execute_insertandreturnquery(querystring)

def get_balance(id):
    querystring = "SELECT balance  FROM client WHERE user_id = 'id'"
    return con.execute_insertandreturonequery(querystring)