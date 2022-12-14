from decorators.CompareType import compare_with_int


class Variable:
    def __init__(self, value, cast_function):
        if isinstance(value, bool):
            value = int(value)
        self.value = value
        self.cast_function = cast_function

    def __call__(self):
        return self.cast_function(self.value)

    @compare_with_int('+')
    def __add__(self, other):
        return Variable(self() + other(), self.cast_function)

    @compare_with_int('-')
    def __sub__(self, other):
        return Variable(self() - other(), self.cast_function)

    @compare_with_int('*')
    def __mul__(self, other):
        return Variable(self() * other(), self.cast_function)

    @compare_with_int('/')
    def __floordiv__(self, other):
        return Variable(self() // other(), self.cast_function)

    @compare_with_int('&&')
    def __and__(self, other):
        return Variable(self() and other(), self.cast_function)

    @compare_with_int('||')
    def __or__(self, other):
        return Variable(self() or other(), self.cast_function)

    def __eq__(self, other):
        return Variable(self() == other(), self.cast_function)

    def __lt__(self, other):
        return Variable(self() < other(), self.cast_function)

    def __gt__(self, other):
        return Variable(self() > other(), self.cast_function)

    def __concat__(self, other):
        return Variable(str(self.value) + str(other.value), str)

    @compare_with_int('+')
    def __pos__(self):
        return self

    @compare_with_int('-')
    def __neg__(self):
        return Variable(-self(), self.cast_function)

    @compare_with_int('!')
    def __not__(self):
        return Variable(not self.value, self.cast_function)
