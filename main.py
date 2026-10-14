import json


form = ["priority", "title", "deadline", "details"]

def change_structure(f):
    def main(m):
        x = input("Enter the new value: ")
        f(m, new_value=x)

    return main


def first_input(f):
    inputs = []
    def main(s, chars=[]):
        if chars:
            f(s, chars=chars)
            return None
        for i in form:
            x = input(f"{i}: ")
            inputs.append(x)
        f(s, chars=inputs)
    return main



class Task:
    @first_input
    def __init__(self, chars: list=None, status:bool=False):
        self.priority = chars[0]
        self.title = chars[1]
        self.deadline = chars[2]
        self.details = chars[3]
        self.chars = [self.priority, self.title, self.deadline, self.details]
        self.status = status


    def _update(self):
        self.chars = [self.priority, self.title, self.deadline, self.details]


    def __str__(self) -> str:
        result = ""
        a = dict(zip(form, self.chars))
        for i,j in a.items():
            result += f"{i.title()}: {j}\n"
        return result

    def __repr__(self) -> str:
        return f"{self.title}"

    @change_structure
    def change_title(self, new_value=None):
        self.title = new_value
        self._update()

    @change_structure
    def change_deadline(self, new_value=None):
        self.deadline = new_value
        self._update()

    @change_structure
    def change_details(self, new_value=None):
        self.details = new_value
        self._update()

    @change_structure
    def change_priority(self, new_value=None):
        self.priority = new_value
        self._update()

    def done(self):
        self.status = True


class TaskManager:
    def __init__(self):
        self.tasks = []
        try:
            with open("tasks.json", "r") as f:
                recall_info = json.load(f)
                for i in recall_info:
                    recalled_chars = list(i.values())
                    x = Task(chars=recalled_chars)
                    self.tasks.append(x)
        except FileNotFoundError:
            with open("tasks.json", "w") as f:
                pass

    def save(self):
        to_be_saved = []

        for task in self.tasks:
            to_be_saved.append(dict(zip(form, task.chars)))
        with open("tasks.json", "w") as f:
            json.dump(to_be_saved, f)

    def add(self, new_task: Task):
        self.tasks.append(new_task)

    def find(self, task_title: str) -> Task:
        for task in self.tasks:
            if task.title.title() == task_title.title():
                return task
        return None

    def delete(self, value_for_del):
        self.tasks.remove(value_for_del)



