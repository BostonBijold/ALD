


class todo_task:
    def __init__(self, title, details, priority, deadline, complete, completed_datetime):
        # self._id = _id # can't be sent in api due to object not being in '' s
        # extract the id out of the object(id) to store locally for APIs.
        self.title = title
        self.details = details
        self.priority = priority
        self.deadline = deadline
        self.complete = complete
        self.completed_datetime = completed_datetime
