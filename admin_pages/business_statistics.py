from admin_pages import admin_homepage
from db_handlers import db_article


def main(result):
    import db_handlers

    print("Business Statistics")
    print("1: All time | 2: By timeframe | 3: By article | 4: Back")
    buttonpressed = None
    buttonpressed = input()
    select_opt_business_stats(buttonpressed,result)

def select_opt_business_stats(buttonpressed,result):
    if buttonpressed == '1':
        print("All time")
        all_time(result)

    elif buttonpressed == '2':
        print("Last month")
        by_timeframe(result)

    elif buttonpressed == '3':
        print("By article")
        by_article(result)

    elif buttonpressed == '4':
        print("Going back")
        from admin_pages import admin_homepage
        admin_homepage.main(result)
    else:
        print("bad option. try again.")
        select_opt_business_stats()



def all_time(result):
    print("All time sales:")
    from db_handlers import db_rent
    list = db_rent.get_article_rent_overview()
    sum = 0
    for rent in list:
        # this would print a list of all sales
        print("Purchase date: " + str(rent[1]) + " Price: " + str(rent[2]))
        # but i want a sum of all prices in that list
        sum += rent[2]


    print("Total revenue: " + str(sum) + " euros.")

    print("Returning to homepage.")
    admin_homepage.main(result)


def by_timeframe(result):

    print("Introduce start day:")
    start_day = input()
    print("Introduce start month:")
    start_month =input()
    print("Introduce start year:")
    start_year = input()

    print("Introduce end day:")
    end_day = input()
    print("Introduce end month:")
    end_month = input()
    print("Introduce end year:")
    end_year = input()


    from db_handlers import db_rent
    moneymade = db_rent.get_rent_by_timeframe(start_day,start_month,start_year,end_day,end_month,end_year)
    print('We made ' + str(moneymade[0]) + " euros between " + start_day + "-" + start_month + "-" + start_year + " and " + end_day + "-" + end_month + "-" + end_year)

    # if db_rent.check_if_rent_exists():
    #     from db_handlers import db_rent
    #     list = db_rent.get_article_rent_overview()
    #     for rent in list:
    #         import datetime
    #         current_month = datetime.datetime.now().month
    #         month = rent[1]#except i only want the month field here
    #
    #         if current_month == month:
    #             # this would print a list of all sales of that article
    #             print("Id: " + rent[0] + "Purchase Date: " + str(rent[1]) + " Price: " + str(rent[2]))
    #             # but i want a sum of all prices in that list
    #             sum += sum + rent[2]
    #             print("Total revenue of last month: " + sum + " euros.")
    # else:
    #     print("Couldn't find sales. Returning to homepage.")
    #     from admin_pages import main
    #     admin_homepage.main(result)

    print("Returning to homepage.")
    admin_homepage.main(result)



# def by_year(result):
#     print("Last year sales:")
#     from db_handlers import db_rent
#     if db_rent.check_if_rent_exists():
#         from db_handlers import db_rent
#         list = db_rent.get_article_rent_overview()
#         for rent in list:
#             import datetime
#             current_year = datetime.datetime.now().year
#             year = rent[1]  # except i only want the month field here
#
#             if current_year == year:
#                 # this would print a list of all sales of that article
#                 print("Id: " + rent[0] + "Purchase Date: " + str(rent[1]) + " Price: " + str(rent[2]))
#                 # but i want a sum of all prices in that list
#                 sum += sum + rent[2]
#                 print("Total revenue of last month: " + sum + " euros.")
#     else:
#         print("Couldn't find rents with that article. Returning to homepage.")
#         from admin_pages import main
#         admin_homepage.main(result)
#
#     print("Returning to homepage.")
#     admin_homepage.main(result)


def by_article(result):

    print("Introduce article to search its stats.")
    article_id_input = input()

    from db_handlers import db_rent
    if db_rent.check_if_rent_exists(article_id_input):
        from db_handlers import db_rent
        n = db_rent.get_numberoftimes_by_article(article_id_input)
        article = db_article.get_article_by_filter('id', article_id_input)

        sum = n[0] * article[2]

        print("Total revenue of that artice: " + str(sum) + " euros.")

    else:
        print("Couldn't find rents with that article. Returning to homepage.")
        from admin_pages import main
        admin_homepage.main(result)

    print("Returning to homepage.")
    admin_homepage.main(result)




