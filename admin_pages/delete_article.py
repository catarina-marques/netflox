def main(result):
    from db_handlers import db_article
    from db_handlers import db_price
    from db_handlers import db_duration
    from admin_pages import admin_homepage
    from . import manage_articles
    import loggedin

    print("Delete article")
    print("Introduce article to delete.")
    article_name_input = input()
    if db_article.check_if_article_exists(article_name_input):

        article = db_article.get_article_by_filter('name', article_name_input)
        print("Name : " + article[1])
        print("Price : " + str(article[2]))
        print("Stock : " + str(article[3]))
        print("Is this the article you wish to delete?(Y/N)")
        buttonpressed = input()
        if buttonpressed == 'y' or 'Y':
            db_article.delete_article(article[0])
            print("Article deleted. Returning to homepage")
            admin_homepage.main(result)
        else:
            print("Not deleted. Returning to homepage")
            admin_homepage.main(result)

    else:
        print("Couldn't find the article. Returning to homepage.")
        admin_homepage.main(result)

