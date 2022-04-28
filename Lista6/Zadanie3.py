from Lista6.Zadanie1 import ControlledText


class LastName(ControlledText):

    def __init__(self, name):
        super().__init__(name)
        self.lname = name

    @property
    def lname(self):
        return self.text

    @lname.setter
    def lname(self, value):

        if '-' in value:
            list_names = value.split(sep='-')
            proper_name = ''
            for i in list_names:
                proper_name += i.capitalize()
                proper_name += '-'
            proper_name = proper_name[:len(proper_name) - 1]

            if  value == proper_name:
                self.text = value
            else:
                raise ValueError('The last name should start with capital letter')
        else:
            if value == value.capitalize():
                self.text = value
            else:
                raise ValueError('The last name should start with capital letter')


    @lname.deleter
    def lname(self):
        del self.text


# lname_o = LastName("Kowalski")
# print(lname_o.lname)
# lname_o.lname = "Nowak-Strzala"
# print(lname_o.lname)
# lname_o.lname = "janicki"
