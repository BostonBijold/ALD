import datetime
# import Flask
import pymongo
# from datetime import date


my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["ALD"]
to_do_col = my_db["to_do_items"]


def enter_to_do():
    to_do_title = input("what do you need to do today(title)? ")
    to_do_details = input("what do you need to do to complete it? ")
    to_do_date = datetime.datetime.now()
    to_do_priority = int(input("What is the priority level? (1-4): "))

    to_do_deadline = datetime.datetime(year=to_do_date.year, month=to_do_date.month,
                                       day=to_do_date.day, hour=23, minute=59).strftime("%Y-%m-%d %H:%M:%S")
    to_do_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    to_do_complete = False

    new_todo = {
        "title": to_do_title,
        "details": to_do_details,
        "date": to_do_date,
        "complete": to_do_complete,
        "deadline": to_do_deadline,
        "priority": to_do_priority
    }
    print(new_todo)
    to_do_col.insert_one(new_todo)


def view_todays_list():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    completed_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # cuts the search down to only today's to_do list.
    to_do_list = to_do_col.find({"date": {"$gte": today}})
    for x in to_do_list:
        print("")
        print("I need to :", x['title'])
        print("Priority :", x["priority"])
        print("Details :", x["details"])
        print("By :", x["deadline"])
        print("Is complete? ", x["complete"])
        print("----------------")

    completed = input("Did you complete one? (y/n) ")

    if completed == "y":
        completed_to_do = input("which did you complete? (title)")
        to_do_col.update_one({"title": completed_to_do},
                             {"$set": {"complete": True, "completed_time": completed_datetime}})


def main():
    while True:
        print("")
        print("ALD: To do list")
        print("")
        print("1. enter to do")
        print("2. view today's list")
        print("5. exit")
        x = int(input("enter option: "))
        if x == 1:
            enter_to_do()
            print("----------------")
        if x == 2:
            view_todays_list()
            print("----------------")

        if x == 5:
            break


if __name__ == "__main__":
    main()
