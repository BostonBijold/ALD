import datetime

import pymongo
from datetime import date





myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ALD"]
mycol = mydb["todos"]


def enterTodo():
    todo_title = input("what do you need to do today(title)? ")
    todo_details = input("what do you need to do to complete it? ")
    todo_date = datetime.datetime.now()

    todo_deadline = datetime.datetime(year=todo_date.year, month=todo_date.month, day=todo_date.day, hour=23, minute=59).strftime("%Y-%m-%d %H:%M:%S")
    todo_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    todo_complete = False

    new_todo = {
        "tile": todo_title,
        "details": todo_details,
        "date": todo_date,
        "complete": todo_complete,
        "deadline": todo_deadline
    }
    print(new_todo)



def main():
    while True:
        x = int(input("enter"))
        if x == 1:
            enterTodo()

        if x == 2:
            break


if __name__ == "__main__":
    main()
