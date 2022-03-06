set2 = ('Bread', 3, 43, 5)
set3 = ('Ham', 3, 4, 52)
set4 = ('Cheese', 3, 4, 5)
set5 = ('Vegetables', 34, 4, 5)

set_all = [set2, set3, set4, set5]


def printValuesOld(set_all):
    print('%-12s %8s %8s %8s' % ('Product', 'Amount', 'Vat', 'Price'))
    for i in set_all:
        print('%-12s %8d %8d %8d' % i)


printValuesOld(set_all)
print()


def printValuesNew(set_all):
    print('%-12s %8s %8s %8s' % ('Product', 'Amount', 'Vat', 'Price'))
    for i in set_all:
        print('{0:12s} {1:8d} {2:8d} {3:8d}'.format(i[0], i[1], i[2], i[3]))


printValuesNew(set_all)
