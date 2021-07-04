import datetime

def get_tasks():
    """Выкачивание заданий и сроков их выполнения из текстового файла."""
    tasks_date = {}

    with open("input_tasks.txt", "r", encoding="UTF-8") as tasks:
        all_tasks = tasks.readlines()
        #Помещение в словарь отформатированные задание и сроки.

        for task_and_date in all_tasks:
            task_and_date = task_and_date.split(": ") #0 - задание, 1 - сроки.
            end_and_start_dates = task_and_date[1].split(', ') #Формат в виде листа с начальным сроком и конечным нужен для сравнения.
            task = task_and_date[0]
            tasks_date[task] = end_and_start_dates

    return tasks_date

#Вытаскивание даты, вырезая время.
day_date = str(datetime.datetime.today()).split()[0].split("-")
day_date = ".".join(day_date)
tasks_date = get_tasks()

for task, date in tasks_date.items():
    #Начальный и конечный срок выполнения задачи.
    start_date = date[0]
    end_date = date[1]

    if (start_date <= day_date and end_date >= day_date):
        print(task)