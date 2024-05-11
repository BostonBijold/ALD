from flask import Flask, request
import json
import datetime
import pymongo
import todoclass
app = Flask(__name__)

my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["ALD"]
to_do_col = my_db["to_do_items"]


@app.route('/today')
def view_todays_list():
    tasklist = []
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    # completed_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
        new = todoclass.todo_task(x['title'], x["details"], x["priority"], x["deadline"], x["complete"],
                        completed_datetime = 0)
        tasklist.append(vars(new))
    # print(type(vars(tasklist)))
    # Vars() returns the variables and values of a object.

    return tasklist


@app.route('/add-todo-task', methods=['POST'])
def enter_to_do():
    entry = request.json
    to_do_date = datetime.datetime.now()
    to_do_deadline = datetime.datetime(year=to_do_date.year, month=to_do_date.month,
                                       day=to_do_date.day, hour=23, minute=59).strftime("%Y-%m-%d %H:%M:%S")
    to_do_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    to_do_complete = False

    # new = todoclass.todo_task(to_do_title, to_do_details, to_do_priority, to_do_deadline, to_do_complete, completed_datetime= 0)
    # print(new)
    # print(vars(new))

    new_todo = {
        "title": entry['title'],
        "details": entry['details'],
        "date": to_do_date,
        "complete": entry['complete'],
        "deadline": entry['deadline'],
        "priority": entry['priority']
        # completed notes: where users can add notes to a completed task if they want to track how things changed.
        # completed - timestamp: when did a user complete the task, if null the task is incomplete.
    }
    print(new_todo)
    to_do_col.insert_one(new_todo)
    return 'success'

