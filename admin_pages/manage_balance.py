from admin_pages import admin_homepage


def main(result):
    from db_handlers import db_user
    from db_handlers import db_client
    print("Enter user ID you want to add balance to.")
    user_id_input = input()

    if db_user.get_user(user_id_input):
        print("Is this the user you wish to add balance to?(Y/N)")
        buttonpressed = input()
        if buttonpressed == 'y' or 'Y':
            print("Enter the amount to add")
            amount_input = input()
            db_client.add_balance(user_id_input, amount_input)
            #get existing balance, update query to change the balance to the existing balance plus the amount_input
            print("Amount added. Returning to homepage")
            admin_homepage.main(result)
        else:
            print("Nothing was done. Returning to homepage")
            admin_homepage.main(result)

    else:
        print("Couldn't find the user. Returning to homepage.")
        admin_homepage.main(result)



