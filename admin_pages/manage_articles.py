def main(result):
    print("Articles")
    print("1:Add | 2:Edit | 3:Delete | 4: Back")
    buttonpressed = None
    buttonpressed = input()
    select_opt_manage_articles(buttonpressed,result)


def select_opt_manage_articles(buttonpressed,result):

    if buttonpressed == '1':
        #print("Add")
        from admin_pages import add_article
        add_article.main(result)

    elif buttonpressed == '2':
        #print("Edit")
        from admin_pages import edit_article
        edit_article.main(result)

    elif buttonpressed == '3':
        #print("Delete")
        from admin_pages import delete_article
        delete_article.main(result)

    elif buttonpressed == '4':
        print("Going back")
        from admin_pages import admin_homepage
        admin_homepage.main(result)

    else:
        print("Invalid option.")
        select_opt_manage_articles()

