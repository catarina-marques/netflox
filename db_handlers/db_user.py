import db_handlers.db_connect as con


def add_user(name, email, password):
    querystring = "INSERT INTO public.user(name, email, password) VALUES('" + name + "', '" + email + "', crypt('" + password + "', gen_salt('bf')) ) RETURNING id"
    return con.execute_insertandreturnonequery(querystring)



def check_if_email_exists(email):
    querystring = "SELECT EXISTS(SELECT 1 FROM public.user WHERE email = '" + email + "')"

    if con.execute_selectonequery(querystring) == True :
        return True
    else:
        return False


def userlogin(email, password):
    querystring = "SELECT id FROM public.user WHERE email = '" + email + "' AND password = crypt('{}', password) LIMIT 1".format(password)
    return con.execute_selectonequery(querystring)

def get_user(id):
    querystring = "SELECT * FROM public.user WHERE id = {} LIMIT 1".format(id)
    return con.execute_selectonequery(querystring)

def get_user_overview(id):
    querystring = "SELECT id, name, email FROM public.user WHERE id = '"+ str(id) +"'"
    return con.execute_insertandreturnonequery(querystring)

def get_user_by_email(email):
    querystring = "SELECT id FROM public.user WHERE email = '" + email + "'"
    return con.execute_selectonequery(querystring)

def get_user_by_filter(filter, filterparameter):
   if filter == 0:
       return get_user_overview()
   elif filter == "id":
       querystring = "SELECT user.id, user.name, user.email  FROM user WHERE user.id ='" + filterparameter + "'"
       return con.execute_insertandreturnonequery(querystring)
   elif filter == "email":
       querystring = "SELECT  user.id, user.name, user.email FROM  user WHERE user.email ='" + filterparameter + "'"
       return con.execute_insertandreturnonequery(querystring)

def get_all_user_ids():
    querystring = "SELECT id FROM public.user"
    return con.execute_insertandreturnallquery(querystring)

