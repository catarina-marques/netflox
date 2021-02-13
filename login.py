import psycopg2

from client_pages import client_homepage


def mainlog():
    import db_handlers
    from admin_pages import admin_homepage
    #from client_pages import client_homepage
    import loggedin
    while True:
        print("Login")
        print("Email:")
        email = input()
        print("Password:")
        password = input()

        result = db_handlers.userlogin(email, password)
        if result is False:
            print("Something went wrong. Try again")
            continue
        elif result is None:
            print("Login information was wrong. Try again")
            continue
        else:
            print("Login successful.")
            loggedin.currentuser = result
            if db_handlers.checkifadmin(result):
                admin_homepage.main(result)
                break
            else:
                client_id = db_handlers.get_user(result)
                client = db_handlers.get_user_overview(client_id)
                client_name = client[1]
                conn = psycopg2.connect(host="localhost", dbname="netflox", user="postgres", password="postgres")
                cur = conn.cursor()
                client_homepage.menuCliente(client_name, result, conn, cur)
                break



