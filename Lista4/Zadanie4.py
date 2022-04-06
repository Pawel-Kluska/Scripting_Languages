import time


def printer_2(func):
    def wraper():
        start = time.time()
        print("Start time")

        s = 0;
        for i in range(10000000):
            s = s+i
        end = time.time()
        func(end - start)


    return wraper


@printer_2
def printer(string):
    print('Zmierzony czas')
    print(string)


printer()
