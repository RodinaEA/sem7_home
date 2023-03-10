# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках
# не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, 
# что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# Ввод:  пара-ра-рам рам-пам-папам па-ра-па-дам  Вывод: Парам пам-пам

def rythm(poem):
    poem = poem.lower().split()
    for i in range(len(poem)):
        number = 0
        list = poem[i]
        for s in range(len(list)):
            if list[s] in "аеёиоуыэюя":
                number += 1
        if i == 0:
            count = number
        elif count != number:
            return "Пам парам" 
    return "Парам пам-пам"
check = input("Введите текст стихотворения: ")
print(f"Результат проверки стихов: {rythm(check)}")