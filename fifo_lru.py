import random

print()

for i in range(100):
    print('#', i + 1)

    los = []
    for i in range(100):
        los.append(random.randint(1, 20))

    print("Ciąg:", *los, sep=' ')  # wypisanie ciągu
    print()


    def fifo():
        ref = []
        list = []
        traf1 = 0
        traf2 = 0
        traf3 = 0

        for i in range(100):
            ref.append(los[i])  # dodanie liczby o losowej wartości

        for i in range(100):
            flag = False
            for x in list:  # sprawdzenie, czy element jest już w ramkach
                if x == ref[i]:
                    flag = True
                    traf1 += 1
            if not flag:  # jeśli nie jest, to:
                if len(list) < 3:  # jesli są jeszcze wolne ramki, to dodawaj
                    list.append(ref[i])
                else:  # jeśli nie ma już wolnych ramek, to usuń z indeksem 0 i dodaj nową na koniec
                    list.pop(0)
                    list.append(ref[i])

        # print("| Liczba trafionych stron / FIFO / 3 ramki:", traf1)
        print("| Liczba brakujących stron / FIFO / 3 ramki:", 100 - traf1)

        for i in range(100):
            flag = False
            for x in list:  # sprawdzenie, czy element jest już w ramkach
                if x == ref[i]:
                    flag = True
                    traf2 += 1
            if not flag:  # jeśli nie jest, to:
                if len(list) < 5:  # jesli są jeszcze wolne ramki, to dodawaj
                    list.append(ref[i])
                else:  # jeśli nie ma już wolnych ramek, to usuń z indeksem 0 i dodaj nową na koniec
                    list.pop(0)
                    list.append(ref[i])

        # print("| Liczba trafionych stron / FIFO / 5 ramek:", traf2)
        print("| Liczba brakujących stron / FIFO / 5 ramek:", 100 - traf2)

        for i in range(100):
            flag = False
            for x in list:  # sprawdzenie, czy element jest już w ramkach
                if x == ref[i]:
                    flag = True
                    traf3 += 1
            if not flag:  # jeśli nie jest, to:
                if len(list) < 7:  # jesli są jeszcze wolne ramki, to dodawaj
                    list.append(ref[i])
                else:  # jeśli nie ma już wolnych ramek, to usuń z indeksem 0 i dodaj nową na koniec
                    list.pop(0)
                    list.append(ref[i])

        # print("| Liczba trafionych stron / FIFO / 7 ramek:", traf3)
        print("| Liczba brakujących stron / FIFO / 7 ramek:", 100 - traf3)


    def lru():
        class Reference:
            def __init__(self, value, step):
                self.value = value
                self.step = step

        ref = []
        list = []
        counter = 1
        traf11 = 0
        traf22 = 0
        traf33 = 0

        for i in range(100):
            ref.append(Reference(los[i], 0))  # dodawanie losowej wartosci do ciagu

        for i in range(100):
            flag = False
            for x in list:
                if x.value == ref[i].value:  # jeśli element jest już w list, to...
                    flag = True
                    x.step = counter  # zaktualizuj mu stepa
                    counter += 1
                    traf11 += 1
            if not flag:  # jeśli go nie ma, to...
                if len(list) < 3:  # jeśli jeszcze nie wszystkie ramki są zapelnione, to dodaj od razu z wpisanym stepem
                    ref[i].step = counter
                    counter += 1
                    list.append(ref[i])
                else:  # a jeśli ramki są już zapełnione, to...
                    min_step = list[0].step
                    for x in list:
                        if x.step < min_step:  # szukanie liczby z najmniejszym stepem
                            min_step = x.step
                    for x in list:
                        if x.step == min_step:
                            list.remove(x)  # usuwanie liczby z najmniejszym stepem
                    ref[i].step = counter
                    counter += 1  # przypisanie odpowiedniego stepu
                    list.append(ref[i])  # dodanie nowego z wpisanym stepem

        # print("| Liczba trafionych stron / LRU / 3 ramki:", traf11)
        print("| Liczba brakujących stron / LRU / 3 ramki:", 100 - traf11)

        for i in range(100):
            flag = False
            for x in list:
                if x.value == ref[i].value:  # jeśli element jest już w list, to...
                    flag = True
                    x.step = counter  # zaktualizuj mu stepa
                    counter += 1
                    traf22 += 1
            if not flag:  # jeśli go nie ma, to...
                if len(list) < 5:  # jeśli jeszcze nie wszystkie ramki są zapelnione, to dodaj od razu z wpisanym stepem
                    ref[i].step = counter
                    counter += 1
                    list.append(ref[i])
                else:  # a jeśli ramki są już zapełnione, to...
                    min_step = list[0].step
                    for x in list:
                        if x.step < min_step:  # szukanie liczby z najmniejszym stepem
                            min_step = x.step
                    for x in list:
                        if x.step == min_step:
                            list.remove(x)  # usuwanie liczby z najmniejszym stepem
                    ref[i].step = counter
                    counter += 1  # przypisanie odpowiedniego stepu
                    list.append(ref[i])  # dodanie nowego z wpisanym stepem

        # print("| Liczba trafionych stron / LRU / 5 ramek:", traf22)
        print("| Liczba brakujących stron / LRU / 5 ramek:", 100 - traf22)

        for i in range(100):
            flag = False
            for x in list:
                if x.value == ref[i].value:  # jeśli element jest już w list, to...
                    flag = True
                    x.step = counter  # zaktualizuj mu stepa
                    counter += 1
                    traf33 += 1
            if not flag:  # jeśli go nie ma, to...
                if len(list) < 7:  # jeśli jeszcze nie wszystkie ramki są zapelnione, to dodaj od razu z wpisanym stepem
                    ref[i].step = counter
                    counter += 1
                    list.append(ref[i])
                else:  # a jeśli ramki są już zapełnione, to...
                    min_step = list[0].step
                    for x in list:
                        if x.step < min_step:  # szukanie liczby z najmniejszym stepem
                            min_step = x.step
                    for x in list:
                        if x.step == min_step:
                            list.remove(x)  # usuwanie liczby z najmniejszym stepem
                    ref[i].step = counter
                    counter += 1  # przypisanie odpowiedniego stepu
                    list.append(ref[i])  # dodanie nowego z wpisanym stepem

        # print("| Liczba trafionych stron / LRU / 7 ramek:", traf33)
        print("| Liczba brakujących stron / LRU / 7 ramek:", 100 - traf33)


    # wywołanie funkcji
    fifo()
    lru()
    print()
