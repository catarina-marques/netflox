import db_handlers.db_connect as con

def check_if_rent_exists(id):
    querystring = "SELECT EXISTS(SELECT 1 FROM rent_article WHERE article_id = '" + id + "')"

    if con.execute_selectonequery(querystring) == True :
        return True
    else:
        return False

def check_if_rent_date_exists(filterparameter):
    querystring = "SELECT EXISTS(SELECT 1 FROM rent WHERE purchase_date = 'filterparameter')"

    if con.execute_selectonequery(querystring) == True :
        return True
    else:
        return False



def get_article_rent_overview():
    querystring = "SELECT rent.id, rent.purchase_date, rent.price, rent.user_id FROM rent"
    return con.execute_insertandreturnallquery(querystring)


def get_numberoftimes_by_article(id):
    querystring = "SELECT COUNT(*) FROM rent_article WHERE article_id = '" + id + "' "
    return con.execute_insertandreturnonequery(querystring)

def get_rent_by_timeframe(sday, smonth, syear, eday, emonth, eyear):
    querystring= "SELECT SUM(rent.price) FROM rent WHERE rent.purchase_date >= '" + syear + "-" + smonth + "-" + sday + " 00:00:00' AND rent.purchase_date <= '" + eyear + "-" + emonth + "-" + eday + " 00:00:00'"
    return con.execute_insertandreturnonequery(querystring)