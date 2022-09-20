class SymbolTable:
    def __init__(self):
        self.table = {}

    def get(self, k):
        if k in self.table.keys():
            return self.table[k]
        raise Exception(f'{k} variable never created')

    def set(self, k, v):
        self.table[k] = v
