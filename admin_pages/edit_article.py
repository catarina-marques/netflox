import admin_pages
from db_handlers import db_article


def main(result):
    from db_handlers import db_article
    from db_handlers import db_price
    from db_handlers import db_duration
    from admin_pages import admin_homepage
    from . import manage_articles
    import loggedin

    print("Editing article")
    print("Introduce article to edit.")
    article_id_input = input()
    if db_article.get_article(article_id_input):
        print("Is this the article you wish to edit?(Y/N)")
        buttonpressed = input()
        if buttonpressed == 'y' or 'Y':
            field_edit(article_id_input,result)
        else:
            print("Nothing changed. Returning to homepage")
            admin_homepage.main

    else:
        print("Couldn't find the article. Returning to homepage.")
        admin_homepage.main


def wrong():
    print("Something went wrong. Going back.")
    from admin_pages import admin_homepage
    admin_homepage.main


def field_edit(article_id_input,result):
    print("Enter the field to edit.")
    print("1:Name | 2:Price | 3:Stock | 4:Expiration | 5:Details|  6:Go back")
    buttonpressed = None
    buttonpressed = input()
    select_opt_edit_articles(article_id_input,buttonpressed, result)


def select_opt_edit_articles(article_id_input,buttonpressed, result):

    if buttonpressed == '1':
        print("Enter new name")
        new_name = input()
        db_article.edit_name(article_id_input,new_name)
        admin_pages.main(result)


    elif buttonpressed == '2':
        print("Enter new price")
        new_price = input()
        db_article.edit_price(article_id_input, new_price)
        admin_pages.main(result)


    elif buttonpressed == '3':
        print("Enter new stock")
        new_stock = input()
        db_article.edit_stock(article_id_input, new_stock)
        admin_pages.main(result)

    elif buttonpressed == '4':
        print("Enter new expiration")
        new_expiration = input()
        db_article.edit_expiration(article_id_input, new_expiration)
        admin_pages.main(result)

    elif buttonpressed == '5':
        print("Details")
        details(result)

    elif buttonpressed == '6':
        print("Going back")
        admin_pages.main(result)

    else:
        print("bad option. try again")
        select_opt_edit_articles()


def details(result):
    print("Details")
    print("1:Add to database | 2:Associate to article|  3:Go back")
    buttonpressed = None
    buttonpressed = input()
    select_opt_details(buttonpressed, result)


def select_opt_details(buttonpressed, result):
    if buttonpressed == '1':
        print("Add details")
        print("1:Actor | 2:Director| 3:Producer| 4:Genre | 5 :Go back")
        buttonpressed2 = None
        buttonpressed2 = input()
        #select_opt_add_details(buttonpressed2, result)


    elif buttonpressed == '2':
        print("Associate detail")
        print("1:Actor | 2:Director| 3:Producer| 4:Genre | 5 :Go back")
        buttonpressed3 = None
        buttonpressed3 = input()
        # select_opt_associate_details(buttonpressed3, result)

    else:
        print("Going back.")
        admin_pages.admin_homepage(result)



def select_opt_add_details(buttonpressed2, result):
    print("Add Detail")
    if buttonpressed2 == '1':
        print("Actor")
        new_actor = input()
        print("To do.")
        admin_pages.main(result)


    elif buttonpressed2 == '2':
        print("Director")
        new_director = input()
        print("To do.")
        admin_pages.main(result)

    elif buttonpressed2 == '3':
        print("Producer")
        new_producer = input()
        print("To do.")
        admin_pages.main(result)

    elif buttonpressed2 == '4':
        print("Genre")
        new_genre = input()
        print("To do.")
        admin_pages.main(result)

    elif buttonpressed2 == '5':
        print("Going back")
        admin_pages.main(result)


    else:
        print("Bad option. Try again")
        select_opt_add_details()
    admin_pages.admin_homepage(result)



def select_opt_associate_details(buttonpressed3, result):
    print("Associate Detail")
    admin_pages.admin_homepage(result)
