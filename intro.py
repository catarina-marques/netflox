import login
import register


def main():
    #import register
    #import login

    while True:
        print("Do you want to register or log in? (R or L)")
        registerorlogin = None
        registerorlogin = input()
        if registerorlogin == 'R' or registerorlogin == 'r' :

            register.mainreg()

        elif registerorlogin == 'L' or registerorlogin == 'l' :
            
            login.mainlog()
        else :
            print("Invalid option.")


main()

