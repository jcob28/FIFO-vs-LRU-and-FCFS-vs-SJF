import random

for i in range(100):  # wypisanie stu ciągów
    print("Proces no.", i + 1)
    print("______________")


    class Process:
        def __init__(self, at, bt):
            self.at = at  # Arrival Time
            self.bt = bt  # Burst Time


    list = []
    arrival_list = []
    stos = []
    counterr = 0

    for i in range(100):
        temp = Process(random.randint(0, 150), random.randint(1, 10))  # losowanie procesu
        list.append(temp)  # dodanie procesu o losowych parametrach
        counterr += list[i].at

    for i in range(100):  # wypisanie ciągu stu procesów
        print(list[i].at, end=' ')
        print(" ", end=' ')
        print(list[i].bt)

    def fcfs():
        itterator = 0
        counter = 0

        while itterator < 151:  # czy Arrival Time == czas procesora
            for x in range(100):
                var_temp = list[x].at  # jeśli jest, to...
                if var_temp == itterator:
                    counter += list[x].at
                    proces1 = Process(list[x].at, list[x].bt)  # ...dodaj go do kolejki
                    arrival_list.append(proces1)
                    list[x].at = 151  # przypisanie procesowi at spoza zakresu, aby pętla nie znalazła go drugi raz
                    itterator -= 1  # po dodaniu procesu: sprawdenie, czy nie ma drugiego o takim samym at
            itterator += 1

        # for i in range(n):  # wypisywanie procesów w prawidłowej kolejności, w której ze sobą kolidują
        #    print(arrival_list[i].at, end=' ')
        #    print(" ", end=' ')
        #    print(arrival_list[i].bt)

        for i in range(99):
            if (arrival_list[i].at + arrival_list[i].bt) > arrival_list[i].at:  # ustawienie procesów,
                arrival_list[i + 1].at = arrival_list[i].at + arrival_list[i].bt  # aby nie kolidowaly ze sobą

        # for i in range(n):  # wypisywanie procesów w prawidłowej kolejności, w której już ze sobą nie kolidują
        #    print(arrival_list[i].at, end=' ')
        #    print(" ", end=' ')
        #    print(arrival_list[i].bt)

        counter2 = 0
        counter3 = 0
        for i in range(100):
            counter2 += arrival_list[i].at
            counter3 += arrival_list[i].bt

        print("| Średni czas cyklu przetwarzania / FCFS:", (counter2 - counter + counter3) / 100)
        print("| Średni czas oczekiwania na przydzielenie procesora / FCFS:", (counter2 - counter) / 100)


    def sjf():
        stack = []
        final_list = []
        czy_wolne = True
        czas = 0
        i = 0

        while len(final_list) < 100:
            for x in range(100):
                if arrival_list[x].at == i:
                    stack.append(Process(arrival_list[x].at, arrival_list[x].bt))
            if czy_wolne is True and len(stack) > 0:
                stack.sort(key=lambda x: x.bt, reverse=True)
                final_list.append(Process(stack[-1].at, stack[-1].bt))
                czas = stack[-1].bt
                stack.pop(-1)
                czy_wolne = False
            else:
                if czas > 1:
                    czas -= 1
                elif czas == 1:
                    czy_wolne = True
            i += 1

        for i in range(99):
            if (final_list[i].at + final_list[i].bt) > final_list[i].at:  # ustawienie procesów,
                final_list[i + 1].at = final_list[i].at + final_list[i].bt  # aby nie kolidowały ze sobą

        counter2 = 0
        counter3 = 0
        for i in range(100):
            counter2 += final_list[i].at
            counter3 += final_list[i].bt

        print("| Średni czas cyklu przetwarzania / SJF:", (counter2 + counter3 - counterr) / 100)
        print("| Średni czas oczekiwania na przydzielenie procesora / SJF:", (counter2 - counterr) / 100)
        print("")

    # wywołanie funkcji
    fcfs()
    sjf()
