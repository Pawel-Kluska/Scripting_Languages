list = [19, 3, 15, 43, 98, 16, 9, 23, 4]


def isPrime(num):
    list_of_divisors = []
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                list_of_divisors.append(i)

    return list_of_divisors


for number in list:
    divisors = isPrime(number)
    if divisors:
        print("Liczba {0:d} nie jest liczba pierwsza, oto jej dzielniki {1}".format(number, divisors))
    else:
        print("Liczba {0:d} jest liczba pierwsza".format(number))

list.sort()
print("Posortowana: " + str(list))

list.reverse()
print("Odwrotnie posortowana: " + str(list))

list = [19, 3, 15, 43, 98, 16, 9, 23, 4]

list2 = list[0:3]
list2.sort()
list = list2 + list[3:]
print(list)
