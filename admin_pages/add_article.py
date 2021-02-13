def main(result):
    from db_handlers import db_article
    from db_handlers import db_price
    from db_handlers import db_stock
    from db_handlers import db_duration
    from admin_pages import admin_homepage
    from . import manage_articles
    import loggedin
    print("Add Article")

    print("Enter a name for new article: ")
    article_name = input()
    print("Enter price: ")
    article_price = input()
    print("Enter stock: ")
    article_stock = input()
    print("Enter lease duration: ")
    article_expiration = input()

    id = db_article.add_article(article_name, article_price, article_stock, article_expiration)
    #db_stock.add_stock(id, article_stock)
    db_price.add_price(article_price, loggedin.currentuser, id )
    #db_duration.add_expiration(article_expiration, loggedin.currentuser, id)

    print("Article added. Returning to homepage.")
    admin_homepage.main(result)
