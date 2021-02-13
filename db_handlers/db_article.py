import db_handlers.db_connect as con


def add_article(name, price, stock, expiration):
    querystring = "INSERT INTO public.article(name, price, stock, expiration) VALUES('" + name + "','" + price + "', '" + stock + "', '" + expiration + "') RETURNING id"
    article_id = con.execute_insertandreturnquery(querystring)
    return article_id


def check_if_article_exists(name):
    querystring = "SELECT EXISTS(SELECT 1 FROM public.article WHERE name = '" + name + "')"

    if con.execute_selectonequery(querystring):
        return True
    else:
        return False


def get_article(id):
    querystring = "SELECT * FROM article WHERE id = {} LIMIT 1".format(id)
    return con.execute_selectonequery(querystring)


def delete_article(id):
    querystring = "DELETE FROM article WHERE id = {} RETURNING id".format(id)
    if con.execute_selectonequery(querystring):
        return True
    else:
        return False


def get_article_overview():
    querystring = "SELECT article.id, article.name, article.stock, article.expiration FROM article"
    return con.execute_insertandreturnallquery(querystring)


def get_article_by_filter(filter, filterparameter):
   if filter == 0:
       return get_article_overview()
   elif filter == "id":
       querystring = "SELECT article.id, article.name, article.price FROM article WHERE article.id ='" + filterparameter + "'"
       return con.execute_insertandreturnonequery(querystring)
   elif filter == "name":
       querystring = "SELECT article.id, article.name, article.price, article.stock FROM article WHERE article.name ='" + filterparameter + "'"
       return con.execute_insertandreturnonequery(querystring)
   elif filter == "genre":
       querystring = "SELECT article.id, article.name, article.stock, genre.name FROM article INNER JOIN article_genre ON article.id = article_genre.article_id INNER JOIN genre ON article_genre.genre_id = genre.id WHERE genre.name = '" + filterparameter + "'"
       return con.execute_insertandreturonequery(querystring)
   elif filter == "actor":
       querystring = "SELECT article.id, article.name, article.stock, actor.name FROM article INNER JOIN article_actor ON article.id = article_actor.article_id INNER JOIN actor ON article_actor.actor_id = actor.id WHERE actor.name = '" + filterparameter + "'"
       return con.execute_insertandreturnonequery(querystring)
   elif filter == " director":
       querystring = "SELECT article.id, article.name, article.stock, director.name FROM article INNER JOIN article_director ON article.id = article_director.article_id INNER JOIN director ON article_director.director_id = director.id WHERE director.name = '" + filterparameter + "'"
       return con.execute_insertandreturnonequery(querystring)
   elif filter == "producer":
       querystring = "SELECT article.id, article.name, article.stock, producer.name FROM article INNER JOIN article_producer ON article.id = article_producer.article_id INNER JOIN producer ON article_producer.producer_id = producer.id WHERE producer.name = '" + filterparameter + "'"
       return con.execute_insertandreturnonequery(querystring)


def edit_name(id, new_name):
    querystring = "UPDATE public.article SET name = '" + new_name + "' WHERE article.id = '" + id + "'"
    return con.execute_insertandreturnquery(querystring)


def edit_price(id, new_price):
    querystring = "UPDATE public.article SET name = '" + new_price + "' WHERE article.id = '" + id + "'"
    return con.execute_insertandreturnquery(querystring)


def edit_stock(id, new_stock):
    querystring = "UPDATE public.article SET stock = '" + new_stock + "' WHERE article.id = '" + id + "'"
    return con.execute_insertandreturnquery(querystring)


def edit_expiration(id, new_expiration):
    querystring = "UPDATE public.article SET expiration = '" + new_expiration + "' WHERE article.id = '" + id + "'"
    return con.execute_insertandreturnquery(querystring)