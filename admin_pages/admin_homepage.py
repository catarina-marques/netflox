def main(result):
    print("Admin Homepage")
    print(
        "1:View all articles | 2:Manage articles | 3:Send messages | 4:Add balance | 5:Statistics | 6:Logout")
    buttonpressed = None
    buttonpressed = input()
    select_opt_homepage(buttonpressed,result)


def select_opt_homepage(buttonpressed,result):
    if buttonpressed == '1':
        from admin_pages import view_all_articles
        view_all_articles.main(result),

    elif buttonpressed == '2':
        from admin_pages import manage_articles
        manage_articles.main(result)

    elif buttonpressed == '3':
        from admin_pages import send_messages
        send_messages.main(result)

    elif buttonpressed == '4':
        from admin_pages import manage_balance
        manage_balance.main(result)

    elif buttonpressed == '5':
        from admin_pages import business_statistics
        business_statistics.main(result)
    else:
        print("bad. going back")
        select_opt_homepage()



def wrong():
    print("Wrong button. Try again.")
    main()