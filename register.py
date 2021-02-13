def mainreg():
    import db_handlers
    #import login
    while True:
        print("Register yourself:")
        print("Name:")
        user_name_input = input()
        email_input = emailcheck()
        print("Password:")
        password_input = input()
        newid = db_handlers.add_user(user_name_input, email_input, password_input)
        if newid != None :

            #user = db_handlers.get_user_by_filter('email', email_input)

            #user = db_handlers.get_user(email_input)
            #print( "user id" + user[0])
            db_handlers.create_balance(newid)
            print("Registration successful. Going to login.")
            import login
            login.mainlog()
            break
        else:
            print("Registration failed. Email might not be unique. Try again.")
            continue


def emailcheck():
    import db_handlers
    while True:
        print("Email:")
        email = input()
        if db_handlers.check_if_email_exists(email):
            print("This email already exists. Try again.")
            continue
        else:
            return email
            break

