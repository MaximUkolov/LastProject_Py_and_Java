import os

# создаем функцию для добавления заметки
def add_note():
    # запрашиваем у пользователя текст заметки
    note = input("Введите текст заметки: ")
    
    # открываем файл заметок в режиме добавления (a)
    with open("notes.txt", "a") as file:
        # записываем заметку в файл
        file.write(note + "\n")
    
    print("Заметка успешно добавлена!")

# создаем функцию для просмотра всех заметок
def view_notes():
    # проверяем, существует ли файл заметок
    if not os.path.exists("notes.txt"):
        print("Заметок нет.")
        return
    
    # открываем файл заметок в режиме чтения (r)
    with open("notes.txt", "r") as file:
        # читаем все заметки из файла
        notes = file.readlines()
        
        # выводим заметки на экран
        for note in notes:
            print(note.strip())

# создаем бесконечный цикл для работы с программой
while True:
    # выводим меню программы
    print("1. Добавить заметку")
    print("2. Просмотреть заметки")
    print("3. Выйти из программы")
    
    # запрашиваем у пользователя выбор действия
    choice = input("Выберите действие: ")
    
    # выполняем действие в зависимости от выбора пользователя
    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        print("До свидания!")
        break
    else:
        print("Некорректный выбор.")