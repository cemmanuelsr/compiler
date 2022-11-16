class SymbolTable:
    def __init__(self):
        self.table = {}
        self.shift = 0

    def get(self, k):
        if k not in self.table.keys():
            raise Exception(f'{k} variable never created')
        return self.table[k]

    def create(self, k):
        if k in self.table.keys():
            raise Exception(f'{k} already created on currently scope')
        self.shift += 4
        self.table[k] = self.shift
