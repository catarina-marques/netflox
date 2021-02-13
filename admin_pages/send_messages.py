from admin_pages import admin_homepage
from db_handlers import db_user, db_msg


def main(result):
    define_recipient(result)


def define_recipient(result):

    print("Send message")
    print("Enter message recipient (email or all)")
    recipient_input = input()

    if recipient_input == 'all' or recipient_input == 'ALL':
        print("Send all")
        print("Enter subject")
        subject_input = input()
        print("Enter content of the message")
        content_input = input()
        msgid = db_msg.create_message(subject_input, content_input, result)
        userlist = db_user.get_all_user_ids()
        for user in userlist :
            db_msg.create_flag_message(msgid[0], user[0])

    elif db_user.check_if_email_exists(recipient_input):
        print("Enter subject")
        subject_input = input()
        print("Enter content of the message")
        content_input = input()
        msgid = db_msg.create_message(subject_input, content_input, result)
        userid = db_user.get_user_by_email(recipient_input)
        db_msg.create_flag_message(msgid[0],userid)
        print("Message sent.")
    else:
        print("That's not a valid recipient.")
        define_recipient(result)


    admin_homepage.main(result)
















