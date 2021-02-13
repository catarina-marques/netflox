def main(result):
    print("View all articles")
    from db_handlers import db_article
    list = db_article.get_article_overview()
    for article in list:
        print("Name: " + article[1] + " Price: " + str(article[2]) + " Stock: " + str(article[3]))

#going back
    print("Back")
    from admin_pages import admin_homepage
    admin_homepage.main(result)


