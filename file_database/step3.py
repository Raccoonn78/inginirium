def get_line(): # ввод данных 
    print("Введите ваши данные через пробел (id,имя,фамилию,возраст,рост,вес)")
    s=list(input().split()) # ВВЕСТИ ДАННЫЕ 
    return (int(s[0]), s[1], s[2], int(s[3]), int(s[4]), int(s[5])) 

def insert(line): # добавление данных в базу данных
    if line not in data: # Если такой строки нет в наших данных то они добавляются 
        data.append(line) # добавление 

def print_data(): # вывод в терминал 
    m=max([len(i) for i in columns]) # максимальная длина слова 
    for i in columns:
        print(str(i).ljust(m+1, ' '), end='') # ljust добавляет пробелы к названиям колонок и данныым чтобы вывод был читаемый
    print()
    for line in data:
        for i in line:
            print(str(i).ljust(m+1, ' '), end='')# ljust добавляет пробелы к названиям колонок и данныым чтобы вывод был читаемый
        print()

def write_to_file(filename): # запись в файл  
    with open(filename, 'w') as file:  #способ открытия файлы  ("w"- файл доступен для записи)
        file.write(','.join(columns)+'\n') # соединяем при помощи join введеные данные через запятую 
        for line in data: # перезапись в файл 
            line=[str(i) for i in line]
            file.write(','.join(line)+'\n')

def read_from_file(filename): # чтение из файла  
    with open(filename, 'r') as file: # открываем файл  ('r' -доступ для чтения )
        columns = tuple(file.readline().split(',')) # Запись первой строки с названиями колонок 
        data = [] 
        for line in file: # запись самих данных в переменную data 
            line = line.split(',')
            data.append((int(line[0]), line[1], line[2], int(line[3]), int(line[4]), int(line[5])))  # добавление 
    return columns, data  # 


global data, columns     # глобальные перменные чтобы все функции видели эти переменные , то есть глобальный доступ 
columns, data = read_from_file('C:\\Users\\Дмитрий\\Desktop\\kurs_python\\modul_2\\Step3\\data.csv') # вызов функции для записи в перменные 
#print(data) # вывод данных  , но не название колонок 
print("введите данные, id,имя,фамилия,возраст,рост,вес")
insert(get_line()) # просит пользователя ввести данные , далее она записывает это в data 
print_data() # выводятся данные 
write_to_file('C:\\Users\\Дмитрий\\Desktop\\kurs_python\\modul_2\\Step3\\data.csv') # запись в файл 
columns=('id', 'name', 'lastname', 'age', 'height', 'weight')
data = [
    (1, 'Ivan', 'Ivanov', 14, 160, 50),
    (2, 'Sasha', 'Sidorov', 15, 210, 40),
    (3, 'Masha', 'Poradina', 30, 178, 70),
    (4, 'Timur', 'Korolev', 44, 160, 12)
]
print_data() # вывод данных с колонками 
 







#C:\\Users\\Дмитрий\\Desktop\\kurs_python\\modul_2\\Step3\\data.csv