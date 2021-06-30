import datetime

#Задания и сроки их выполнения.
tasks_date = {
    "Накопить на JBL LIVE 500BT": ["2021.07.24", "2021.08.06"],
    "Посмотреть первый сезон 'Время приключений' на английском": ["2021.07.01", "2021.07.20"],
    "Посмотреть 'Человек-паук через вселенные' на английском": ["2021.08.08", "2021.08.10"],
    "Посмотреть 'Гравити Фолз' на английском": ["2021.07.01", "2021.08.25"],
    "Сделать корабль и переплыть через озеро": ["2021.08.08", "2021.08.15"],
    "Дочитать 'Изучаем Python'": ["2021.07.15", "2021.07.28"],
    "Прочитать 'Python.К вершинам мастерства'": ["2021.06.30", "2021.09.01"],
    "Сделать какой-нибудь проект на Python": ["2021.07.03", "2021.07.10"],
    "Научиться делать 10 подтягиваний": ["2021.07.20", "2021.08.30"],
    "Набрать 50 подписчиков на 'ОКП'" : ["2021.08.10", "2021.09.01"],
    "Открыть MM в Доте": ["2021.08.01", "2021.08.15"],
    "Посмотреть новых смешариков": ["2021.07.03", "2021.07.08"],
    "Научиться печатать 250 символов в минуту в слепую": ["2021.06.30", "2021.09.01"],
    "Изучить GIT": ["2021.07.17", "2021.07.20"],
    "Изучить Linux": ["2021.07.10", "2021.07.17"],
    "Изучить 2 модуля новых в степике": ["2021.09.01", "2021.09.07"],
    "Изучить C# по PDF файлу": ["2021.06.30", "2021.07.20"],
    "Изучить Unity по файлу": ["2021.07.20", "2021.08.10"],
    "Изучить blender по файлу": ["2021.08.10", "2021.09.01"],
    "Изучить геймдизайн по файлу": ["2021.09.01", "2021.09.20"],
    "Начать делать игру 'Посёлок'": ["2021.09.20", "2025.09.20"]
}

#Вытаскивание даты вырезая время.
day_date = str(datetime.datetime.today()).split()[0].split('-')
day_date = ".".join(day_date)

for task, date in tasks_date.items():
    start_date = date[0]
    end_date = date[1]

    if (start_date <= day_date and end_date >= day_date):
        print(task)