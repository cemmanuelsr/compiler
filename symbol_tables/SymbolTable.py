class SymbolTable:
    def __init__(self):
        self.table = {}
        self.shift = 0

    def get(self, k):
        if k not in self.table.keys():
            raise Exception(f'{k} variable never created')
        return self.table[k]

    def set(self, k, v):
        if k not in self.table.keys():
            raise Exception(f'{k} variable never created')
        if self.table[k][0].cast_function != v.cast_function:
            raise Exception(
                f'Cannot assign {v.value} (which is {v.cast_function}) when {self.table[k].cast_function} is expected')
        self.table[k] = (v, self.table[k][1])

    def create(self, k, v):
        if k in self.table.keys():
            raise Exception(f'{k} already created on actual scope')
        self.shift += 4
        self.table[k] = (v, self.shift)
