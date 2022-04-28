

class ControlledText:

    def __init__(self, text):
        self.text = text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if value.isprintable() and not value.isspace():
            self._text = value
        else:
            raise ValueError('The text must be printable and dont have spaces')

    @text.deleter
    def text(self):
        del self._text

    def __add__(self, x):
        if isinstance(x, ControlledText):
            return ControlledText(self._text + x._text)

    def __eq__(self, x):
        if isinstance(x, ControlledText):
            return self._text == x._text

    def __gt__(self, x):
        if isinstance(x, ControlledText):
            return self._text > x._text

    def __lt__(self, x):
        if isinstance(x, ControlledText):
            return self._text < x._text

    def __str__(self):
        return "Text: {0}, \n".format(self._text)


# text_o1 = ControlledText("hello")
# print(text_o1.text)
# text_o2 = ControlledText("yo")
# print(text_o2.text)

# print(text_o1 < text_o2)
# print(text_o1 > text_o2)
# text_o1.text = "   "
# text_o2.text = "hello there"
# print(text_o2.text)
# print(text_o1.text)





