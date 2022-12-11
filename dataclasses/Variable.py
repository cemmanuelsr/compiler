class Type:
    def __init__(self, value, cast_function):
        if isinstance(value, bool):
            value = int(value)
        self.value = value
        self.cast_function = cast_function

    def __call__(self):
        return self.cast_function(self.value)

    def __add__(self, other):
        if self.cast_function != int or other.cast_function != int:
            raise Exception(f'Add expected int and int, got {self.cast_function} and {other.cast_function}')
        return Type(self() + other(), self.cast_function)

    def __sub__(self, other):
        if self.cast_function != int or other.cast_function != int:
            raise Exception(f'Subtraction expected int and int, got {self.cast_function} and {other.cast_function}')
        return Type(self() - other(), self.cast_function)

    def __mul__(self, other):
        if self.cast_function != int or other.cast_function != int:
            raise Exception(f'Multiplication expected int and int, got {self.cast_function} and {other.cast_function}')
        return Type(self() * other(), self.cast_function)

    def __floordiv__(self, other):
        if self.cast_function != int or other.cast_function != int:
            raise Exception(f'Division expected int and int, got {self.cast_function} and {other.cast_function}')
        return Type(self() // other(), self.cast_function)

    def __and__(self, other):
        if self.cast_function != int or other.cast_function != int:
            raise Exception(f'And expected int and int, got {self.cast_function} and {other.cast_function}')
        return Type(self() and other(), self.cast_function)

    def __or__(self, other):
        if self.cast_function != int or other.cast_function != int:
            raise Exception(f'Or expected int and int, got {self.cast_function} and {other.cast_function}')
        return Type(self() or other(), self.cast_function)

    def __eq__(self, other):
        return Type(self() == other(), self.cast_function)

    def __lt__(self, other):
        return Type(self() < other(), self.cast_function)

    def __gt__(self, other):
        return Type(self() > other(), self.cast_function)

    def __concat__(self, other):
        return Type(str(self.value) + str(other.value), str)

    def __pos__(self):
        if self.cast_function != int:
            raise Exception(f'Pos expected int, got {self.cast_function}')
        return self

    def __neg__(self):
        if self.cast_function != int:
            raise Exception(f'Neg expected int, got {self.cast_function}')
        return Type(-self(), self.cast_function)

    def __not__(self):
        if self.cast_function != int:
            raise Exception(f'Not expected int, got {self.cast_function}')
        return Type(not self.value, self.cast_function)
