class Task():
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        self.tasks.append({'description': description, 'deadline': deadline, 'status': "Not Started"})

    def complete_task(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task ['status'] = "Done"
                print (f'The {task ['description']} has been completed.')
        else:
            print(f"The {task ['description']} has not been found.")

    def show_tasks(self):
        print ('Current Tasks:')
        for task in self.tasks:
            if task['status'] == "Not Started":
                print (f"{task['description']} and {task['deadline']}")


t = Task ()
t.add_task('read a book', "05.06.2023")
t.add_task('run the maraphon', "05.06.2023")
t.add_task('fix a car', "05.06.2023")

t.show_tasks()

t.complete_task('read a book')

t.show_tasks()


